// ============================================================================
// Low Ballerz — Futures & Ballot live predictions feed (Firebase Firestore)
// Not overwritten by build.py — safe to edit. Reuses the same Firebase project
// as the Trash Talk board (window.LOW_BALLERZ_FIREBASE_CONFIG), in a separate
// "predictions2026" collection.
// ============================================================================

const cfg = window.LOW_BALLERZ_FIREBASE_CONFIG || {};
const statusEl = document.getElementById("predictions-live-status");
const feedEl = document.getElementById("predictions-feed");
const formEl = document.getElementById("predictions-form");
const nameEl = document.getElementById("pred-name");
const champEl = document.getElementById("pred-champion");
const lastEl = document.getElementById("pred-lastplace");
const boldEl = document.getElementById("pred-bold");

function showStatus(html) {
  if (!statusEl) return;
  statusEl.style.display = "block";
  statusEl.innerHTML = html;
}

function isConfigured(c) {
  return c && c.apiKey && !String(c.apiKey).startsWith("PASTE_") && c.projectId && !String(c.projectId).startsWith("PASTE_");
}

function escapeText(s) {
  const div = document.createElement("div");
  div.textContent = s;
  return div.innerHTML;
}

function timeAgo(date) {
  if (!date) return "just now";
  const secs = Math.floor((Date.now() - date.getTime()) / 1000);
  if (secs < 30) return "just now";
  if (secs < 60) return secs + "s ago";
  const mins = Math.floor(secs / 60);
  if (mins < 60) return mins + "m ago";
  const hrs = Math.floor(mins / 60);
  if (hrs < 24) return hrs + "h ago";
  const days = Math.floor(hrs / 24);
  if (days < 7) return days + "d ago";
  return date.toLocaleDateString();
}

function renderPredictions(items) {
  if (!feedEl) return;
  if (!items.length) {
    feedEl.innerHTML = '<p class="talk-empty">No predictions locked in yet. Be the first.</p>';
    return;
  }
  feedEl.innerHTML = items.map(function (p) {
    const name = escapeText(p.name || "Anonymous");
    const champ = escapeText(p.champion || "");
    const last = escapeText(p.lastPlace || "");
    const bold = escapeText(p.bold || "");
    const when = timeAgo(p.createdAt);
    return (
      '<div class="talk-comment">' +
        '<div class="talk-comment-head">' +
          '<span class="talk-comment-name">' + name + "</span>" +
          '<span class="talk-comment-time">' + when + "</span>" +
        "</div>" +
        '<div class="talk-comment-msg">' +
          '<strong>Champion:</strong> ' + champ + '<br>' +
          '<strong>Last Place:</strong> ' + last + '<br>' +
          '<strong>Bold Prediction:</strong> ' + bold +
        "</div>" +
      "</div>"
    );
  }).join("");
}

async function init() {
  if (!isConfigured(cfg)) {
    showStatus(
      "<p><strong>Live ballot isn't set up yet.</strong> This site's owner needs to create a free Firebase project " +
      "and paste the config into <code>firebase-config.js</code> (same setup used for the Trash Talk board). " +
      "Until then, this ballot is read-only.</p>"
    );
    if (feedEl) feedEl.innerHTML = '<p class="talk-empty">Live ballot coming soon.</p>';
    if (formEl) {
      const btn = formEl.querySelector(".talk-submit");
      if (btn) { btn.disabled = true; btn.textContent = "Ballot Not Set Up Yet"; }
    }
    return;
  }

  try {
    const { initializeApp } = await import("https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js");
    const {
      getFirestore, collection, addDoc, query, orderBy, limit,
      onSnapshot, serverTimestamp
    } = await import("https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js");

    const app = initializeApp(cfg);
    const db = getFirestore(app);
    const predCol = collection(db, "predictions2026");
    const q = query(predCol, orderBy("createdAt", "desc"), limit(200));

    onSnapshot(q, function (snap) {
      const items = snap.docs.map(function (d) {
        const data = d.data();
        return {
          name: data.name,
          champion: data.champion,
          lastPlace: data.lastPlace,
          bold: data.bold,
          createdAt: data.createdAt && data.createdAt.toDate ? data.createdAt.toDate() : null
        };
      });
      renderPredictions(items);
    }, function (err) {
      console.error(err);
      showStatus("<p><strong>Couldn't load the ballot.</strong> Check the Firestore security rules and project config.</p>");
    });

    if (formEl) {
      formEl.addEventListener("submit", async function (e) {
        e.preventDefault();
        const name = nameEl.value.trim().slice(0, 40);
        const champion = champEl.value.trim().slice(0, 60);
        const lastPlace = lastEl.value.trim().slice(0, 60);
        const bold = boldEl.value.trim().slice(0, 400);
        if (!name || !champion || !lastPlace || !bold) return;
        const btn = formEl.querySelector(".talk-submit");
        if (btn) { btn.disabled = true; btn.textContent = "Locking In..."; }
        try {
          await addDoc(predCol, { name, champion, lastPlace, bold, createdAt: serverTimestamp() });
          champEl.value = ""; lastEl.value = ""; boldEl.value = "";
        } catch (err) {
          console.error(err);
          showStatus("<p><strong>Couldn't submit.</strong> Check the Firestore security rules allow writes to the 'predictions2026' collection.</p>");
        } finally {
          if (btn) { btn.disabled = false; btn.textContent = "Lock In My Picks"; }
        }
      });
    }
  } catch (err) {
    console.error(err);
    showStatus("<p><strong>Ballot failed to load.</strong> This can happen if the page is opened as a local file instead of a hosted page.</p>");
  }
}

init();

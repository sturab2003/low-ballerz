// ============================================================================
// Low Ballerz — Trash Talk live board (Firebase Firestore, real-time)
// Not overwritten by build.py — safe to edit.
// ============================================================================

const cfg = window.LOW_BALLERZ_FIREBASE_CONFIG || {};
const statusEl = document.getElementById("talk-live-status");
const feedEl = document.getElementById("talk-feed");
const formEl = document.getElementById("talk-form");
const nameEl = document.getElementById("talk-name");
const msgEl = document.getElementById("talk-message");

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

function renderComments(items) {
  if (!feedEl) return;
  if (!items.length) {
    feedEl.innerHTML = '<p class="talk-empty">No posts yet. Be the first to talk some trash.</p>';
    return;
  }
  feedEl.innerHTML = items.map(function (c) {
    const name = escapeText(c.name || "Anonymous");
    const msg = escapeText(c.message || "");
    const when = timeAgo(c.createdAt);
    return (
      '<div class="talk-comment">' +
        '<div class="talk-comment-head">' +
          '<span class="talk-comment-name">' + name + "</span>" +
          '<span class="talk-comment-time">' + when + "</span>" +
        "</div>" +
        '<div class="talk-comment-msg">' + msg + "</div>" +
      "</div>"
    );
  }).join("");
}

async function init() {
  if (!isConfigured(cfg)) {
    showStatus(
      "<p><strong>Live board isn't set up yet.</strong> This site's owner needs to create a free Firebase project " +
      "and paste the config into <code>firebase-config.js</code> — instructions are in that file. " +
      "Until then, this board is read-only.</p>"
    );
    if (feedEl) feedEl.innerHTML = '<p class="talk-empty">Live board coming soon.</p>';
    if (formEl) {
      const btn = formEl.querySelector(".talk-submit");
      if (btn) { btn.disabled = true; btn.textContent = "Board Not Set Up Yet"; }
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
    const talkCol = collection(db, "trashtalk");
    const q = query(talkCol, orderBy("createdAt", "desc"), limit(200));

    onSnapshot(q, function (snap) {
      const items = snap.docs.map(function (d) {
        const data = d.data();
        return {
          name: data.name,
          message: data.message,
          createdAt: data.createdAt && data.createdAt.toDate ? data.createdAt.toDate() : null
        };
      });
      renderComments(items);
    }, function (err) {
      console.error(err);
      showStatus("<p><strong>Couldn't load the live board.</strong> Check the Firestore security rules and project config.</p>");
    });

    if (formEl) {
      formEl.addEventListener("submit", async function (e) {
        e.preventDefault();
        const name = nameEl.value.trim().slice(0, 40);
        const message = msgEl.value.trim().slice(0, 400);
        if (!name || !message) return;
        const btn = formEl.querySelector(".talk-submit");
        if (btn) { btn.disabled = true; btn.textContent = "Posting..."; }
        try {
          await addDoc(talkCol, { name: name, message: message, createdAt: serverTimestamp() });
          msgEl.value = "";
        } catch (err) {
          console.error(err);
          showStatus("<p><strong>Couldn't post.</strong> Check the Firestore security rules allow writes to the 'trashtalk' collection.</p>");
        } finally {
          if (btn) { btn.disabled = false; btn.textContent = "Post It"; }
        }
      });
    }
  } catch (err) {
    console.error(err);
    showStatus("<p><strong>Live board failed to load.</strong> This can happen if the page is opened as a local file instead of a hosted page — host the site (Netlify/Vercel/GitHub Pages) and try again.</p>");
  }
}

init();

// ============================================================================
// Low Ballerz — Draft Central live board (Firebase Firestore, real-time)
// Not overwritten by build.py — safe to edit. Reuses the same Firebase project
// as the Trash Talk board (window.LOW_BALLERZ_FIREBASE_CONFIG), in a separate
// "draftboard2026" collection.
// ============================================================================

const cfg = window.LOW_BALLERZ_FIREBASE_CONFIG || {};
const statusEl = document.getElementById("draft-live-status");
const cells = document.querySelectorAll(".draft-cell");

// ---- Position color-coding: match typed/synced cell text against the known player pool ----
const POS_MAP = window.LOW_BALLERZ_PLAYER_POSITIONS || {};
const POS_NAMES_SORTED = Object.keys(POS_MAP).sort(function (a, b) { return b.length - a.length; });
const POS_CLASSES = ["pos-QB", "pos-RB", "pos-WR", "pos-TE", "pos-K", "pos-DEF"];

function detectPosition(text) {
  if (!text) return null;
  const t = text.toLowerCase();
  for (let i = 0; i < POS_NAMES_SORTED.length; i++) {
    const name = POS_NAMES_SORTED[i];
    if (t.indexOf(name.toLowerCase()) !== -1) return POS_MAP[name];
  }
  return null;
}

function applyPositionColor(cell) {
  const pos = detectPosition(cell.textContent);
  cell.classList.remove.apply(cell.classList, POS_CLASSES);
  if (pos) cell.classList.add("pos-" + pos);
}

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

async function init() {
  if (!isConfigured(cfg)) {
    showStatus(
      "<p><strong>Live draft board isn't set up yet.</strong> This site's owner needs to create a free Firebase " +
      "project and paste the config into <code>firebase-config.js</code> (same setup used for the Trash Talk board). " +
      "Until then, this board is local-only and won't sync between visitors.</p>"
    );
    return;
  }

  try {
    const { initializeApp } = await import("https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js");
    const {
      getFirestore, doc, setDoc, onSnapshot, collection
    } = await import("https://www.gstatic.com/firebasejs/10.13.0/firebase-firestore.js");

    const app = initializeApp(cfg);
    const db = getFirestore(app);
    const boardCol = collection(db, "draftboard2026");

    cells.forEach(function (cell) {
      const cellId = cell.getAttribute("data-cell-id");
      const cellRef = doc(boardCol, cellId);

      onSnapshot(cellRef, function (snap) {
        if (document.activeElement === cell) return; // don't clobber while typing
        const data = snap.data();
        const text = data && data.pick ? data.pick : "";
        if (cell.textContent !== text) cell.textContent = text;
        applyPositionColor(cell);
      }, function (err) {
        console.error(err);
      });

      let saveTimer = null;
      cell.addEventListener("input", function () {
        cell.classList.remove("cell-saved");
        applyPositionColor(cell);
        if (saveTimer) clearTimeout(saveTimer);
        saveTimer = setTimeout(function () { save(); }, 600);
      });
      cell.addEventListener("blur", function () {
        if (saveTimer) clearTimeout(saveTimer);
        save();
      });
      cell.addEventListener("keydown", function (e) {
        if (e.key === "Enter") { e.preventDefault(); cell.blur(); }
      });

      function save() {
        const text = cell.textContent.trim().slice(0, 60);
        setDoc(cellRef, { pick: text, updatedAt: Date.now() }, { merge: true })
          .then(function () { cell.classList.add("cell-saved"); })
          .catch(function (err) {
            console.error(err);
            showStatus("<p><strong>Couldn't save that pick.</strong> Check the Firestore security rules allow writes to the 'draftboard2026' collection.</p>");
          });
      }
    });
  } catch (err) {
    console.error(err);
    showStatus("<p><strong>Live draft board failed to load.</strong> This can happen if the page is opened as a local file instead of a hosted page.</p>");
  }
}

init();

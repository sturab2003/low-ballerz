// ============================================================================
// Low Ballerz — Trash Talk live board configuration
// ============================================================================
// This file is NOT overwritten when you re-run build.py, so it's safe to edit.
//
// To turn on the live trash talk board:
//   1. Go to https://console.firebase.google.com and create a free project
//      (no credit card required). Any name is fine, e.g. "low-ballerz".
//   2. In the project, click "Build > Firestore Database" > Create database >
//      start in PRODUCTION mode (any region is fine).
//   3. Once created, go to the Firestore "Rules" tab and replace the rules
//      with the ones in FIRESTORE-RULES.txt (in this same folder), then Publish.
//   4. Back in the project Overview page, click the "</>" (Web) icon to
//      register a web app (any nickname). Firebase will show you a config
//      object that looks like the one below — copy those exact values in.
//   5. Save this file. Reload trash-talk.html (on a hosted URL, not file://)
//      and the live board will be active.
//
// These values are NOT secret — Firebase web config is meant to be public.
// Access control is handled by the Firestore security rules in step 3.
// ============================================================================

window.LOW_BALLERZ_FIREBASE_CONFIG = {
  apiKey: "AIzaSyB79lvZ9-F7RABKMOiEbgAKLSoehv7sECA",
  authDomain: "low-ballerz.firebaseapp.com",
  projectId: "low-ballerz",
  storageBucket: "low-ballerz.firebasestorage.app",
  messagingSenderId: "430804372437",
  appId: "1:430804372437:web:826044750d7379a6d38b5c"
};

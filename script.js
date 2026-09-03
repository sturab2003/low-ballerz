document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('siteNav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
  }

  var weekTabs = document.querySelectorAll('.week-tab');
  if (weekTabs.length) {
    weekTabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        var week = tab.getAttribute('data-week');
        document.querySelectorAll('.week-tab').forEach(function (t) { t.classList.remove('active'); });
        document.querySelectorAll('.week-panel').forEach(function (p) { p.classList.remove('active'); });
        tab.classList.add('active');
        var panel = document.getElementById(week);
        if (panel) panel.classList.add('active');
      });
    });
  }

  // ---- Sortable tables (click header to sort) ----
  document.querySelectorAll('table.sortable').forEach(function (table) {
    var tbody = table.querySelector('tbody');
    var headers = table.querySelectorAll('th[data-sort]');
    headers.forEach(function (th, idx) {
      th.addEventListener('click', function () {
        var type = th.getAttribute('data-sort');
        var key = th.getAttribute('data-key');
        var rows = Array.prototype.slice.call(tbody.querySelectorAll('tr'));
        var asc = !th.classList.contains('sort-asc');
        headers.forEach(function (h) { h.classList.remove('sort-asc', 'sort-desc'); });
        th.classList.add(asc ? 'sort-asc' : 'sort-desc');
        rows.sort(function (r1, r2) {
          var v1, v2;
          if (key) {
            v1 = parseFloat(r1.getAttribute('data-' + key)) || 0;
            v2 = parseFloat(r2.getAttribute('data-' + key)) || 0;
          } else {
            v1 = r1.children[idx].textContent.trim();
            v2 = r2.children[idx].textContent.trim();
            if (type === 'num') { v1 = parseFloat(v1) || 0; v2 = parseFloat(v2) || 0; }
          }
          if (v1 < v2) return asc ? -1 : 1;
          if (v1 > v2) return asc ? 1 : -1;
          return 0;
        });
        rows.forEach(function (r) { tbody.appendChild(r); });
      });
    });
  });

  // ---- Highlight & scroll to a #mgr-... row (arrived here from a Managers card) ----
  var hash = window.location.hash;
  if (hash && hash.indexOf('#mgr-') === 0) {
    var targetRow = document.querySelector(hash);
    if (targetRow) {
      setTimeout(function () {
        targetRow.scrollIntoView({ behavior: 'smooth', block: 'center' });
        targetRow.classList.add('row-highlight');
      }, 80);
    }
  }

  // ---- Trade Analyzer ----
  var taRoot = document.getElementById('trade-analyzer');
  if (taRoot && window.LOW_BALLERZ_TRADE_DATA) {
    var TA_DATA = window.LOW_BALLERZ_TRADE_DATA;
    var TA_NEED = window.LOW_BALLERZ_TRADE_NEED || {};
    var teamASelect = document.getElementById('ta-team-a');
    var teamBSelect = document.getElementById('ta-team-b');
    var rosterA = document.getElementById('ta-roster-a');
    var rosterB = document.getElementById('ta-roster-b');
    var simulateBtn = document.getElementById('ta-simulate-btn');
    var confirmOverlay = document.getElementById('ta-confirm-overlay');
    var confirmAName = document.getElementById('ta-confirm-a-name');
    var confirmBName = document.getElementById('ta-confirm-b-name');
    var confirmAList = document.getElementById('ta-confirm-a-list');
    var confirmBList = document.getElementById('ta-confirm-b-list');
    var confirmCancelBtn = document.getElementById('ta-confirm-cancel');
    var confirmCloseBtn = document.getElementById('ta-confirm-close');
    var confirmTradeBtn = document.getElementById('ta-confirm-trade');
    var resultOverlay = document.getElementById('ta-result-overlay');
    var resultFill = document.getElementById('ta-result-fill');
    var verdictEl = document.getElementById('ta-verdict');
    var totalsEl = document.getElementById('ta-totals');
    var resultCloseBtn = document.getElementById('ta-result-close');
    var resultNewTradeBtn = document.getElementById('ta-result-newtrade');
    var selected = { a: {}, b: {} };

    // Roster Fit: how much the RECEIVING team currently needs (or is already deep
    // at) a given position, based on their real roster minus whatever they're
    // simultaneously sending away in this same trade.
    function taTeamPositionCounts(team, excludeNames) {
      var counts = {};
      (TA_DATA[team] || []).forEach(function (p) {
        if (excludeNames.indexOf(p.name) !== -1) return;
        counts[p.pos] = (counts[p.pos] || 0) + 1;
      });
      return counts;
    }

    function taFitInfo(receivingTeam, pos, excludeNames) {
      var thresholds = TA_NEED[pos];
      if (!thresholds || !receivingTeam) return { mult: 1, tag: null };
      var counts = taTeamPositionCounts(receivingTeam, excludeNames);
      var count = counts[pos] || 0;
      if (count < thresholds.low) return { mult: 1.12, tag: 'need' };
      if (count >= thresholds.high) return { mult: 0.92, tag: 'deep' };
      return { mult: 1, tag: null };
    }

    function taOutgoingNames(side) {
      return Object.keys(selected[side]).map(function (k) { return selected[side][k].name; });
    }

    function taAdjustedValue(side, idx) {
      var p = selected[side][idx];
      if (!p) return 0;
      var receivingTeam = side === 'a' ? teamBSelect.value : teamASelect.value;
      var otherSide = side === 'a' ? 'b' : 'a';
      var fit = taFitInfo(receivingTeam, p.pos, taOutgoingNames(otherSide));
      return p.value * fit.mult;
    }

    function taSum(side) {
      var total = 0;
      Object.keys(selected[side]).forEach(function (k) { total += taAdjustedValue(side, k); });
      return total;
    }

    function taUpdateFitBadges() {
      ['a', 'b'].forEach(function (side) {
        var container = side === 'a' ? rosterA : rosterB;
        var receivingTeam = side === 'a' ? teamBSelect.value : teamASelect.value;
        var otherSide = side === 'a' ? 'b' : 'a';
        var excludeNames = taOutgoingNames(otherSide);
        container.querySelectorAll('.ta-player').forEach(function (label) {
          var existingBadge = label.querySelector('.ta-fit-badge');
          if (existingBadge) existingBadge.remove();
          if (!label.classList.contains('ta-selected')) return;
          var idx = label.getAttribute('data-idx');
          var p = selected[side][idx];
          if (!p) return;
          var fit = taFitInfo(receivingTeam, p.pos, excludeNames);
          if (fit.tag) {
            var badge = document.createElement('span');
            badge.className = 'ta-fit-badge ta-fit-' + fit.tag;
            badge.textContent = fit.tag === 'need' ? 'Need' : 'Deep';
            label.appendChild(badge);
          }
        });
      });
    }

    // Live feedback while picking players (fit badges + enabling the Simulate
    // button) — the actual value/verdict math only runs once the trade is confirmed.
    function taRefreshSelectionState() {
      taUpdateFitBadges();
      var countA = Object.keys(selected.a).length, countB = Object.keys(selected.b).length;
      simulateBtn.disabled = !(countA > 0 && countB > 0);
    }

    function taKeeperBadge(p) {
      if (!p.keeper) return '';
      return p.keeperFinalYear
        ? '<span class="ta-keeper-badge ta-keeper-final" title="Already in year 2+ of being kept — can\'t be kept again next season, only rented for the rest of this one">Last Yr</span>'
        : '<span class="ta-keeper-badge ta-keeper-renewable" title="First year as a keeper — still eligible to be kept one more season">Renewable</span>';
    }

    function taRenderConfirmList(container, side) {
      var html = '';
      Object.keys(selected[side]).forEach(function (idx) {
        var p = selected[side][idx];
        var star = p.keeper ? ' ⭐' : '';
        html += '<div class="ta-confirm-player pos-' + p.pos + '">' +
          '<span class="ta-player-name">' + p.name + star + '</span>' +
          '<span class="ta-player-pos">' + p.pos + '</span>' +
          '<span class="ta-player-value">' + p.value.toFixed(1) + '</span>' +
          taKeeperBadge(p) +
          '</div>';
      });
      container.innerHTML = html || '<p class="ta-placeholder">No players selected.</p>';
    }

    function taOpenConfirmModal() {
      var teamAName = teamASelect.value || 'Team A';
      var teamBName = teamBSelect.value || 'Team B';
      confirmAName.textContent = teamAName + ' sends';
      confirmBName.textContent = teamBName + ' sends';
      taRenderConfirmList(confirmAList, 'a');
      taRenderConfirmList(confirmBList, 'b');
      confirmOverlay.classList.add('ta-modal-open');
    }

    function taCloseConfirmModal() {
      confirmOverlay.classList.remove('ta-modal-open');
    }

    function taShowResult() {
      var sumA = taSum('a'), sumB = taSum('b');
      var countA = Object.keys(selected.a).length, countB = Object.keys(selected.b).length;
      var total = sumA + sumB;
      var pctA = total > 0 ? (sumA / total) * 100 : 50;
      resultFill.style.width = pctA + '%';

      var teamAName = teamASelect.value || 'Team A';
      var teamBName = teamBSelect.value || 'Team B';
      var diffPct = total > 0 ? Math.abs(sumA - sumB) / total * 100 : 0;
      // sumA = value A gives up (adjusted for B's need); sumB = value B gives up
      // (adjusted for A's need). Whoever gives up LESS than they receive wins.
      var winner = sumB > sumA ? teamAName : teamBName;
      var verdict, tier;
      if (diffPct < 7) {
        verdict = 'Fair Trade — both sides walk away even.';
        tier = 'fair';
      } else if (diffPct < 18) {
        verdict = 'Slight Win for ' + winner + '.';
        tier = 'slight';
      } else if (diffPct < 35) {
        verdict = 'Clear Win for ' + winner + '.';
        tier = 'clear';
      } else {
        verdict = 'Lopsided — ' + winner + ' wins big.';
        tier = 'lopsided';
      }
      verdictEl.textContent = verdict;
      verdictEl.className = 'ta-verdict' + (tier ? ' ta-verdict-' + tier : '');
      totalsEl.innerHTML =
        '<div class="ta-total-card"><strong>' + teamAName + '</strong> sends ' + countA + ' player' + (countA === 1 ? '' : 's') + ' &middot; value delivered ' + sumA.toFixed(1) + '</div>' +
        '<div class="ta-total-card"><strong>' + teamBName + '</strong> sends ' + countB + ' player' + (countB === 1 ? '' : 's') + ' &middot; value delivered ' + sumB.toFixed(1) + '</div>';

      resultOverlay.classList.add('ta-modal-open');
    }

    function taCloseResultModal() {
      resultOverlay.classList.remove('ta-modal-open');
    }

    function taResetTrade() {
      selected = { a: {}, b: {} };
      [rosterA, rosterB].forEach(function (container) {
        container.querySelectorAll('.ta-checkbox').forEach(function (cb) { cb.checked = false; });
        container.querySelectorAll('.ta-player').forEach(function (label) {
          label.classList.remove('ta-selected');
          var badge = label.querySelector('.ta-fit-badge');
          if (badge) badge.remove();
        });
      });
      simulateBtn.disabled = true;
    }

    function taRenderRoster(team, container, side) {
      selected[side] = {};
      if (!team || !TA_DATA[team]) {
        container.innerHTML = '<p class="ta-placeholder">Pick a team to see its roster.</p>';
        taRefreshSelectionState();
        return;
      }
      var html = '';
      TA_DATA[team].forEach(function (p, idx) {
        var star = p.keeper ? ' ⭐' : '';
        html += '<label class="ta-player pos-' + p.pos + '" data-idx="' + idx + '">' +
          '<input type="checkbox" class="ta-checkbox">' +
          '<span class="ta-player-name">' + p.name + star + '</span>' +
          '<span class="ta-player-pos">' + p.pos + '</span>' +
          taKeeperBadge(p) +
          '<span class="ta-player-value">' + p.value.toFixed(1) + '</span>' +
          '</label>';
      });
      container.innerHTML = html;
      container.querySelectorAll('.ta-player').forEach(function (label) {
        var checkbox = label.querySelector('.ta-checkbox');
        checkbox.addEventListener('change', function () {
          var idx = label.getAttribute('data-idx');
          label.classList.toggle('ta-selected', checkbox.checked);
          if (checkbox.checked) { selected[side][idx] = TA_DATA[team][idx]; }
          else { delete selected[side][idx]; }
          taRefreshSelectionState();
        });
      });
      taRefreshSelectionState();
    }

    teamASelect.addEventListener('change', function () { taRenderRoster(teamASelect.value, rosterA, 'a'); });
    teamBSelect.addEventListener('change', function () { taRenderRoster(teamBSelect.value, rosterB, 'b'); });

    simulateBtn.addEventListener('click', taOpenConfirmModal);
    confirmCancelBtn.addEventListener('click', taCloseConfirmModal);
    confirmCloseBtn.addEventListener('click', taCloseConfirmModal);
    confirmOverlay.addEventListener('click', function (e) { if (e.target === confirmOverlay) taCloseConfirmModal(); });
    confirmTradeBtn.addEventListener('click', function () {
      taCloseConfirmModal();
      taShowResult();
    });

    resultCloseBtn.addEventListener('click', taCloseResultModal);
    resultOverlay.addEventListener('click', function (e) { if (e.target === resultOverlay) taCloseResultModal(); });
    resultNewTradeBtn.addEventListener('click', function () {
      taCloseResultModal();
      taResetTrade();
    });
  }

  // ---- Countdown timer (Draft Central) ----
  var countdownEl = document.getElementById('draft-countdown');
  if (countdownEl) {
    var target = new Date(countdownEl.getAttribute('data-target')).getTime();
    var dEl = document.getElementById('cd-days');
    var hEl = document.getElementById('cd-hours');
    var mEl = document.getElementById('cd-mins');
    var sEl = document.getElementById('cd-secs');
    function tick() {
      var diff = target - Date.now();
      if (diff <= 0) {
        dEl.textContent = hEl.textContent = mEl.textContent = sEl.textContent = '0';
        return;
      }
      var days = Math.floor(diff / (1000 * 60 * 60 * 24));
      var hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
      var mins = Math.floor((diff / (1000 * 60)) % 60);
      var secs = Math.floor((diff / 1000) % 60);
      dEl.textContent = days;
      hEl.textContent = hours;
      mEl.textContent = mins;
      sEl.textContent = secs;
    }
    tick();
    setInterval(tick, 1000);
  }

  // ---- Randomize draft order (visual only, not persisted) ----
  var randomizeBtn = document.getElementById('randomize-order-btn');
  if (randomizeBtn) {
    randomizeBtn.addEventListener('click', function () {
      var tbody = document.querySelector('#draft-order-table tbody');
      var rows = Array.prototype.slice.call(tbody.querySelectorAll('tr'));
      for (var i = rows.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = rows[i]; rows[i] = rows[j]; rows[j] = tmp;
      }
      rows.forEach(function (r, i) {
        r.children[0].textContent = (i + 1);
        tbody.appendChild(r);
      });
    });
  }
});

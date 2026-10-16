(function () {
  "use strict";
  var root = document.documentElement;

  /* ---------- Theme toggle ---------- */
  function currentTheme() {
    var set = root.getAttribute("data-theme");
    if (set) return set;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function applyTheme(t) {
    root.setAttribute("data-theme", t);
    var btn = document.querySelector(".theme-toggle");
    if (btn) {
      btn.setAttribute("aria-label", t === "dark" ? "Switch to light mode" : "Switch to dark mode");
      btn.setAttribute("aria-pressed", t === "dark" ? "true" : "false");
    }
  }
  applyTheme(currentTheme());
  var toggle = document.querySelector(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      applyTheme(next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var onChange = function (e) {
      var saved = null;
      try { saved = localStorage.getItem("theme"); } catch (err) {}
      if (!saved) applyTheme(e.matches ? "dark" : "light");
    };
    if (mq.addEventListener) mq.addEventListener("change", onChange);
  }

  /* ---------- Hero figure: play once ---------- */
  var fig = document.querySelector(".dist");
  if (fig) {
    var agg = fig.querySelector(".agg");
    if (agg && agg.getTotalLength) {
      agg.style.setProperty("--len", Math.ceil(agg.getTotalLength()));
    }
    if ("IntersectionObserver" in window) {
      var dio = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { fig.classList.add("play"); dio.disconnect(); }
        });
      }, { threshold: 0.5 });
      dio.observe(fig);
    } else {
      fig.classList.add("play");
    }
  }

  /* ---------- Dissertation figure: reveal once when scrolled into view ---------- */
  var tfig = document.querySelector(".thesis-fig");
  if (tfig && "IntersectionObserver" in window) {
    tfig.classList.add("armed");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { tfig.classList.add("play"); io.disconnect(); }
      });
    }, { threshold: 0.35 });
    io.observe(tfig);
  }

  /* ---------- Publications: filters ---------- */
  var chips = document.querySelectorAll(".chip[data-filter]");
  var pubs = document.querySelectorAll(".pub[data-theme-tags]");
  var groups = document.querySelectorAll(".year-group");
  var status = document.querySelector(".status");

  function applyFilter(f) {
    var shown = 0;
    pubs.forEach(function (p) {
      var tags = p.getAttribute("data-theme-tags").split(" ");
      var ok = f === "all" || tags.indexOf(f) !== -1;
      p.hidden = !ok;
      if (ok) shown++;
    });
    groups.forEach(function (g) {
      g.hidden = g.querySelectorAll(".pub:not([hidden])").length === 0;
    });
    chips.forEach(function (c) {
      c.setAttribute("aria-pressed", c.getAttribute("data-filter") === f ? "true" : "false");
    });
    if (status) status.textContent = "Showing " + shown + (shown === 1 ? " publication" : " publications");
  }
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var f = c.getAttribute("data-filter");
      applyFilter(f);
      if (history.replaceState) history.replaceState(null, "", f === "all" ? location.pathname : "#" + f);
    });
  });
  if (chips.length) {
    var initial = (location.hash || "").replace("#", "");
    var valid = Array.prototype.some.call(chips, function (c) { return c.getAttribute("data-filter") === initial; });
    applyFilter(valid ? initial : "all");
  }

  /* ---------- Publications: expand / collapse all abstracts ---------- */
  var expand = document.querySelector("[data-expand-all]");
  if (expand) {
    expand.addEventListener("click", function () {
      var all = document.querySelectorAll(".pub:not([hidden]) details");
      var anyClosed = Array.prototype.some.call(all, function (d) { return !d.open; });
      all.forEach(function (d) { d.open = anyClosed; });
      expand.textContent = anyClosed ? "Collapse all abstracts" : "Expand all abstracts";
    });
  }

  /* Open an abstract when arriving via a #paper-id link */
  if (location.hash) {
    var target = document.getElementById(location.hash.slice(1));
    if (target && target.classList.contains("pub")) {
      var d = target.querySelector("details");
      if (d) d.open = true;
    }
  }
})();

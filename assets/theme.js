/* 深色 / 浅色模式切换。注入到导航栏，偏好存于 localStorage，跨页保持。 */
(function () {
  var KEY = 'uo_theme';

  function getPref() {
    try {
      var s = localStorage.getItem(KEY);
      if (s === 'dark' || s === 'light') return s;
    } catch (e) {}
    try {
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) return 'dark';
    } catch (e) {}
    return 'light';
  }

  function apply(t) {
    document.documentElement.setAttribute('data-theme', t);
  }

  // 尽早应用，避免浅色闪烁
  apply(getPref());

  function buildBtn() {
    if (document.getElementById('theme-toggle')) return;
    var nav = document.querySelector('.site-nav') ||
              document.querySelector('header.site') ||
              document.querySelector('nav');
    if (!nav) return;

    var btn = document.createElement('button');
    btn.id = 'theme-toggle';
    btn.type = 'button';
    btn.className = 'theme-toggle';
    btn.setAttribute('aria-label', '切换深色 / 浅色模式');

    function paint() {
      var dark = document.documentElement.getAttribute('data-theme') === 'dark';
      btn.textContent = dark ? '☀ 浅色' : '🌙 深色';
    }
    paint();

    btn.addEventListener('click', function () {
      var cur = document.documentElement.getAttribute('data-theme');
      var next = cur === 'dark' ? 'light' : 'dark';
      apply(next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
      paint();
    });

    nav.appendChild(btn);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildBtn);
  } else {
    buildBtn();
  }
})();

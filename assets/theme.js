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

  // 全局署名条：插入到导航栏之后，所有页面生效
  function buildCredit() {
    if (document.getElementById('site-credit')) return;
    var nav = document.querySelector('.site-nav') ||
              document.querySelector('header.site');
    if (!nav || !nav.parentNode) return;
    var bar = document.createElement('div');
    bar.id = 'site-credit';
    bar.className = 'site-credit';
    bar.textContent = '收集整理：Snowman Liang ｜ 如发现错误请联系整理者：QQ16873486 ｜ 更新日期：2026年8月12日';
    nav.parentNode.insertBefore(bar, nav.nextSibling);
  }

  // 清除遗留的“本地预览版”字样（旧页脚）
  function fixFooters() {
    var footers = document.querySelectorAll('footer');
    for (var i = 0; i < footers.length; i++) {
      var f = footers[i];
      if (f.innerHTML.indexOf('本地预览版') !== -1) {
        f.innerHTML = f.innerHTML
          .replace(/本地预览版\s*·\s*/, '')
          .replace(/本地预览版/, '');
      }
    }
  }

  function init() {
    buildBtn();
    buildCredit();
    fixFooters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

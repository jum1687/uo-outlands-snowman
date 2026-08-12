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

  // 清除遗留的"本地预览版"字样（旧页脚）
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

  // 汉堡菜单（≤768px 手机时生效）
  function buildHamburger() {
    if (document.getElementById('nav-hamburger')) return;
    var nav = document.querySelector('.site-nav') ||
              document.querySelector('header.site');
    if (!nav) return;
    var btn = document.createElement('button');
    btn.id = 'nav-hamburger';
    btn.type = 'button';
    btn.className = 'nav-hamburger';
    btn.innerHTML = '&#9776;';  // ☰
    btn.setAttribute('aria-label', '菜单');
    btn.addEventListener('click', function(e){
      e.stopPropagation();
      nav.classList.toggle('nav-open');
    });
    nav.appendChild(btn);
    // 点页面其他区域关闭菜单
    document.addEventListener('click', function(e){
      if (!nav.contains(e.target)) nav.classList.remove('nav-open');
    });
  }

  // 模拟器手机端 Tab 切换
  function buildSimTabs() {
    if (document.getElementById('sim-mobile-tabs')) return;
    var wrap = document.getElementById('sim');
    if (!wrap) return;
    var tabs = document.createElement('div');
    tabs.id = 'sim-mobile-tabs';
    tabs.className = 'sim-mobile-tabs';
    var clsList = ['Attack','Utility','Tank'];
    var zh = {Attack:'攻击',Utility:'辅助',Tank:'坦克'};
    var activeClass = 'Attack';
    for (var i=0;i<clsList.length;i++){
      var t = document.createElement('button');
      t.className = 'sim-tab-btn' + (clsList[i]===activeClass?' active':'');
      t.textContent = zh[clsList[i]];
      t.setAttribute('data-cls', clsList[i]);
      t.addEventListener('click', function(){
        document.querySelectorAll('.sim-tab-btn').forEach(function(b){b.classList.remove('active');});
        this.classList.add('active');
        var cls = this.getAttribute('data-cls');
        document.querySelectorAll('.sim-col').forEach(function(c){
          c.style.display = c.id === 'col-'+cls ? '' : 'none';
        });
      });
      tabs.appendChild(t);
    }
    wrap.parentNode.insertBefore(tabs, wrap);
    // 仅移动端：默认显示 Attack，隐藏其他列
    if(window.innerWidth<=768){
      document.querySelectorAll('.sim-col').forEach(function(c){
        c.style.display = c.id === 'col-Attack' ? '' : 'none';
      });
    }else{
      // 桌面端：确保所有列都可见（防止手机切过的状态残留）
      document.querySelectorAll('.sim-col').forEach(function(c){
        c.style.display = '';
      });
    }
  }

  // 窗口尺寸变化时同步模拟器列显示
  window.addEventListener('resize',function(){
    var tabs=document.getElementById('sim-mobile-tabs');
    if(!tabs)return;
    if(window.innerWidth<=768){
      var activeTab=document.querySelector('.sim-tab-btn.active');
      var showCls = activeTab ? activeTab.getAttribute('data-cls') : 'Attack';
      document.querySelectorAll('.sim-col').forEach(function(c){
        c.style.display = c.id === 'col-'+showCls ? '' : 'none';
      });
    }else{
      document.querySelectorAll('.sim-col').forEach(function(c){c.style.display='';});
    }
  });

  function init() {
    buildBtn();
    buildCredit();
    buildHamburger();
    buildSimTabs();
    fixFooters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

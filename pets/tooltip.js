// 技能链接悬浮提示：鼠标移上去，跟随鼠标显示技能详细说明。
(function () {
  function ensureTip() {
    var t = document.getElementById('ability-tip');
    if (!t) {
      t = document.createElement('div');
      t.id = 'ability-tip';
      t.className = 'tooltip';
      document.body.appendChild(t);
    }
    return t;
  }

  function moveTip(e, tip) {
    var x = e.clientX, y = e.clientY;
    var w = tip.offsetWidth, h = tip.offsetHeight;
    var nx = x + 14;
    if (nx + w > window.innerWidth - 8) nx = x - w - 14;
    var ny = y + 14;
    if (ny + h > window.innerHeight - 8) ny = y - h - 14;
    if (nx < 8) nx = 8;
    if (ny < 8) ny = 8;
    tip.style.left = nx + 'px';
    tip.style.top = ny + 'px';
  }

  document.addEventListener('DOMContentLoaded', function () {
    var tip = ensureTip();
    var nodes = document.querySelectorAll('[data-ability]');
    Array.prototype.forEach.call(nodes, function (el) {
      el.addEventListener('mouseenter', function (e) {
        var s = el.getAttribute('data-ability');
        var a = window.ABILITIES && window.ABILITIES[s];
        if (!a) return;
        tip.innerHTML = '<div class="tip-name">' + a.name + '</div><div class="tip-desc">' + a.desc + '</div>';
        tip.style.display = 'block';
        moveTip(e, tip);
      });
      el.addEventListener('mousemove', function (e) { moveTip(e, tip); });
      el.addEventListener('mouseleave', function () { tip.style.display = 'none'; });
    });
  });
})();

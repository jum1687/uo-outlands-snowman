# -*- coding: utf-8 -*-
import os

WEB = r"C:/Users/Snowman/WorkBuddy/2026-08-06-22-17-01/outlands-wiki-cn/web"
CODEX_DIR = os.path.join(WEB, "codex")
os.makedirs(CODEX_DIR, exist_ok=True)

SRC = "https://wiki.uooutlands.com/Weapon_and_Parry_Codex"

# ===== 背景音乐块（与现有板块一致）=====
BGM = '''<audio id="bgm" loop preload="auto" src="../assets/music/buccaneers-den.mp3"></audio>
<div class="bgm-ctrl" id="bgmCtrl">
  <button class="bgm-toggle" id="bgmToggle" aria-label="播放/暂停背景音乐" title="播放/暂停：Buccaneer's Den">
    <svg class="icon-play" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
    <svg class="icon-pause" viewBox="0 0 24 24" fill="currentColor"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
  </button>
  <button class="bgm-mute" id="bgmMute" aria-label="静音/取消静音" title="静音">
    <svg class="icon-sound" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3z"/><path d="M16 8a4 4 0 010 8" fill="none" stroke="currentColor" stroke-width="2"/><path d="M18.5 5.5a8 8 0 010 13" fill="none" stroke="currentColor" stroke-width="2"/></svg>
    <svg class="icon-muted" viewBox="0 0 24 24" fill="currentColor"><path d="M3 9v6h4l5 5V4L7 9H3z"/><path d="M16 9l5 5M21 9l-5 5" fill="none" stroke="currentColor" stroke-width="2"/></svg>
  </button>
  <input type="range" class="bgm-vol" id="bgmVol" min="0" max="1" step="0.01" value="0.5" aria-label="音量">
</div>
<script>
(function(){
  var KEY_P='uo_bgm_playing', KEY_M='uo_bgm_muted', KEY_V='uo_bgm_vol', KEY_T='uo_bgm_time';
  var bgm=document.getElementById('bgm');
  var toggle=document.getElementById('bgmToggle');
  var mute=document.getElementById('bgmMute');
  var vol=document.getElementById('bgmVol');
  var playing=false;
  function setPlaying(p){playing=p;toggle.classList.toggle('playing',p);}
  var v=parseFloat(localStorage.getItem(KEY_V)); if(isNaN(v))v=0.5;
  bgm.volume=v; vol.value=v;
  var muted=localStorage.getItem(KEY_M)==='1';
  bgm.muted=muted; mute.classList.toggle('muted',muted);
  var intendPlay=localStorage.getItem(KEY_P)==='1';
  function saveTime(){ try{localStorage.setItem(KEY_T,String(bgm.currentTime||0));}catch(e){} }
  bgm.addEventListener('timeupdate',saveTime);
  window.addEventListener('pagehide',saveTime);
  function startFrom(t){
    if(t>0 && isFinite(t)){ try{bgm.currentTime=t;}catch(e){} }
    bgm.play().then(function(){setPlaying(true);}).catch(function(){});
  }
  if(intendPlay){
    var t=parseFloat(localStorage.getItem(KEY_T))||0;
    if(bgm.readyState>=1){ startFrom(t); }
    else { bgm.addEventListener('loadedmetadata',function(){startFrom(t);},{once:true}); }
  }
  toggle.addEventListener('click',function(){
    if(playing){bgm.pause();localStorage.setItem(KEY_P,'0');setPlaying(false);}
    else{bgm.play().then(function(){localStorage.setItem(KEY_P,'1');setPlaying(true);}).catch(function(){});}
  });
  bgm.addEventListener('play',function(){setPlaying(true);localStorage.setItem(KEY_P,'1');});
  mute.addEventListener('click',function(){
    bgm.muted=!bgm.muted;
    mute.classList.toggle('muted',bgm.muted);
    localStorage.setItem(KEY_M,bgm.muted?'1':'0');
  });
  vol.addEventListener('input',function(){
    var val=parseFloat(vol.value);
    bgm.volume=val;
    localStorage.setItem(KEY_V,String(val));
    if(val>0 && bgm.muted){bgm.muted=false;mute.classList.remove('muted');localStorage.setItem(KEY_M,'0');}
  });
})();
</script>

<style>
.bgm-ctrl{position:fixed;right:18px;bottom:18px;z-index:60;display:flex;align-items:center;gap:6px;
  background:rgba(255,255,255,.92);border:1px solid #c8ccd1;border-radius:24px;padding:6px 10px 6px 6px;
  box-shadow:0 2px 10px rgba(0,0,0,.12);}
.bgm-toggle,.bgm-mute{width:36px;height:36px;border-radius:50%;border:1px solid #c8ccd1;background:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;color:#36c;flex-shrink:0;transition:background .2s,color .2s;}
.bgm-toggle:hover,.bgm-mute:hover{background:#eef3fb;}
.bgm-toggle svg,.bgm-mute svg{width:18px;height:18px;}
.bgm-toggle.playing{background:#36c;color:#fff;border-color:#36c;}
.bgm-mute.muted{background:#e74c3c;color:#fff;border-color:#e74c3c;}
.bgm-toggle .icon-pause,.bgm-mute .icon-muted{display:none;}
.bgm-toggle.playing .icon-play{display:none;}
.bgm-toggle.playing .icon-pause{display:block;}
.bgm-mute.muted .icon-sound{display:none;}
.bgm-mute.muted .icon-muted{display:block;}
.bgm-vol{width:80px;accent-color:#36c;cursor:pointer;}
@media(max-width:600px){.bgm-vol{width:56px;}.bgm-ctrl{right:10px;bottom:10px;}}
</style>'''

# 当前 codex 下拉菜单（生成时列出全部宝典，便于互跳）
def codex_dropdown_items():
    items = []
    for c in CODEXS:
        items.append('      <a href="%s.html">%s <span class="en">%s</span></a>' % (c["slug"], c["cn"], c["en"]))
    return "\n".join(items)

NAV_TMPL = '''<nav class="site-nav">
  <span class="nav-brand">UO Outlands 中文资料库</span>
  <a href="../index.html">首页</a>
  <a href="../skills/index.html">技能详解</a>
  <a href="../elements/index.html">元素精通</a>
  <div class="nav-dropdown">
    <a href="../pets/index.html">宠物图鉴</a>
    <div class="nav-menu">
      <a href="../pets/index.html">可驯服宠物</a>
      <a href="../pets/follower-abilities.html">宠物技能大全</a>
      <a href="../pets/simulator.html">宠物天赋模拟器</a>
    </div>
  </div>
  <div class="nav-dropdown">
    <a href="index.html">宝典图鉴</a>
    <div class="nav-menu">
@@DROPDOWN@@
    </div>
  </div>
</nav>'''

def rows(items):
    out = []
    for en, cn, desc in items:
        out.append('    <tr><td>%s <span class="en-cell">%s</span></td><td>%s</td></tr>' % (cn, en, desc))
    return "\n".join(out)

def detail_page(c):
    st = '''  <h2>姿态 <span class="en-h">Stances</span></h2>
  <table class="aspect-data-table">
    <tr><th>姿态 <span class="en-cell">Stance</span></th><th>效果 <span class="en-cell">Effect</span></th></tr>
@@S@@
  </table>'''.replace("@@S@@", rows(c["stances"]))
    fi = '''  <h2>终结技 <span class="en-h">Finishers</span></h2>
  <table class="aspect-data-table">
    <tr><th>终结技 <span class="en-cell">Finisher</span></th><th>效果 <span class="en-cell">Effect</span></th></tr>
@@F@@
  </table>'''.replace("@@F@@", rows(c["finishers"]))
    ab = ""
    if c.get("abilities"):
        ab = '''  <h2>武器能力 <span class="en-h">Weapon Abilities</span></h2>
  <table class="aspect-data-table">
    <tr><th>能力 <span class="en-cell">Ability</span></th><th>效果 <span class="en-cell">Effect</span></th></tr>
@@A@@
  </table>'''.replace("@@A@@", rows(c["abilities"]))
    html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@CN@@（@@EN@@）宝典 | UO Outlands 中文资料库</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
@@NAV@@
<nav class="breadcrumb"><a href="../index.html">资料库首页</a> › <a href="index.html">宝典图鉴</a> › <span>@@CN@@ @@EN@@</span></nav>
<div class="source-link">官方原文：<a href="@@SRC@@" target="_blank" rel="noopener">wiki.uooutlands.com/Weapon_and_Parry_Codex</a></div>
<div class="mw-body">
  <h1 class="mw-page-title-main">@@CN@@ <span class="cnsub">@@EN@@ 宝典</span></h1>
  <div class="pet-summary">类型 <b>@@TYPE@@</b> · 使用要求 <b>@@REQ@@</b></div>
  <p>@@INTRO@@</p>
@@ST@@
@@FI@@
@@AB@@
  <p class="backlink"><a href="index.html">← 返回宝典图鉴</a></p>
</div>
<footer>
  <div><b>资料来源：</b>译自官方 Wiki <a href="@@SRC@@" target="_blank" rel="noopener">wiki.uooutlands.com/Weapon_and_Parry_Codex</a>，非官方整理，仅供学习交流；数值以官方 Discord 补丁公告为准。</div>
  <div>UO Outlands 中文资料库 · 本地预览版 · 2026-08-08</div>
</footer>
@@BGM@@
</body>
</html>'''
    html = (html
        .replace("@@CN@@", c["cn"]).replace("@@EN@@", c["en"])
        .replace("@@NAV@@", NAV).replace("@@SRC@@", SRC)
        .replace("@@TYPE@@", c["type"]).replace("@@REQ@@", c["req"])
        .replace("@@INTRO@@", c["intro"]).replace("@@ST@@", st)
        .replace("@@FI@@", fi).replace("@@AB@@", ab).replace("@@BGM@@", BGM))
    return html

# ===== 数据 =====
CODEXS = [
 {
  "slug":"arcane","cn":"奥术","en":"Arcane","type":"武器 Weapon",
  "req":"80 徒手(Wrestling) + 80 魔法(Magery) + 80 奥术(Arcane)",
  "intro":"奥术宝典是武器与格挡宝典体系中唯一以法术为核心的武器分支，围绕「奥术蓄积 Arcane Buildup」与「元素特攻 Aspect Special」运作。",
  "stances":[
    ("Leech","吸取","奥术法力恢复几率每级 +1.5%"),
    ("Shield","护盾","武器挥击使你的伤害减免提升 3%/级，奥术法力恢复几率 +1%/级，持续 5 秒（不叠加）"),
    ("Scatter","散射","对 3 格内额外 2 个随机目标各造成 1%/级的伤害，每命中一个额外目标奥术法力恢复几率 +1.25%/级"),
    ("Fracture","碎裂","目标每有 25 点护甲值（最多 100），伤害 +2%/级，奥术法力恢复几率 +0.75%/级"),
    ("Surge","涌动","若过去 15 秒触发过元素特攻(Aspect Special)，伤害 +8%/级，奥术法力恢复几率 +2.5%/级"),
  ],
  "finishers":[
    ("Clarity","明澈","对目标造成 300% 伤害，接下来 15 秒所有元素近战特攻触发几率 +20%（不叠加），奥术法力恢复几率 +10%（不叠加）"),
    ("Catalyst","催化","对目标造成 300% 伤害，消耗全部奥术蓄积(Arcane Buildup)，每消耗 1 点蓄积伤害 +7%，并恢复 30×消耗点数的法力"),
  ],
  "abilities":[
    ("Seeking","觅的","接下来 15 秒命中率 +25%，攻击速度 +15%"),
    ("Leyline","灵线","接下来 15 秒每 3 秒恢复 5 点法力"),
    ("Soulfire","魂火","接下来 15 秒奥术蓄积对法术伤害的加成 +50%，但对伤害减免的加成 -100%"),
  ],
 },
 {
  "slug":"archery","cn":"弓箭","en":"Archery","type":"武器 Weapon",
  "req":"80 战术(Tactics) + 80 弓箭(Archery)",
  "intro":"弓箭宝典专注于远程输出的姿态、终结技与能力。",
  "stances":[
    ("Arcane","奥术","命中率与伤害每级 +3%"),
    ("Fowling","诱禽","武器射击使对目标的伤害减免提升 6%/级，持续 5 秒（不叠加）"),
    ("Incendiary","燃烧","对 2 格内随机目标额外造成 8%/级的伤害"),
    ("Longshot","远射","射程 +(等级/2 向上取整)，伤害 +3%/级"),
    ("Maiming","致残","阻碍(Hinder)效果持续时长每级 +10%，过载阻碍(Overpowered Hinder)效果额外伤害 +10%/级"),
  ],
  "finishers":[
    ("Ricochet","跳弹","对目标造成 300% 伤害，并对目标 6 格内最多 2 个额外随机敌人造成同等伤害"),
    ("Pincushion","针垫","对目标进行 8 次攻击，每次有 66% 命中几率造成 100% 伤害"),
  ],
  "abilities":[
    ("Skirmish","游击","接下来 15 秒伤害 +25%，且可在移动中射击"),
    ("Full Draw","满弓","接下来 15 秒伤害 +35%，但需静止 5 秒才能射击"),
    ("Repeater","连射","若未潜行，立即进行 3 次额外攻击尝试，每次有 66% 几率造成 100% 武器伤害（按武器速度缩放）"),
  ],
 },
 {
  "slug":"dual-wielding","cn":"双持","en":"Dual Wielding","type":"武器 Weapon",
  "req":"80 战术(Tactics) + 80 双持(Dual Wielding)",
  "intro":"双持宝典强化双武器战斗，利用正面 / 侧面 / 背面弧线获得不同加成。",
  "stances":[
    ("Aggressive","进攻","武器特攻触发几率 +4%/级"),
    ("Defensive","防守","伤害 +2%/级，武器挥击使你对所有敌人的伤害减免提升 4%/级，持续 5 秒（不叠加）"),
    ("Cleave","横扫","对 2 格内随机敌人造成 10%/级 的伤害"),
    ("Square Off","摆架","命中率 +2%/级，有效格挡(Effective Parry) +2/级；处于目标正面弧线时加成翻倍"),
    ("Shank","暗刺","伤害 +2%/级，攻击速度 +1%/级；处于目标侧面或背面弧线时加成翻倍"),
  ],
  "finishers":[
    ("En Garde","警戒","对目标造成 600% 伤害，获得 5 点伤害护盾持续 15 秒（不叠加）；处于目标正面弧线时护盾升至 15；仇恨提升 15 秒"),
    ("Coup de Grace","致命一击","对目标造成 400% 伤害；处于目标侧面或背面弧线时伤害额外 +400%；仇恨降低 15 秒"),
  ],
  "abilities":[
    ("Bladewhirl","旋风刃","若未潜行，立即对 4 格内最多 4 个其他目标进行近战攻击，造成 100% 武器伤害（按武器速度缩放）"),
    ("Knightly","骑士","提升仇恨，并使对敌人正面弧线内的命中率与近战伤害 +20%，持续 15 秒"),
    ("Knave","无赖","降低仇恨，并使对敌人侧面或背面弧线内的近战伤害 +35%，持续 15 秒"),
  ],
 },
 {
  "slug":"fencing","cn":"细剑","en":"Fencing","type":"武器 Weapon",
  "req":"80 战术(Tactics) + 80 细剑(Fencing)",
  "intro":"细剑宝典强调攻击速度、中毒与暗杀式终结技。",
  "stances":[
    ("Aggressive","进攻","攻击速度 +2.5%/级，但玩家受到的所有伤害 +1%/级"),
    ("Defensive","防守","武器挥击使你对所有敌人的伤害减免提升 4%/级，持续 5 秒（不叠加）"),
    ("Cleave","横扫","对 2 格内随机目标额外造成 8%/级的伤害"),
    ("Blackguard","恶徒","成功命中时有 4%/级 几率对目标施加疾病(Disease)效果，造成 200% 伤害分摊在 20 秒内（潜行攻击则造成 66% 伤害）"),
    ("Fang","獠牙","使用涂有（大|致命|致死）毒药的武器时，伤害 +(3%|3.5%|4%)/级；若满足涂抹该毒药所需的最低毒药(Poisoning)技能（印刷值），加成翻倍"),
  ],
  "finishers":[
    ("Assassinate","刺杀","造成 400% 伤害，并立即结算目标身上最多额外 500% 伤害值的疾病与中毒持续伤害（由玩家造成）"),
    ("Flurry","乱舞","攻击速度 +15%，持续 20 秒（不叠加）"),
  ],
  "abilities":[
    ("Gambit","赌注","接下来 15 秒伤害 +40%，但有 10% 几率任何命中转为未命中"),
    ("Swiftstrikes","疾刺","接下来 15 秒每次命中提升攻击速度 5%（按武器速度缩放），最高 +25%"),
    ("Bane","灾厄","若玩家对怪物施加了武器毒药，立即结算 3 层中毒持续伤害"),
  ],
 },
 {
  "slug":"fishing","cn":"钓鱼","en":"Fishing","type":"武器 Weapon",
  "req":"80 战术(Tactics) + 80 钓鱼(Fishing)",
  "intro":"钓鱼宝典兼具陆上与海上（船只）战斗能力，部分效果在船上大幅增强。",
  "stances":[
    ("Snipe","狙击","命中率 +4%/级"),
    ("Pin Down","钉住","武器挥击使你对所有敌人的伤害减免提升 4%/级，持续 5 秒（不叠加）"),
    ("Skewer","穿刺","对 2 格内随机目标额外造成 6%/级的伤害，并有 2%/级 几率对两个目标施加 25 点持续 15 秒的穿刺(Pierce)效果"),
    ("Strafe","穿插","若玩家的船在最近 0.5 秒内移动过，伤害 +4%/级，若目标不在同一艘船上则加成翻倍"),
    ("Heave","投掷","[海上] 射程 +1/级，伤害 +10%/级，但有 2%/级 几率任何命中转为未命中"),
  ],
  "finishers":[
    ("Run Through","贯穿","对目标造成 600% 伤害"),
    ("Salvo","齐射","对目标造成 600% 伤害"),
  ],
  "abilities":[
    ("Rouse","激励","接下来 15 秒船只全体船员造成的所有伤害 +40%"),
    ("Scourge","鞭笞","接下来 15 秒穿刺(Impale)武器特攻将额外命中 2 个目标，或为每个未使用的额外目标附加 30% 伤害加成"),
    ("Buoy","浮标","立即恢复每名船员 7.5% 的生命值"),
  ],
 },
 {
  "slug":"macing","cn":"锤类","en":"Macing","type":"武器 Weapon",
  "req":"80 战术(Tactics) + 80 锤类(Macing)",
  "intro":"锤类宝典以高伤害与穿刺(Pierce)强化见长。",
  "stances":[
    ("Aggressive","进攻","伤害 +7%/级"),
    ("Defensive","防守","伤害 +2%/级，武器挥击使你对所有敌人的伤害减免提升 4%/级，持续 5 秒（不叠加）"),
    ("Cleave","横扫","对 2 格内随机敌人造成 10%/级 的伤害"),
    ("Wild Swing","狂挥","命中率 -2%/级，但伤害 +10%/级"),
    ("Sunder","破甲","穿刺(Pierce)效果额外 +5 点护甲削减/级，且伤害 +4%/级"),
  ],
  "finishers":[
    ("Pulverize","粉碎","若目标身上有穿刺(Pierce)效果，则取消该效果并将伤害额外 +350%"),
    ("Shatter","碎裂","对目标造成 500%+ 伤害"),
  ],
  "abilities":[
    ("Pummel","重击","接下来 15 秒每次命中伤害 +10%（按武器速度缩放），最高 +40%"),
    ("Stun","眩晕","接下来 15 秒武器特攻还会对目标施加 (穿刺值/10) 秒的阻碍(Hinder)"),
    ("Smash","猛砸","触发该能力的近战命中伤害 +300%（按武器速度缩放），但有 25% 几率改为仅造成 1 点伤害"),
  ],
 },
 {
  "slug":"swords","cn":"剑术","en":"Swords","type":"武器 Weapon",
  "req":"80 战术(Tactics) + 80 剑术(Swordsmanship)",
  "intro":"剑术宝典攻守兼备，并强化流血(Bleed)效果。",
  "stances":[
    ("Aggressive","进攻","命中率与伤害 +3.5%/级，但玩家受到伤害 +1%/级"),
    ("Defensive","防守","武器挥击使你对所有敌人的伤害减免提升 4%/级，持续 5 秒（不叠加）"),
    ("Cleave","横扫","对 2 格内随机目标额外造成 8%/级的伤害"),
    ("Warrior","战士","命中率、防御与伤害 +2%/级"),
    ("Flaying","剥皮","非元素(Aspect)流血(Bleed)伤害 +10%/级"),
  ],
  "finishers":[
    ("Bleed Out","放血","施加相当于 500% 伤害的流血(Bleed)效果（仅获得 Flaying 姿态 50% 的加成）"),
    ("Execute","处决","对目标造成 350% 伤害，并立即结算目标身上由玩家造成的所有剩余流血(Bleed)持续伤害"),
  ],
  "abilities":[
    ("Spinslash","旋斩","接下来 15 秒命中率、伤害与武器特攻触发几率 +15%"),
    ("Rend","撕裂","立即结算目标身上所有玩家造成的流血(Bleed)持续伤害，并在接下来 15 秒新产生的武器特攻流血效果伤害 +25%"),
    ("Chop","劈砍","触发该能力的近战命中伤害 +200%（按武器速度缩放）"),
  ],
 },
 {
  "slug":"throwing","cn":"投掷","en":"Throwing","type":"武器 Weapon",
  "req":"80 战术(Tactics) + 80 投掷(Throwing)",
  "intro":"投掷宝典擅长移动中攻击与范围控制。",
  "stances":[
    ("Torrent","激流","近战命中累积提升攻击速度 1.0%/级（上限 5 次命中）；切换姿态、5 秒未命中或命中 5 次后重置"),
    ("Suppress","压制","伤害 +2%/级，武器挥击使你对所有敌人的伤害减免提升 4%/级，持续 5 秒（不叠加）"),
    ("Reaper","收割","对 2 格内额外 2 个随机目标造成 8%/级的伤害"),
    ("Rake","耙击","伤害 +3%/级，在移动投掷(Moving Throws)时加成翻倍"),
    ("Kite","风筝","命中率 +1%/级，伤害 +2%/级；若目标在 1 秒内移动过则加成翻倍"),
  ],
  "finishers":[
    ("Hunter","猎手","对目标造成 400% 伤害；接下来 15 秒玩家近战伤害 +10%，对同一屠杀组(Slayer Group)目标翻倍（不叠加）"),
    ("Hobble","绊跌","目标每移动一步受到 120% 伤害，直到 20 秒经过或移动 10 步（不叠加）"),
  ],
  "abilities":[
    ("Clash","冲突","15 秒内对 2 格内的目标获得 +10% 命中率、+10% 伤害减免、+20% 近战伤害"),
    ("Blitz","突袭","15 秒内玩家拥有无限移动投掷(Moving Throws)，且若未静止 1 秒以上则获得 +15% 挥击速度"),
    ("Hail Mary","远投","15 秒内攻击距离 +4，若与目标距离 9 格或以上则近战伤害 +30%"),
  ],
 },
 {
  "slug":"wrestling","cn":"徒手","en":"Wrestling","type":"武器 Weapon",
  "req":"80 战术(Tactics) + 80 徒手(Wrestling)",
  "intro":"徒手宝典以贴身缠斗、生命与资源回复为特色。",
  "stances":[
    ("Dragon","龙","武器特攻将消耗最多 5 点法力，每消耗 1 点法力伤害 +5%/级（采纳姿态后前 10 秒加成翻倍）"),
    ("Crab","蟹","武器挥击使你对所有敌人的伤害减免提升 3%/级，持续 5 秒（不叠加）（采纳姿态后前 10 秒加成翻倍）"),
    ("Spider","蛛","对 2 格内额外 2 个随机目标造成 5%/级的伤害（采纳姿态后前 10 秒加成翻倍）"),
    ("Monkey","猴","连续命中 3 次后，第 3 次命中伤害 +15%/级（采纳姿态后前 10 秒加成翻倍）"),
    ("Crane","鹤","近战命中时有 2.5%/级 几率恢复 10 点生命（采纳姿态后前 10 秒加成翻倍）"),
  ],
  "finishers":[
    ("Chi Thrust","气劲","对目标造成 150% 武器伤害，将消耗最多 25 点法力，每消耗 1 点法力伤害 +50%"),
    ("Zen Strike","禅击","对目标造成 350% 伤害，并恢复 25 生命、25 耐力、25 法力"),
  ],
  "abilities":[
    ("Brawl","搏斗","接下来 15 秒每次命中命中率、伤害与攻击速度 +4%（按武器速度缩放），最高 +20%"),
    ("Haymaker","重拳","接下来 15 秒玩家可在目标生命 50% 或以下时触发终结技，或对 Boss 在 45 秒冷却后触发"),
    ("Takedown","擒抱","触发该能力的近战命中 100% 触发武器特攻，并施加 300% 普通武器特攻效果"),
  ],
 },
 {
  "slug":"parrying","cn":"格挡","en":"Parrying","type":"格挡 Parry",
  "req":"80 战术(Tactics) 或 80 徒手(Wrestling) + 80 格挡(Parrying)",
  "intro":"格挡宝典是防御向分支，提供姿态与终结技，无独立武器能力(Weapon Abilities)。装备双手武器或盾牌时获得经验。",
  "stances":[
    ("Shield Bash","盾击","对战斗对象的伤害减免 +3%/级，被战斗对象近战命中时有 4%/级 几率对其施加 3 秒阻碍(Hinder)"),
    ("Warding","守护","中毒、流血、疾病持续伤害 -8%/级"),
    ("Testudo","龟甲","每有一个敌对生物对你产生仇恨，伤害减免 +1.5%/级，最多 5 个生物"),
    ("Mirror","镜反","受到的法术伤害 -7%/级"),
    ("Bulwark","壁垒","若玩家静止 3 秒或以上，伤害减免 +5%/级"),
  ],
  "finishers":[
    ("Last Stand","背水","有 5%/级 几率将受到的任何伤害减至 1"),
    ("Barrier","屏障","有 10%/级 几率将任何中毒、流血、疾病持续伤害减至 1"),
  ],
  "abilities":[],
 },
]

# 宝典导航下拉需在 CODEXS 定义后构造
NAV = NAV_TMPL.replace("@@DROPDOWN@@", codex_dropdown_items())

# ===== 生成详情页 =====
for c in CODEXS:
    with open(os.path.join(CODEX_DIR, c["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(detail_page(c))
print("generated", len(CODEXS), "detail pages")

# ===== 生成宝典首页 index.html =====
xp_rows = """    <tr><td>1</td><td>4</td><td>20,000</td></tr>
    <tr><td>2</td><td>8</td><td>40,000</td></tr>
    <tr><td>3</td><td>12</td><td>60,000</td></tr>
    <tr><td>4</td><td>16</td><td>80,000</td></tr>
    <tr><td>5</td><td>20</td><td>100,000</td></tr>
    <tr><td>6</td><td>40</td><td>200,000</td></tr>
    <tr><td>7</td><td>60</td><td>300,000</td></tr>
    <tr><td>武器能力 Weapon Abilities</td><td>50</td><td>250,000</td></tr>"""

list_rows = []
for c in CODEXS:
    list_rows.append(
      '    <tr><td><a href="%s.html">%s</a> <span class="en-cell">%s</span></td>'
      '<td>%s</td><td>%s</td><td>%s</td><td><a href="%s.html">查看详情 →</a></td></tr>'
      % (c["slug"], c["cn"], c["en"], c["type"], c["req"], c["intro"], c["slug"]))
list_rows = "\n".join(list_rows)

index_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>宝典图鉴（Codex）| UO Outlands 中文资料库</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
@@NAV@@
<nav class="breadcrumb"><a href="../index.html">资料库首页</a> › <span>宝典图鉴 Codex</span></nav>
<div class="source-link">官方原文：<a href="@@SRC@@" target="_blank" rel="noopener">wiki.uooutlands.com/Weapon_and_Parry_Codex</a></div>
<div class="mw-body">
  <h1 class="mw-page-title-main">宝典图鉴 <span class="cnsub">Codex</span></h1>
  <div class="mw-content">
    <h2>什么是宝典 <span class="en-h">What is a Codex</span></h2>
    <p>宝典（Codex）是 Outlands 中以<strong>武器与格挡</strong>为核心的玩家进程系统（player progression system）。玩家通过升级宝典<strong>姿态（Stances）</strong>，解锁对应武器技能的<strong>终结技（Finishers）</strong>与<strong>武器能力（Weapon Abilities）</strong>，从而强化战斗。宝典可用<a href="../skills/inscription.html">抄写（Inscription）</a>技能制作，全部为<strong>祝福（Blessed）</strong>状态、不可被盗。</p>
    <p>每个角色的宝典档案<strong>按角色永久保存</strong>（与物品本身无关），即使宝典丢失进度也不丢；但玩家仍需将宝典放在<strong>背包中</strong>才能获取经验并激活姿态 / 终结技 / 能力。</p>
    <h2>使用条件 <span class="en-h">Requirements</span></h2>
    <ul>
      <li>武器宝典：至少 <b>80 战术（Tactics）</b>与 <b>80 点对应武器技能</b>（奥术 Arcane 例外，需 80 徒手 / 80 魔法 / 80 奥术）。</li>
      <li>格挡宝典：至少 <b>80 战术</b> 或 <b>80 徒手 + 80 格挡（Parrying）</b>。</li>
      <li>技能要求基于<strong>印刷技能（printed skill）</strong>，武器附带的战术加成不计入 80 要求。</li>
      <li>宝典在<strong>庇护岛（Shelter Island）</strong>不获得经验；武器能力与终结技无法在<strong>背刺（backstab）</strong>上触发。</li>
    </ul>
    <h2>经验与升级 <span class="en-h">Experience &amp; Upgrade Points</span></h2>
    <p>用符合技能要求的武器击杀怪物获得经验（可同时升级多个宝典）；格挡宝典在装备双手武器或盾牌时获得经验。每 <b>5,000 gold</b> 经验 = 1 升级点。姿态可升至 Rank 7；Rank 5 解锁第一层终结技，每多一级 Rank 5 姿态解锁一层；每个武器宝典有 3 个武器能力，各需 50 点解锁，需充满武器能力槽（每 6 秒回充 10% + 10%×臂力 Arms Lore/100，默认 60 秒充满，最高 24 秒）。</p>
    <table class="aspect-data-table">
      <tr><th>等级 <span class="en-cell">Rank</span></th><th>升级点 <span class="en-cell">Upgrade Points</span></th><th>所需经验 <span class="en-cell">XP Needed</span></th></tr>
@@XP@@
    </table>
    <h2>宝典列表 <span class="en-h">Codex List</span></h2>
    <p class="note">武器与格挡宝典（Weapon and Parry Codex）共细分为以下 10 个分支，点击进入各宝典查看姿态 / 终结技 / 武器能力的完整中英对照。</p>
    <table class="aspect-data-table">
      <tr><th>宝典 <span class="en-cell">Codex</span></th><th>类型 <span class="en-cell">Type</span></th><th>使用要求 <span class="en-cell">Requirement</span></th><th>简介 <span class="en-cell">Overview</span></th><th>详情</th></tr>
@@LIST@@
    </table>
  </div>
  <p class="backlink"><a href="../index.html">← 返回资料库首页</a></p>
</div>
<footer>
  <div><b>资料来源：</b>译自官方 Wiki <a href="@@SRC@@" target="_blank" rel="noopener">wiki.uooutlands.com/Weapon_and_Parry_Codex</a>，非官方整理，仅供学习交流；数值以官方 Discord 补丁公告为准。</div>
  <div>UO Outlands 中文资料库 · 本地预览版 · 2026-08-08</div>
</footer>
@@BGM@@
</body>
</html>'''.replace("@@NAV@@", NAV).replace("@@SRC@@", SRC).replace("@@XP@@", xp_rows).replace("@@LIST@@", list_rows).replace("@@BGM@@", BGM)

with open(os.path.join(CODEX_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
print("generated codex/index.html")
print("all codex files done")

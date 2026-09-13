# -*- coding: utf-8 -*-
"""
生成 UO Outlands 中文资料库 —— 精通链 Mastery Chain 页面。
数据源：
  https://wiki.uooutlands.com/Mastery_Chain
  Template:MasteryChainLinks  (链环奖励值大表)
  Template:MasteryChainXP     (XP 需求表)
图片：web/data/images/mastery/ (19 张，已下载)
重跑：python web/mastery/gen_mastery.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = '../data/images/mastery'
CSSV = '20260904_1'

# ---------------- 链环奖励值大表（7 列） ----------------
# (英文, 中文, Bronze, Silver, Gold, Corrupted, Elective, Multi)
GROUPS = [
 ("Barding Type Links", "吟游类链环", [
  ("Bard Reset/Break Ignore Chance", "吟游重置/打断无视几率", "2.50%", "~3.13%", "3.75%", "4.06%", "", ""),
  ("Barding Effect Durations", "吟游效果持续时间", "3.00%", "3.75%", "4.50%", "~4.88%", "吟游重置/打断无视几率", ""),
  ("Damage to Barded Creatures", "对被吟游生物伤害", "1.75%", "~2.19%", "~2.63%", "~2.84%", "", "乘算"),
  ("Effective Barding Skill", "有效吟游技能", "3.00", "3.75", "4.50", "~4.88", "吟游重置/打断无视几率", ""),
 ]),
 ("Boating Type Links", "航海类链环", [
  ("Damage on Ships", "对船只伤害", "3.00%", "3.75%", "4.50%", "~4.88%", "", "乘算"),
  ("Damage Resistance on Ships", "船只伤害抗性", "3.00%", "3.75%", "4.50%", "~4.88%", "伤害抗性", ""),
  ("Ship Cannon Damage**", "船炮伤害", "1.50%", "~1.88%", "2.25%", "~2.44%", "加算?", ""),
  ("Crewmember Damage***", "船员伤害", "1.50%", "~1.88%", "2.25%", "~2.44%", "加算?", ""),
  ("Crewmember Damage Resistance***", "船员伤害抗性", "1.50%", "~1.88%", "2.25%", "~2.44%", "", ""),
 ]),
 ("Follower Type Links", "随从类链环", [
  ("Follower Accuracy/Defense***", "随从命中/防御", "1.50%", "~1.88%", "2.25%", "~2.44%", "", ""),
  ("Follower Attack Speed", "随从攻击速度", "1.00%", "1.25%", "1.50%", "~1.63%", "", ""),
  ("Follower Damage", "随从伤害", "2.00%", "2.50%", "3.00%", "3.25%", "随从攻击速度", "加算"),
  ("Follower Damage Resistance", "随从伤害抗性", "2.00%", "2.50%", "3.00%", "3.25%", "炼金/治疗/兽医<br>随从攻击速度", ""),
  ("Follower Healing Received", "随从受到的治疗", "3.00%", "3.75%", "4.50%", "~4.88%", "炼金/治疗/兽医、随从攻击速度", ""),
 ]),
 ("Melee Type Links", "近战类链环", [
  ("Melee Aspect Effect Chance****", "近战元素特效几率", "4.50%", "~5.63%", "6.75%", "~7.31%", "", ""),
  ("Melee Aspect Effect Modifier", "近战元素特效倍率", "5.00%", "6.25%", "7.50%", "~8.13%", "", ""),
  ("Melee Accuracy", "近战命中", "1.75%", "~2.19%", "~2.62%", "~2.84%", "近战命中/防御", ""),
  ("Melee Defense", "近战防御", "2.50%", "~3.13%", "3.75%", "4.06%", "近战命中/防御", ""),
  ("Melee Accuracy/Defense", "近战命中/防御", "1.50%", "~1.88%", "2.25%", "~2.44%", "", ""),
  ("Melee Special Chance**", "近战特殊几率", "2.00%", "2.50%", "3.00%", "3.25%", "近战特殊几率/特殊伤害", ""),
  ("Melee Special Chance/Special Damage**", "近战特殊几率/特殊伤害", "1.75%", "~2.19%", "~2.63%", "~2.88%", "", "加算"),
  ("Melee Damage**", "近战伤害", "3.00%", "3.75%", "4.50%", "~4.88%", "近战伤害/无视护甲几率", "加算"),
  ("Melee Ignore Armor Chance", "近战无视护甲几率", "4.00%", "5.00%", "6.00%", "6.50%", "近战伤害/无视护甲几率", ""),
  ("Melee Damage/Ignore Armor Chance**", "近战伤害/无视护甲几率", "2.50%", "~3.13%", "3.75%", "~4.06%", "", "加算"),
  ("Melee Swing Speed****", "近战挥击速度", "0.80%", "1.00%", "1.20%", "1.30%", "", ""),
 ]),
 ("Spell Type Links", "法术类链环", [
  ("Meditation Rate", "冥想速率", "2.00%", "2.50%", "3.00%", "3.25%", "冥想速率/打断回避几率", ""),
  ("Spell Disrupt Avoid Chance", "法术打断回避几率", "6.00%", "7.50%", "9.00%", "9.75%", "冥想速率/打断回避几率<br>无随从时法术伤害", ""),
  ("Meditation Rate/Disrupt Avoid Chance", "冥想速率/打断回避几率", "2.00%", "2.50%", "3.00%", "3.25%", "无随从时法术伤害", ""),
  ("Spell Aspect Effect Modifier", "法术元素特效倍率", "5.00%", "6.25%", "7.50%", "~8.13%", "", ""),
  ("Spell Aspect Special Chance****", "法术元素特殊几率", "4.50%", "~5.63%", "6.75%", "~7.31%", "", ""),
  ("Spell Charged Chance**", "法术充能几率", "4.00%", "5.00%", "6.00%", "6.50%", "法术充能几率/充能伤害", ""),
  ("Spell Charged Damage**", "法术充能伤害", "6.00%", "7.50%", "9.00%", "9.75%", "法术充能几率/充能伤害", "加算"),
  ("Spell Charged Chance/Charged Damage**", "法术充能几率/充能伤害", "3.50%", "~4.38%", "5.25%", "~5.69%", "", "加算"),
  ("Spell Damage**", "法术伤害", "3.00%", "3.75%", "4.50%", "~4.88%", "法术伤害/无视抗性几率", "加算"),
  ("Spell Ignore Resist Chance", "法术无视抗性几率", "4.00%", "5.00%", "6.00%", "6.50%", "法术伤害/无视抗性几率", ""),
  ("Spell Damage/Ignore Resist Chance**", "法术伤害/无视抗性几率", "2.50%", "~3.13%", "3.75%", "~4.06%", "", "加算"),
  ("Spell Damage When No Followers**", "无随从时法术伤害", "4.00%", "5.00%", "6.00%", "6.50%", "", "加算"),
 ]),
 ("Damage Type Links", "伤害类链环", [
  ("Backstab Damage****", "背刺伤害", "4.50%", "~5.63%", "6.75%", "~7.31%", "乘算?", ""),
  ("Damage to Diseased Creatures****", "对患病生物伤害", "1.75%", "2.1875%", "2.625%", "2.84375%", "", "乘算"),
  ("Damage to Bleeding Creatures", "对流血生物伤害", "1.75%", "2.1875%", "2.625%", "2.84375%", "", "乘算"),
  ("Damage to Bosses", "对 BOSS 伤害", "3.00%", "3.75%", "4.50%", "~4.88%", "", "乘算"),
  ("Damage to Creatures Above 66% HP****", "对 66% 以上血量生物伤害", "2.00%", "2.50%", "3.00%", "3.25%", "玩家造成的伤害", "乘算"),
  ("Damage to Creatures Below 33% HP", "对 33% 以下血量生物伤害", "2.50%", "~3.13%", "3.75%", "4.06%", "玩家造成的伤害", "乘算"),
  ("Damage Dealt By Player", "玩家造成的伤害", "1.50%", "~1.88%", "2.25%", "~2.44%", "可升级为任意其他类型链环", "乘算"),
  ("Trap Damage**", "陷阱伤害", "4.00%", "5.00%", "6.00%", "6.50%", "", "加算"),
 ]),
 ("Poison Type Links", "剧毒类链环", [
  ("Damage to Poisoned Creatures****", "对中毒生物伤害", "1.75%", "~2.19%", "~2.63%", "~2.84%", "", "乘算"),
  ("Effective Poisoning Skill", "有效毒药技能", "3.00", "3.75", "4.50", "~4.88", "毒伤害/无视抗性、对患病生物伤害", ""),
  ("Poison Damage**", "毒伤害", "7.00%", "8.75%", "10.50%", "11.375%", "毒伤害/无视毒抗", "乘算?"),
  ("Poison Damage/Resist Ignore****", "毒伤害/无视毒抗", "4.50%", "5.625%", "6.75%", "7.3125%", "对患病生物伤害", "乘算?"),
 ]),
 ("Resistance Type Links", "抗性类链环", [
  ("Boss Damage Resistance", "BOSS 伤害抗性", "2.00%", "2.50%", "3.00%", "3.25%", "伤害抗性", ""),
  ("Damage Resistance", "伤害抗性", "1.00%", "1.25%", "1.50%", "~1.63%", "", ""),
  ("Physical Damage Resistance", "物理伤害抗性", "1.50%", "~1.88%", "2.25%", "~2.44%", "伤害抗性", ""),
  ("Spell Damage Resistance", "法术伤害抗性", "1.50%", "~1.88%", "2.25%", "~2.44%", "伤害抗性", ""),
 ]),
 ("Effective Skill Links", "有效技能类链环", [
  ("Effective Alchemy Skill", "有效炼金技能", "3.00", "3.75", "4.50", "~4.88", "炼金/治疗/兽医", ""),
  ("Alchemy/Healing/Veterinary", "炼金/治疗/兽医", "3.00", "3.75", "4.50", "~4.88", "随从攻击速度", ""),
  ("Effective Arms Lore***", "有效武器学", "3.00", "3.75", "4.50", "~4.88", "", ""),
  ("Effective Camping Skill***", "有效露营技能", "3.00", "3.75", "4.50", "~4.88", "", ""),
  ("Chivalry Skill", "骑士精神技能", "2.50", "~3.13", "3.75", "4.06", "", ""),
  ("Effective Harvest Skill***", "有效采集技能", "1.00", "1.25", "1.50", "~1.63", "", ""),
  ("Effective Magic Resist Skill", "有效魔法抗性技能", "3.00", "3.75", "4.50", "~4.88", "伤害抗性", ""),
  ("Necromancy Skill", "死灵法术技能", "2.50", "~3.13", "3.75", "4.06", "随从伤害<br>随从伤害抗性", ""),
  ("Effective Parrying Skill", "有效格挡技能", "3.00", "3.75", "4.50", "~4.88", "伤害抗性", ""),
  ("Effective Skill on Chests", "对箱子的有效技能", "3.00", "3.75", "4.50", "~4.88", "箱子成功率/进度", ""),
  ("Spirit Speak/Inscription", "通灵/铭文", "2.50", "~3.13", "3.75", "4.06", "随从伤害<br>随从伤害抗性", ""),
 ]),
 ("Other Links", "其他链环", [
  ("Chance on Stealth for 5 Extra Steps", "潜行时 5 额外步数几率", "5.00%", "6.25%", "7.50%", "~8.13%", "", "加算"),
  ("Chest Success Chances/Progress", "箱子成功率/进度", "3.00%", "3.75%", "4.50%", "~4.88%", "", ""),
  ("Exceptional Quality Chance***", "卓越品质几率", "1.50%", "~1.88%", "2.25%", "~2.44%", "", "乘算"),
  ("Gold/Doubloon Drop Increase", "金币/达布隆掉落增加", "1.00%", "1.50%", "2.00%", "2.25%", "", ""),
  ("Healing Received", "受到的治疗", "3.00%", "3.75%", "4.50%", "~4.88%", "炼金/治疗/兽医", ""),
  ("Special Loot Chance*", "特殊战利品几率", "1.00%", "1.50%", "2.00%", "2.25%", "特殊/稀有战利品几率", ""),
  ("Rare Loot Chance*", "稀有战利品几率", "1.00%", "1.50%", "2.00%", "2.25%", "特殊/稀有战利品几率", ""),
  ("Special/Rare Loot Chance", "特殊/稀有战利品几率", "1.00%", "1.50%", "2.00%", "2.25%", "特殊/稀有战利品几率", ""),
  ("Summon Duration and Dispel Resist*", "召唤持续时间与驱散抗性", "3.00%", "3.75%", "4.5%", "4.88%", "通灵/铭文", ""),
 ]),
]

# ---------------- XP 需求表（30 级） ----------------
XP_ROWS = [(i, f"{250000 + (i-1)*250000:,}", f"{(250000 + (250000 + (i-1)*250000)) * i // 2:,}") for i in range(1, 31)]

NAV = '''<nav class="site-nav">
  <span class="nav-brand">UO Outlands 中文资料库</span>
  <a href="../index.html">首页</a>
  <a href="../patch/index.html">版本更新</a>
  <a href="../skills/index.html">技能详解</a>
  <a href="../elements/index.html">元素精通</a>
  <a href="../mastery/index.html">精通链</a>
  <div class="nav-dropdown">
    <a href="../codex/index.html">宝典图鉴</a>
    <div class="nav-menu">
      <a href="../codex/arcane.html">奥术 <span class="en">Arcane</span></a>
      <a href="../codex/archery.html">弓箭 <span class="en">Archery</span></a>
      <a href="../codex/dual-wielding.html">双持 <span class="en">Dual Wielding</span></a>
      <a href="../codex/fencing.html">细剑 <span class="en">Fencing</span></a>
      <a href="../codex/fishing.html">钓鱼 <span class="en">Fishing</span></a>
      <a href="../codex/macing.html">锤类 <span class="en">Macing</span></a>
      <a href="../codex/swords.html">剑术 <span class="en">Swords</span></a>
      <a href="../codex/throwing.html">投掷 <span class="en">Throwing</span></a>
      <a href="../codex/wrestling.html">徒手 <span class="en">Wrestling</span></a>
      <a href="../codex/parrying.html">格挡 <span class="en">Parrying</span></a>
      <a href="../codex/trap.html">陷阱 <span class="en">Trap</span></a>
      <a href="../codex/healers_codex.html">治疗 <span class="en">Healers</span></a>
      <a href="../codex/bard_codex.html">音乐 <span class="en">Bard</span></a>
    </div>
  </div>
  <div class="nav-dropdown">
    <a href="../pets/index.html">宠物图鉴</a>
    <div class="nav-menu">
      <a href="../pets/index.html">可驯服宠物</a>
      <a href="../pets/follower-abilities.html">宠物技能大全</a>
      <a href="../pets/team-builder.html">智能配宠向导</a>
    </div>
  </div>
  <div class="nav-dropdown">
    <a href="../ships.html">船舰系统</a>
    <div class="nav-menu">
      <a href="../ships.html">船舰系统总页</a>
      <a href="../ships-newbie.html">新手第一条船</a>
    </div>
  </div>
</nav>'''


def img(name, cls='mc-img'):
    return f'<img class="{cls}" src="{IMG}/{name}" alt="{name}" loading="lazy">'


def render_links_table():
    out = ['<table class="wikitable mc-links"><thead><tr>',
           '<th>奖励类型<br><span class="en">Bonus Type</span></th>',
           '<th class="th-bronze">青铜<br><span class="en">Bronze</span></th>',
           '<th class="th-silver">白银<br><span class="en">Silver</span></th>',
           '<th class="th-gold">黄金<br><span class="en">Gold</span></th>',
           '<th class="th-corrupt">腐化<br><span class="en">Corrupted</span></th>',
           '<th>可选升级<br><span class="en">Elective Upgrades</span></th>',
           '<th>叠加方式<br><span class="en">Multi Type</span></th>',
           '</tr></thead><tbody>']
    for gen, gcn, rows in GROUPS:
        out.append(f'<tr class="mc-group"><td colspan="7">{gcn} <span class="en">{gen}</span></td></tr>')
        for en, cn, b, s, g, c, ele, mul in rows:
            mul_cls = ''
            if mul.startswith('乘算'):
                mul_cls = ' class="mul-multi"'
            elif mul.startswith('加算'):
                mul_cls = ' class="mul-add"'
            if '?' in mul:
                mul_html = f'<span class="q-mark">{mul}</span>'
            else:
                mul_html = mul
            out.append(
                f'<tr><td class="bonus-name">{cn}<br><span class="en-cell">{en}</span></td>'
                f'<td class="c-bronze">{b}</td>'
                f'<td class="c-silver">{s}</td>'
                f'<td class="c-gold">{g}</td>'
                f'<td class="c-corrupt">{c}</td>'
                f'<td class="elec">{ele}</td>'
                f'<td{mul_cls}>{mul_html}</td></tr>')
    out.append('</tbody></table>')
    return '\n'.join(out)


def render_xp_table():
    out = ['<table class="wikitable mc-xp"><thead><tr><th>链环序号</th><th>本级所需 XP</th><th>累计 XP</th></tr></thead><tbody>']
    for i, xp, cum in XP_ROWS:
        out.append(f'<tr><td>{i}</td><td>{xp}</td><td>{cum}</td></tr>')
    out.append('</tbody></table>')
    return '\n'.join(out)


def build():
    styles = img('masterychainexquisite2.png') + '**精致**'
    style_rows = [
        ('masterychainexquisite2.png', '精致', 'Exquisite'),
        ('masterychainfashionable2.png', '时尚', 'Fashionable'),
        ('masterychaingilded2.png', '鎏金', 'Gilded'),
        ('masterychaintwinloop2.png', '双环', 'Twin Loop'),
        ('briolettechain.png', '梨形珠', 'Briolette'),
        ('cabochonchain.png', '蛋面', 'Cabochon'),
        ('chandelierchain.png', '枝形吊灯', 'Chandelier'),
        ('graduatedbeadchain.png', '渐变珠', 'Graduated Bead'),
        ('hornpendantchain.png', '角坠', 'Horn Pendant'),
        ('layeredchain.png', '层叠', 'Layered'),
        ('twistedcablechain.png', '绞索', 'Twisted Cable'),
    ]
    style_tbl = ['<table class="wikitable mc-style"><tbody>']
    for i in range(0, len(style_rows), 2):
        style_tbl.append('<tr>')
        for f, cn, en in style_rows[i:i+2]:
            style_tbl.append(f'<td>{img(f)}<br><b>{cn}</b><br><span class="en-cell">{en}</span></td>')
        if len(style_rows[i:i+2]) == 1:
            style_tbl.append('<td></td>')
        style_tbl.append('</tr>')
    style_tbl.append('</tbody></table>')
    style_tbl = '\n'.join(style_tbl)

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>精通链 Mastery Chain | UO Outlands 中文资料库</title>
<link rel="stylesheet" href="style.css?v={CSSV}">
  <link rel="stylesheet" href="../assets/theme.css">
  <script src="../assets/theme.js"></script>
</head>
<body class="side-nav-page">
{NAV}
<nav class="breadcrumb"><a href="../index.html">资料库首页</a> › <span>精通链 Mastery Chain</span></nav>
<div class="source-link">官方原文：<a href="https://wiki.uooutlands.com/Mastery_Chain" target="_blank" rel="noopener">wiki.uooutlands.com/Mastery_Chain</a></div>
<div class="mw-body">
  <h1 class="mw-page-title-main">精通链 <span class="cnsub">Mastery Chain</span></h1>
  <div class="toc"><div class="toctitle">目录</div><ol>
    <li><a href="#summary">系统总览 / Summary</a></li>
    <li><a href="#appearance">链的外观 / Appearance</a></li>
    <li><a href="#using">使用精通链 / Using</a></li>
    <li><a href="#liftlock">防抬锁 / Liftlock</a></li>
    <li><a href="#acquire">获取链环 / Acquiring</a></li>
    <li><a href="#exp">获得经验 / Experience</a></li>
    <li><a href="#upgrade">升级精通链 / Upgrading</a></li>
    <li><a href="#linktypes">链环类型 / Link Types</a></li>
    <li><a href="#values">链环奖励数值 / Bonus Values</a></li>
    <li><a href="#pvp">PvP 限制 / Restrictions</a></li>
    <li><a href="#install">安装链环 / Installing</a></li>
    <li><a href="#remove">移除链环 / Removing</a></li>
    <li><a href="#reforge">重铸工具 / Reforging</a></li>
    <li><a href="#tome">链环宝典 / Link Tome</a></li>
    <li><a href="#xptable">XP 需求表 / XP Table</a></li>
  </ol></div>
  <div class="mw-content">

    <h2 id="summary">系统总览 <span class="en-h">Summary</span></h2>
    <ul>
      <li>精通链（Mastery Chain）系统是<strong>终局 PvM 系统</strong>，为玩家提供众多进一步强化角色的选项。</li>
      <li>精通链是<strong>祝福（Blessed）</strong>的可穿戴物品，占用角色的<strong>护身符（Talisman）</strong>栏位。</li>
      <li>精通链必须<strong>双击绑定</strong>到角色后才能使用。
        <ul><li>绑定后，双击或佩戴即可激活。一条链会一直保持激活，直到你激活另一条。</li></ul></li>
      <li>玩家可用 <strong>120 修补（Tinkering）</strong>制作精通链；获得解锁链环槽所需的 XP 后，可为链添加链环，提供 PvM 加成。</li>
      <li>没有精通链也能开始累积 XP，但<strong>必须有链才能看到已累积的 XP</strong>。</li>
      <li>可用 <code>[MasteryChain</code> 命令、双击精通链，或通过角色右键菜单中的「Mastery Chain」选项查看精通链面板。</li>
      <li>精通链 XP 在<strong>同一账号的所有角色间共享</strong>，但每个角色必须各有自己的精通链才能获得收益。</li>
      <li>与元素类似，玩家最多<strong>每 30 秒</strong>只能更换一次精通链（不会阻止你装备，但新装备的精通链加成在 30 秒内不生效）。</li>
    </ul>

    <h2 id="appearance">链的外观 <span class="en-h">Chain Appearance</span></h2>
    <p>视觉效果<strong>不影响机制</strong>，只影响外观。共有 11 种可制作外观：</p>
    {style_tbl}
    <h3>精通链重铸外观契约 <span class="en-h">Restyle Deeds</span></h3>
    <p>精通链可用（通常为限时的）重铸契约改成独特变体：</p>
    <table class="wikitable mc-style"><tbody><tr>
      <td>{img('toothchain.png')}<br><b>牙饰项链</b><br><span class="en-cell">Tooth Necklace</span></td>
      <td></td>
    </tr></tbody></table>

    <h2 id="using">使用精通链 <span class="en-h">Using Mastery Chains</span></h2>
    <ul>
      <li>精通链必须<strong>永久绑定</strong>到该玩家，才能从中获得加成。</li>
      <li>玩家可以同时绑定<strong>多条</strong>精通链到自己身上。</li>
      <li>玩家可以选择把链放在背包里而不佩戴（因为它会占用护身符栏位），但<strong>必须至少装备一次</strong>，才能把该链设为「当前激活」以获取其加成。</li>
      <li>单击已绑定的精通链，会显示它绑定到的角色。</li>
      <li>单击精通链可查看切换当前链后，加成的激活倒计时。</li>
      <li>可随时自由装备精通链（不会受阻），但新装备的链加成 30 秒后才生效。</li>
      <li>只能从<strong>自己拥有的</strong>精通链上移除链环（链绑定其拥有者）。</li>
    </ul>
    <p class="mc-fig">{img('masterychaingumpaddalllinks.gif')}</p>
    <ul>
      <li>精通链菜单有「<strong>安装背包中全部链环</strong>」按钮，点击可搜索背包并一次性安装所有有效链环。</li>
      <li>此方式安装遵循普通安装规则（重复效果上限、腐化链环限制、每环奥术精华消耗等）。</li>
      <li>系统会提示找到并成功安装了多少个链环。</li>
      <li>若因<strong>奥术精华不足</strong>而无法安装，会收到提示。</li>
      <li>若触发重复效果限制，则不会有专门提示：只会告知成功安装了几个（即未安装的都因某种限制被拦下）。</li>
    </ul>

    <h2 id="liftlock">防抬锁 <span class="en-h">Liftlock</span></h2>
    <ul>
      <li>精通链新增「防抬锁（Liftlock）」机制，可切换以防止在背包或已装备状态下被「抬起（Lift）」。</li>
      <li>按住 Shift 单击精通链（背包中或已装备），选择「Enable Liftlock」启用，或「Disable Liftlock」禁用。</li>
    </ul>
    <p class="mc-fig">{img('masterychain-liftlock1.jpg')}</p>
    <ul><li>启用后，若玩家试图从背包或人物栏抬起该物品，会被阻止并收到系统提示。</li></ul>
    <p class="mc-fig">{img('masterychain-liftlock2.jpg')}</p>

    <h2 id="acquire">获取精通链环 <span class="en-h">Acquiring Mastery Chain Links</span></h2>
    <p class="mc-fig">{img('howdoigetmasterychains.png')}</p>
    <ul>
      <li>完成一本<a href="../skills/index.html">学识之书（Lore Book）</a></li>
      <li>完成《英雄典籍》（Tome of Heroism）</li>
      <li>击杀全能 BOSS（Omni Boss）</li>
      <li>完成深渊试炼（Pit Trials）</li>
      <li>也可用以下系统的奖励点数购买链环：
        <ul><li>竞技场（Arenas）</li><li>阵营（Factions）</li><li>成就（Achievements）</li><li>公会（Societies）</li><li>奇境（Strangelands）</li></ul></li>
    </ul>

    <h2 id="exp">获得经验 <span class="en-h">Gaining Experience</span></h2>
    <h3>经验公式（说明） <span class="en-h">Experience Formula</span></h3>
    <ul>
      <li>击杀生物时，每位玩家的经验通常按「<strong>对生物造成的伤害百分比 × 该生物的金币价值</strong>」计算。</li>
      <li>例如：一只价值 1000 金币的生物，某玩家造成 33% 伤害，则获得 <strong>333</strong> 点经验（计入精通链、武器宝典、巫师法典等系统）。</li>
      <li>多名队员共同伤害同一生物时，会获得<strong>组队经验倍率</strong>。</li>
      <li>完整的经验获取说明见官方 <a href="https://wiki.uooutlands.com/Experience_Gain" target="_blank" rel="noopener">Experience Gain</a>。</li>
    </ul>

    <h2 id="upgrade">升级精通链 <span class="en-h">Upgrading Mastery Chains</span></h2>
    <ul>
      <li>精通链本身在添加链环前<strong>不提供任何收益</strong>。</li>
      <li>每条精通链最多可添加 <strong>30 个链环</strong>，但必须先用 XP <strong>解锁链环槽</strong>。</li>
      <li>通过能获得金币的行为积累 XP（击杀怪物、开启地牢宝箱等）。</li>
      <li>XP 足够解锁新链环槽时，会收到提示。</li>
      <li>若链上有可用的已解锁槽位，链的图形中会显示一个或多个<strong>绿色</strong>链环。</li>
      <li>安装一个新链环需消耗 <strong>10 个奥术精华（Arcane Essence）</strong>。</li>
    </ul>

    <h2 id="linktypes">精通链环类型 <span class="en-h">Mastery Chain Link Types</span></h2>
    <ul>
      <li>链环是极为稀有的战利品，仅通过少数特定机制获得（如全能 BOSS、寻宝），或用某些系统的大量奖励点数购买（如公会）。</li>
      <li>链环有 <strong>4 种材质</strong>：青铜（Bronze）、白银（Silver）、黄金（Gold）、腐化（Corrupted）。
        <ul><li>腐化链环的完整说明、限制与衰减计时，见官方 <a href="https://wiki.uooutlands.com/Corrupted_Mastery_Chain_Links" target="_blank" rel="noopener">Corrupted Mastery Chain Links</a>。</li></ul></li>
      <li>每个链环提供特定效果或加成，加成数值随材质提升：
        <ul>
          <li><strong>白银</strong>比青铜更稀有，加成通常比青铜高 <strong>25%</strong>。</li>
          <li><strong>黄金</strong>极为稀有，加成通常比青铜高 <strong>50%</strong>。</li>
        </ul></li>
    </ul>
    <h3>链环奖励数值 <span class="en-h">Mastery Chain Link Bonus Values</span></h3>
    <p>各链环的当前数值如下：</p>
    <ul class="mc-note">
      <li>链环的「有效技能」加成<strong>只提升战斗中由该技能带来的收益</strong>，<strong>不</strong>提升制作时的技能值。</li>
      <li>「可选升级（Elective Upgrades）」表示可通过双击把左列链环转换为该列所示链环；<strong>不可逆</strong>（除非使用重铸工具）。</li>
      <li>表格底部星号说明：<em>* 该链环已不再掉落；** 荒野资料片（Wildlands）变更；*** 荒野资料片新增；**** 第一阶段平衡性调整变更。</em></li>
    </ul>
    <div class="mc-table-wrap">
    {render_links_table()}
    </div>

    <h2 id="pvp">PvP 限制 <span class="en-h">PvP Restrictions</span></h2>
    <ul>
      <li>默认情况下，<strong>仅</strong>影响怪物的 PvM 加成在玩家处于 PvP 标记状态时<strong>依然生效</strong>。例如：伤害抗性、防御。</li>
      <li>凡本质上有可能影响 PvP 的效果，在 PvP 标记时<strong>一律禁用</strong>。例如：法力回复/恢复、法力返还、生命回复/恢复、给予/受到的治疗、有效技能。</li>
      <li>在竞技场、冥河裂隙（Stygian Rifts），或 Stalag Grotto Battle 等特殊 PvP 事件中，PvM 加成始终禁用。</li>
    </ul>
    <h3>其他限制 <span class="en-h">Other Restrictions</span></h3>
    <ul><li>「对中毒生物伤害」链环仅在目标带有<strong>高等毒或以上</strong>时生效。</li></ul>

    <h2 id="install">安装链环 <span class="en-h">Installing Mastery Chain Links</span></h2>
    <ul>
      <li>若链上有可用的已解锁槽位（链图形顶部显示为绿色），可在精通链面板点击「Install Link」，再指定背包中的链环安装。</li>
      <li>同一种加成效果的链环，每条链最多安装 <strong>10 个</strong>（红线升级后可提高到 <strong>15 个</strong>），各效果累计加成会显示在面板中。</li>
      <li>唯一例外是「特殊/稀有掉落几率」，可装 <strong>20 个</strong>。</li>
      <li>点击窗口右下角的「Remove Links」按钮可移除链环。</li>
    </ul>

    <h2 id="remove">移除链环 <span class="en-h">Removing Mastery Chain Links</span></h2>
    <ul>
      <li>移除时可用左右箭头浏览已安装的链环，选中的链环以<strong>绿色指针</strong>标记，其加成显示在底部面板。</li>
      <li>点击红色「Remove Link」按钮会移除高亮链环并放回背包。</li>
      <li>移除链环<strong>不会退还</strong> 10 个奥术精华，但可在原位装回新链环。</li>
      <li>完成后点击右下角「Done」返回主界面。</li>
      <li>可点击「Remove Row」移除当前选中行的全部链环（需<strong>双击</strong>确认）。</li>
      <li>可点击「Remove All」移除全部已安装链环（需<strong>三重</strong>确认）。</li>
    </ul>
    <p class="mc-fig">{img('masterychainlinkremoval.png')}</p>

    <h2 id="reforge">链环重铸工具 <span class="en-h">Reforging Tools</span></h2>
    <ul>
      <li>有青铜、白银、黄金、腐化四种重铸工具，须使用与目标链环<strong>相同材质</strong>的工具（即青铜工具用于青铜链环）。</li>
      <li>双击背包中的重铸工具，然后指定要修改的链环。</li>
      <li>在弹出菜单中，用左右箭头在可选的奖励效果间切换。</li>
      <li>选定后点击「Reforge Link」更换链环加成（会消耗该工具）。</li>
      <li>可用竞技场、成就、阵营、公会奖励系统的奖励点数购买重铸工具。</li>
      <li>也可在普雷瓦利亚市场（Prevalia Market）用金币购买。</li>
      <li>重铸工具会同时显示多种奖励类型，并按奖励类型<strong>字母顺序</strong>排列。</li>
      <li>使用新工具时，会记住上一把工具所选的奖励类型与页码，便于连续重铸多个链环。</li>
    </ul>
    <p class="mc-fig">{img('linkreforgeagain.png')}</p>

    <h2 id="tome">链环宝典 <span class="en-h">Mastery Chain Link Tome</span></h2>
    <p>玩家可在普雷瓦利亚市场商人处购买<strong>链环宝典</strong>，用于存放获得的各类链环。</p>
    <p class="mc-fig">{img('masterychainlinktome.png')}</p>

    <h2 id="xptable">XP 需求表 <span class="en-h">Mastery Chain XP Table</span></h2>
    <p>解锁每一个链环槽所需的 XP：</p>
    <div class="mc-table-wrap">
    {render_xp_table()}
    </div>

  </div>
  <p class="backlink"><a href="../index.html">← 返回资料库首页</a></p>
</div>
<footer>
  <p>UO Outlands 中文资料库 · 非官方粉丝翻译，内容版权归 Outlands 官方所有。</p>
</footer>
</body>
</html>
'''
    out = os.path.join(HERE, 'index.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('已生成:', out, len(html), '字符')


if __name__ == '__main__':
    build()

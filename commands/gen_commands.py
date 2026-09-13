# -*- coding: utf-8 -*-
"""
生成「命令大全 Commands」页面。
数据源：官方 wiki.uooutlands.com/Commands（wikitext，323 条 Outlands 命令）
      + Template:ClassicUOCommands（9 条客户端命令）
重跑即重生成 web/commands/index.html，官方更新后直接再跑一次即可。
"""
import os
import html

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = '../data/images/commands'
CSSV = '20260913_1'

# ---------------- ClassicUO 客户端命令 ----------------
CLASSICUO = [
    ('-info', '对准物品可查看其属性'),
    ('-datetime', '显示服务器日期与时间'),
    ('-hue', '对准物品可查看其色号（以系统消息显示）'),
    ('-debug', '在游戏世界的图形周围绘制边框'),
    ('-toggle &lt;选项名&gt;', '通过命令切换 Classic UO 客户端的各项选项'),
    ('-ignore', '对准某玩家，将其加入客户端忽略名单'),
    ('-savenecrobar', '保存死灵能力栏（Gump）的当前位置'),
    ('-savechivbar', '保存骑士能力栏（Gump）的当前位置'),
    ('-savecodexbar（已失效）', '保存宝典能力栏（Gump）的当前位置（可能已失效）'),
]

# ---------------- UO Outlands 命令（11 类，323 条） ----------------
def _rep(tpl, desc_tpl, n):
    """批量展开带序号的命令（如 Stance1~Stance5），保证「大全」可逐条检索。"""
    return [(tpl.format(i=i), desc_tpl.format(i=i)) for i in range(1, n + 1)]


SECTIONS = [
    ('Menus', '菜单', 'Menus', 'commandsmenu.png', [
        ('[Help', '打开 Outlands 帮助页面'),
        ('[Website', '启动 Outlands 官方网站'),
        ('[Wiki', '启动 Outlands Wiki'),
        ('[Forums 或 [Forum', '启动 Outlands 论坛'),
        ('[Discord', '启动 Outlands Discord 频道'),
        ('[HelpRequest 或 [Request', '打开求助页面'),
        ('[Achievements 或 [Achievement', '打开成就页面'),
        ('[Societies 或 [Society', '打开协会页面'),
        ('[AspectMastery 或 [Aspects 或 [Aspect', '打开元素精通（Aspect Mastery）页面'),
        ('[SkillMastery', '打开技能精通页面'),
        ('[Customizations 或 [Customization', '打开自定义外观页面'),
        ('[Titles 或 [Title', '打开称号页面'),
        ('[TownStruggle 或 [TownStruggles', '打开城镇争夺页面'),
        ('[Criminality 或 [ConsiderSins', '打开犯罪状态页面'),
        ('[PlayerStats 或 [Stats', '打开角色属性页面'),
        ('[DamageTracker 或 [Damage', '开启伤害统计工具'),
        ('[Atlas', '给予玩家一份地图册（双击使用）'),
        ('[ServerRankings 或 [ServerRank', '打开服务器排行榜页面'),
        ('[Commands 或 [Command', '打开命令页面'),
        ('[Donate 或 [Donation', '启动 Outlands 捐赠页面'),
        ('[Party', '打开队伍菜单'),
        ('[Survey 或 [HouseSurvey', '启动房屋封锁 / 保全普查机制'),
        ('[Vendor 或 [Vendors', '打开商人菜单'),
        ('[VendorSearch', '打开商人搜索网站'),
    ]),
    ('Mechanics', '机制', 'Mechanics', 'commandsmechanics.png', [
        ('[AutoUseSpellScrolls', '切换施法时是否自动使用背包中的法术卷轴'),
        ('[AutoStealth', '切换在隐藏状态下尝试移动时，是否自动启动潜行'),
        ('[UnequipOnCast', '切换施法或主动冥想时是否自动卸下装备；若玩家的格挡与魔法技能足以持盾施法，则不会卸下盾牌'),
        ('[Pouch', '在背包中随机搜寻一个陷阱袋并触发它'),
        ('[Taunt', '手持双手武器或盾牌时启动嘲讽指令'),
        ('[Rope', '在背包中随机搜寻一根绳子并触发它'),
        ('[VetSupplies 或 [VeterinarySupplies', '在背包中随机搜寻一份兽医用品并使用'),
        ('[SmokeBomb', '在背包中搜寻烟雾弹并触发它'),
        ('[Disarm', '切换玩家是否尝试施展卸武（Disarm）攻击'),
        ('[DisarmUntoggleMode', '更改卸武自动取消切换的触发方式'),
        ('[Hamstring', '切换玩家是否尝试施展断筋（Hamstring）攻击'),
        ('[HamstringUntoggleMode', '更改断筋自动取消切换的触发方式'),
        ('[SpellFizzle', '更改是否显示法术施放失败的音效与动画'),
        ('[Echo 或 [Echoes', '打开回响（Echoes）菜单'),
        ('[BossResults', '打开 BOSS 战果菜单'),
        ('[MasteryChain', '双击你当前使用的精通链'),
        ('[Artisan', '切换穿着工匠元素装备制作时是否获得工匠元素经验（消耗奥术精华）'),
        ('[Fortune', '切换穿着幸运元素装备开锁时是否获得幸运元素经验（消耗奥术精华）'),
        ('[Coord 或 [Coords 或 [Coordinates', '显示玩家当前 X、Y、Z 坐标与经纬度'),
        ('[PullFollowers', '将 5 格范围内所有随从拉到玩家所在位置'),
        ('[PreventCriminalHealing', '切换玩家是否被允许治疗灰色生物（并因此变成罪犯）'),
        ('[PreventCriminalLooting', '切换玩家是否被允许搜刮蓝色尸体（并因此变成罪犯）'),
        ('[PreventBandageOverride', '切换是否阻止玩家对自己正在包扎的目标重复包扎'),
        ('[WarningRavens 或 [WarningRaven', '切换玩家是否会看到谋杀行为的警告乌鸦警报'),
        ('[WizardrySounds', '启用或禁用来自魔法书升级的巫师音效'),
        ('[CraftingQueue 或 [CQ', '打开制作队列菜单'),
        ('[GhostVisible', '允许幽灵在地下城与限制区域中始终看到你（即便当前不在同一队伍 / 公会 / 联盟）'),
        ('[SingleClickPoisonTicks', '切换单击生物时，是否显示该生物身上剩余的中毒跳数'),
        ('[PlaceTrap', '在当前位置放置一个地面陷阱'),
        ('[DetonateTrap', '引爆你当前激活的地面陷阱'),
        ('[Moongate', '尝试使用离玩家最近的月门'),
        ('[Recall &lt;名称&gt;', '尝试使用背包中符文书 / 符文册里第一个同名符文施放召回术（Recall）'),
        ('[RecallCharge &lt;名称&gt;', '尝试消耗符文书 / 符文册的一次充能来施放召回术'),
        ('[GateTravel &lt;名称&gt; 或 [Gate &lt;名称&gt;', '尝试使用第一个同名符文施放传送门术（Gate Travel）'),
        ('[GateTravelCharge &lt;名称&gt; 或 [GateCharge &lt;名称&gt;', '尝试消耗符文书 / 符文册的一次充能来施放传送门术'),
    ]),
    ('Text Displays', '文本显示', 'Text Displays', 'commandstextdisplay.png', [
        ('[ShowMeleeDamage', '在游戏内以文字显示玩家造成的近战与远程伤害'),
        ('[ShowSpellDamage', '在游戏内以文字显示玩家造成的法术伤害'),
        ('[ShowPoisonDamage', '在游戏内以文字显示玩家造成的毒素伤害'),
        ('[ShowSpecialDamage', '在游戏内以文字显示玩家造成的特殊伤害'),
        ('[ShowProvocationDamage', '在游戏内以文字显示被玩家激怒的目标所造成的伤害值'),
        ('[ShowFollowerDamage', '在游戏内以文字显示玩家随从造成的伤害值'),
        ('[ShowDamageTaken', '在游戏内以文字显示玩家承受的伤害'),
        ('[ShowFollowerDamageTaken', '在游戏内以文字显示玩家随从承受的伤害'),
        ('[ShowHealing', '在游戏内以文字显示玩家给出或受到的治疗量'),
        ('[ShowTamedExperience', '在游戏内以文字显示玩家驯服的生物所获得的经验'),
        ('[ShowAspectExperience', '在游戏内以文字显示玩家获得的元素经验'),
        ('[ShowSummonersTomeExperience', '在游戏内以文字显示玩家获得的召唤师之书经验'),
        ('[ShowStealthSteps', '在游戏内以文字显示玩家剩余的潜行步数'),
        ('[ShowBardingDurations', '显示生物身上的吟游效果持续时间'),
        ('[ShowTownStruggleAnnouncements', '显示是否以系统消息通知玩家城镇争夺的发生'),
        ('[ShowDungeonFlashpointAnnouncements', '显示是否以系统消息通知玩家地下城闪点的发生'),
        ('[ShowCorpseCreekContestAnnouncements', '显示是否以系统消息通知玩家尸溪竞赛的发生'),
        ('[ShowShrineCorruptionAnnouncements', '显示是否以系统消息通知玩家神龛腐化的发生'),
        ('[ShowStygianRiftsAnnouncements', '显示是否以系统消息通知玩家冥河裂隙的发生'),
        ('[ShowStrangelandsAnnouncements', '显示是否以系统消息通知玩家异境（Strangelands）的发生'),
        ('[ShowOmniBossAnnouncements', '显示是否以系统消息通知玩家全能 BOSS 事件的发生'),
        ('[ShowContestedBossAnnouncements', '显示是否以系统消息通知玩家争夺 BOSS 事件的发生'),
    ]),
    ('Ships', '船舰', 'Ships', 'commandsships.png', [
        ('[Stop', '停止船只的一切移动'),
        ('[Forward', '开始持续向前航行'),
        ('[ForwardLeft', '开始持续向前左航行'),
        ('[ForwardRight', '开始持续向前右航行'),
        ('[Left', '开始持续向左横移'),
        ('[Right', '开始持续向右横移'),
        ('[Backward', '开始持续向后移动'),
        ('[BackwardLeft', '开始持续向后左移动'),
        ('[BackwardRight', '开始持续向后右移动'),
        ('[TurnLeft', '将船向左转 90 度'),
        ('[TurnRight', '将船向右转 90 度'),
        ('[ForwardOne', '将船向前移动一格'),
        ('[ForwardLeftOne', '将船向前左移动一格'),
        ('[ForwardRightOne', '将船向前右移动一格'),
        ('[LeftOne', '将船向左移动一格'),
        ('[RightOne', '将船向右移动一格'),
        ('[BackwardOne', '将船向后移动一格'),
        ('[BackwardLeftOne', '将船向后左移动一格'),
        ('[BackwardRightOne', '将船向后右移动一格'),
        ('[Ship 或 [ShipMenu', '打开你当前所乘船只的船舰菜单'),
        ('[ShipHotbars', '打开你当前所乘船只的船舰快捷栏'),
        ('[Embark', '登上最近的友方船只'),
        ('[Disembark', '从当前船只下船'),
        ('[EmbarkFollowers', '将附近所有随从送上最近的友方船只'),
        ('[DisembarkFollowers', '让你的随从从当前船只下船'),
        ('[TargetingMode', '打开当前船只的瞄准模式菜单'),
        ('[Reload', '为当前船只的火炮重新装填'),
        ('[Dock', '提示玩家在某个地点或靠泊管理员处停靠船只'),
        ('[ThrowSelfOverboard', '立刻自我了断，并以幽灵形态出现在你最后一次经月门到访的城镇'),
        ('[ClearTheDeck', '移除甲板上所有可移动物品，并将其放入船上的垃圾桶'),
        ('[ReadyCrew', '让船员就位备战'),
        ('[SendCrewBelow', '让船员撤入下层'),
        ('[CrewAttack 或 [CrewTarget', '选择船员应攻击的目标；可对准自己的船只以攻击登船者'),
        ('[CrewStop 或 [CrewHalt', '让船员停止攻击当前目标'),
        ('[Ram 或 [RamShip', '撞击附近的船只（仅当你的船在 6 个或更多方向上被阻挡时可用）'),
        ('[SendBoardingParty 或 [SendBoarding', '打开派船登舰队窗口'),
        ('[RecallBoarding 或 [RecallBoardingParty', '召回所有当前活跃的登舰队'),
        ('[BoardingParty', '打开登舰队窗口，或召回所有当前活跃的登舰队'),
        ('[Repair', '打开船只修理窗口'),
        ('[RepairHull', '修理船体'),
        ('[RepairSails', '修理船帆'),
        ('[RepairGuns', '修理火炮'),
        ('[FireCannons', '向指定目标发射船只火炮'),
        ('[LesserAbility', '启动安装在船只第一「次级能力」槽的能力'),
        ('[SecondLesserAbility', '启动安装在船只第二「次级能力」槽的能力'),
        ('[RegularAbility', '启动安装在船只第一「常规能力」槽的能力'),
        ('[SecondRegularAbility', '启动安装在船只第二「常规能力」槽的能力'),
        ('[GreaterAbility', '启动安装在船只第一「高级能力」槽的能力'),
        ('[SecondGreaterAbility', '启动安装在船只第二「高级能力」槽的能力'),
        ('[AuxiliaryAbility', '启动安装在船只第一「辅助能力」槽的能力'),
        ('[SecondAuxiliaryAbility', '启动安装在船只第二「辅助能力」槽的能力'),
        ('[Spyglass', '双击背包中加成数值最高的望远镜'),
        ('[SpyglassContinuous', '启用或禁用船上望远镜的持续搜索功能'),
    ]),
    ('Codex', '宝典', 'Codex', 'commandscodex.png', [
        ('[CodexHotbar', '启动宝典快捷栏'),
        ('[AbilityHotbar', '打开能力快捷栏'),
        ('[WeaponAbility1', '启动所装备武器的第 1 项能力'),
        ('[WeaponAbility2', '启动所装备武器的第 2 项能力'),
        ('[WeaponAbility3', '启动所装备武器的第 3 项能力'),
    ]
        + _rep('[ArcaneStance{i}', '启动对应宝典第 {i} 位的奥术架势（Arcane Stance）', 5)
        + _rep('[ArcaneFinisher{i}', '启动对应宝典第 {i} 位的奥术终结技（Finisher）', 2)
        + _rep('[ArcheryAmmunition{i}', '启动对应宝典第 {i} 位的弓箭弹药（Ammunition）', 5)
        + _rep('[ArcheryFinisher{i}', '启动对应宝典第 {i} 位的弓箭终结技', 2)
        + _rep('[FencingStance{i}', '启动细剑宝典第 {i} 位的架势', 5)
        + _rep('[FencingFinisher{i}', '启动细剑宝典第 {i} 位的终结技', 2)
        + _rep('[FishingStance{i}', '启动钓鱼宝典第 {i} 位的架势', 5)
        + _rep('[FishingFinisher{i}', '启动钓鱼宝典第 {i} 位的终结技', 2)
        + _rep('[MacingStance{i}', '启动锤类宝典第 {i} 位的架势', 5)
        + _rep('[MacingFinisher{i}', '启动锤类宝典第 {i} 位的终结技', 2)
        + _rep('[SwordsStance{i}', '启动剑术宝典第 {i} 位的架势', 5)
        + _rep('[SwordsFinisher{i}', '启动剑术宝典第 {i} 位的终结技', 2)
        + _rep('[ShieldsStance{i}', '启动格挡宝典第 {i} 位的架势', 5)
        + _rep('[ShieldsFinisher{i}', '启动格挡宝典第 {i} 位的终结技', 2)
        + [('[StanceAutoRenewThroughMeditation', '切换主动冥想时，宝典架势是否自动续期')]
        + _rep('[WrestlingStance{i}', '启动徒手宝典第 {i} 位的架势', 5)
        + _rep('[WrestlingFinisher{i}', '启动徒手宝典第 {i} 位的终结技', 2)
        + _rep('[Stance{i}AutoRenew', '切换所持武器第 {i} 位宝典架势的自动续期处理方式', 5)),
    ('Aspect', '元素', 'Aspect', 'commandsaspect.png', [
        ('[AspectWeapon 元素名', '为所装备的武器激活某个元素。例：<code>[AspectWeapon Fire</code>'),
        ('[AspectWeapon 元素名 等级', '为所装备的武器激活指定等级的元素。例：<code>[AspectWeapon Fire 10</code>'),
        ('[AspectSpellbook 元素名', '为所装备的法术书激活某个元素。例：<code>[AspectSpellbook Fire</code>'),
        ('[AspectSpellbook 元素名 等级', '为所装备的法术书激活指定等级的元素。例：<code>[AspectSpellbook Fire 10</code>'),
        ('[AspectArmor 元素名', '为所装备的护甲激活某个元素。例：<code>[AspectArmor Fire</code>'),
        ('[AspectArmor 元素名 等级', '为所装备的护甲激活指定等级的元素。例：<code>[AspectArmor Fire 10</code>'),
        ('[LowerWeaponAspect', '临时降低武器元素等级'),
        ('[RaiseWeaponAspect', '临时提升武器元素等级'),
        ('[LowerSpellAspect', '临时降低法术书元素等级'),
        ('[RaiseSpellAspect', '临时提升法术书元素等级'),
        ('[LowerArmorAspect', '临时降低护甲元素等级'),
        ('[RaiseArmorAspect', '临时提升护甲元素等级'),
    ]),
    ('Guild', '公会', 'Guild', 'commandsguild.png', [
        ('[Guild', '启动公会页面'),
        ('[Resign', '退出当前公会'),
        ('[Overview', '打开公会页面的「总览」标签'),
        ('[Members', '打开公会页面的「成员」标签'),
        ('[Battle', '打开公会页面的「战斗」标签'),
        ('[TradeCaravan', '打开公会页面的「贸易商队」标签'),
        ('[Faction 或 [Factions', '打开公会页面的「阵营」标签'),
        ('[Candidates', '打开公会页面的「候选者」标签'),
        ('[Diplomacy', '打开公会页面的「外交」标签'),
        ('[Dungeons', '打开公会页面的「地下城」标签'),
        ('[Treasury', '打开公会页面的「金库」标签'),
        ('[BloodFeuds', '打开公会页面的「血仇」标签'),
        ('[Rewards', '打开公会页面的「奖励」标签'),
    ]),
    ('Chivalry', '骑士', 'Chivalry', 'commandschiv.png', [
        ('[Chivalry', '启动骑士菜单'),
        ('[ChivalryHotbar', '启动骑士快捷栏'),
        ('[ChivalryShowSymbolMessages', '切换是否显示圣徽数量的系统消息'),
        ('[RemoveCurse', '启动「移除诅咒」骑士能力'),
        ('[DispelEvil', '启动「驱散邪恶」骑士能力'),
        ('[CleanseByFire', '启动「烈火净化」骑士能力'),
        ('[ConsecrateWeapon', '启动「祝圣武器」骑士能力'),
        ('[CloseWounds', '启动「闭合伤口」骑士能力'),
        ('[EnemyofOne', '启动「指定宿敌」骑士能力'),
        ('[NobleSacrifice', '启动「崇高牺牲」骑士能力'),
        ('[DivineFury', '启动「神圣之怒」骑士能力'),
        ('[SacredJourney', '启动「神圣旅程」骑士能力'),
        ('[HolyLight', '启动「圣光」骑士能力'),
    ]
        + _rep('[Chivalry{i}', '启动第 {i} 位的骑士能力', 10)
        + [
        ('[RemoveCurseAutoRenew', '启动「移除诅咒」骑士能力的自动续期'),
        ('[DispelEvilAutoRenew', '启动「驱散邪恶」骑士能力的自动续期'),
        ('[CleanseByFireAutoRenew', '启动「烈火净化」骑士能力的自动续期'),
        ('[ConsecrateWeaponAutoRenew', '启动「祝圣武器」骑士能力的自动续期'),
        ('[CloseWoundsAutoRenew', '启动「闭合伤口」骑士能力的自动续期'),
        ('[EnemyofOneAutoRenew', '启动「指定宿敌」骑士能力的自动续期'),
        ('[NobleSacrificeAutoRenew', '启动「崇高牺牲」骑士能力的自动续期'),
        ('[DivineFuryAutoRenew', '启动「神圣之怒」骑士能力的自动续期'),
        ('[SacredJourneyAutoRenew', '启动「神圣旅程」骑士能力的自动续期'),
        ('[HolyLightAutoRenew', '启动「圣光」骑士能力的自动续期'),
        ]
        + _rep('[Chivalry{i}AutoRenew', '启动第 {i} 位骑士能力的自动续期', 10)),
    ('Necromancy', '死灵', 'Necromancy', 'commandsnecro.png', [
        ('[Necromancy', '启动死灵菜单'),
        ('[NecromancyHotBar', '启动死灵快捷栏'),
        ('[NecromancyShowSymbolMessages', '切换是否显示死灵符记数量的系统消息'),
        ('[NecromancyAutoRenewThroughMeditation', '切换主动冥想时，死灵能力是否自动续期'),
        ('[EvilOmen', '启动「凶兆」死灵能力'),
        ('[PoisonStrike', '启动「淬毒打击」死灵能力'),
        ('[VampiricEmbrace', '启动「吸血之拥」死灵能力'),
        ('[CorpseSkin', '启动「腐尸皮」死灵能力'),
        ('[Wither', '启动「枯萎」死灵能力'),
        ('[MindRot', '启动「心智腐蚀」死灵能力'),
        ('[BloodOath', '启动「血誓」死灵能力'),
        ('[PainSpike', '启动「痛苦尖刺」死灵能力'),
        ('[Strangle', '启动「扼杀」死灵能力'),
        ('[VengefulSpirit', '启动「复仇之灵」死灵能力'),
    ]
        + _rep('[Necromancy{i}', '启动第 {i} 位的死灵能力', 10)
        + [
        ('[EvilOmenAutoRenew', '启动「凶兆」死灵能力的自动续期'),
        ('[PoisonStrikeAutoRenew', '启动「淬毒打击」死灵能力的自动续期'),
        ('[VampiricEmbraceAutoRenew', '启动「吸血之拥」死灵能力的自动续期'),
        ('[CorpseSkinAutoRenew', '启动「腐尸皮」死灵能力的自动续期'),
        ('[WitherAutoRenew', '启动「枯萎」死灵能力的自动续期'),
        ('[MindRotAutoRenew', '启动「心智腐蚀」死灵能力的自动续期'),
        ('[BloodOathAutoRenew', '启动「血誓」死灵能力的自动续期'),
        ('[PainSpikeAutoRenew', '启动「痛苦尖刺」死灵能力的自动续期'),
        ('[StrangleAutoRenew', '启动「扼杀」死灵能力的自动续期'),
        ('[VengefulSpiritAutoRenew', '启动「复仇之灵」死灵能力的自动续期'),
        ]
        + _rep('[Necromancy{i}AutoRenew', '启动第 {i} 位死灵能力的自动续期', 10)),
    ('Factions', '阵营', 'Factions', 'commandsfactions.png', [
        ('[Faction 或 [Factions', '打开公会页面的「阵营」标签'),
        ('[FactionHotbar', '启动阵营快捷栏'),
        ('[FactionMap', '启动阵营地图'),
        ('[ShowFactionKills 或 [Punkte', '显示玩家通过击杀玩家所获得的赛季与生涯阵营积分'),
        ('[PreventFactionHealing', '切换（未加入阵营的）玩家是否可治疗阵营玩家，并因此被临时标记为阵营可攻击目标'),
        ('[ShowFactionGlobalAnnouncements', '显示是否以系统消息通知玩家阵营全局活动'),
        ('[ShowFactionCastleAnnouncements', '显示是否以系统消息通知玩家阵营城堡活动'),
        ('[ShowFactionFlagAnnouncements', '显示是否以系统消息通知玩家阵营旗帜活动'),
        ('[ShowFactionWaypostAnnouncements', '显示是否以系统消息通知玩家阵营驿站活动'),
        ('[ShowFactionWaypostRegionMessages', '显示玩家进入阵营驿站区域时是否会收到通知'),
    ]),
    ('Test Shard', '测试服务器', 'Test Shard', 'commandstestshard.png', []),
]

NAV = '''<nav class="site-nav">
  <span class="nav-brand">UO Outlands 中文资料库</span>
  <a href="../index.html">首页</a>
  <a href="../patch/index.html">版本更新</a>
  <a href="../skills/index.html">技能详解</a>
  <a href="../elements/index.html">元素精通</a>
  <a href="../mastery/index.html">精通链</a>
  <a href="../commands/index.html">命令大全</a>
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


def sid(en):
    return en.lower().replace(' ', '-')


def render_icon_nav():
    """顶部分类图标导航（与原站一致的两行：5 + 5 + 1）"""
    out = ['<div class="cmd-nav">']
    for en, cn, _, imgf, _ in SECTIONS:
        out.append(
            f'<a class="cmd-nav-item" href="#{sid(en)}">'
            f'<img src="{IMG}/{imgf}" alt="{en}" loading="lazy">'
            f'<span class="cmd-nav-zh">{cn}</span>'
            f'<span class="cmd-nav-en">{en}</span></a>')
    out.append('</div>')
    return '\n'.join(out)


def render_table(rows, title_cn, title_en, icon=None, wide=True):
    head = f'{title_cn} <span class="en">{title_en}</span>'
    if icon:
        head = f'<img class="cmd-sec-icon" src="{IMG}/{icon}" alt="{title_en}" loading="lazy"><br>{head}'
    out = [f'<table class="wikitable cmd-table{" cmd-wide" if wide else ""}">',
           f'<thead><tr><th colspan="2" class="cmd-sec">{head}</th></tr>',
           '<tr><th class="cmd-col-cmd">命令 <span class="en">Command</span></th>'
           '<th>说明 <span class="en">Description</span></th></tr></thead><tbody>']
    if not rows:
        out.append('<tr><td colspan="2" class="cmd-empty">'
                   '官方页面此章节暂无内容 <span class="en">No entries on the official wiki</span>'
                   '</td></tr>')
    for cmd, desc in rows:
        out.append(f'<tr><td class="cmd-name">{cmd}</td><td class="cmd-desc">{desc}</td></tr>')
    out.append('</tbody></table>')
    return '\n'.join(out)


def build():
    total = sum(len(s[4]) for s in SECTIONS)

    toc = ['<div class="toc"><div class="toctitle">目录</div><ol>',
           '<li><a href="#classicuo">ClassicUO 客户端命令 / ClassicUO Commands</a></li>',
           f'<li><a href="#outlands">UO Outlands 命令 / Outlands Commands</a></li>']
    for en, cn, _, _, rows in SECTIONS:
        toc.append(f'<li><a href="#{sid(en)}">{cn} / {en}</a></li>')
    toc.append('</ol></div>')
    toc = '\n'.join(toc)

    body = ['<h2 id="classicuo">ClassicUO 客户端命令 <span class="en-h">ClassicUO Commands</span></h2>',
            '<p>以下命令由 <b>ClassicUO</b> 客户端提供（与服务器无关），用于查看物品属性、切换客户端选项等。</p>',
            render_table(CLASSICUO, 'ClassicUO 客户端', 'ClassicUO Client', wide=False),
            '<h2 id="outlands">UO Outlands 命令 <span class="en-h">UO Outlands Commands</span></h2>',
            f'<p>以下是 UO Outlands 服务器提供的全部命令，共 <b>{total} 条</b>，分为 {len(SECTIONS)} 个类别。'
            '所有命令均以方括号 <code>[</code> 开头，在游戏聊天框输入即可执行；'
            '标注「或」的表示该命令有多个等效写法。</p>',
            render_icon_nav()]
    for en, cn, _, imgf, rows in SECTIONS:
        body.append(f'<h3 id="{sid(en)}">{cn} <span class="en-h">{en}</span></h3>')
        body.append(render_table(rows, cn, en, icon=imgf))
    body = '\n'.join(body)

    html_out = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>命令大全 Commands | UO Outlands 中文资料库</title>
<link rel="stylesheet" href="style.css?v={CSSV}">
  <link rel="stylesheet" href="../assets/theme.css">
  <script src="../assets/theme.js"></script>
</head>
<body class="side-nav-page">
{NAV}
<nav class="breadcrumb"><a href="../index.html">资料库首页</a> › <span>命令大全 Commands</span></nav>
<div class="source-link">官方原文：<a href="https://wiki.uooutlands.com/Commands" target="_blank" rel="noopener">wiki.uooutlands.com/Commands</a></div>
<div class="mw-body">
  <h1 class="mw-page-title-main">命令大全 <span class="cnsub">Commands</span></h1>
  <div class="cmd-intro">
    收录 UO Outlands 全部游戏内命令（<b>{total}</b> 条，{len(SECTIONS)} 类）与 ClassicUO 客户端命令。
    命令在游戏聊天框中以 <code>[</code> 开头输入；表中「说明」为中文译述，命令本身保持英文原文（游戏中需按英文输入）。
  </div>
  {toc}
  <div class="mw-content">
{body}
  </div>
</div>
<footer>
  <div><b>资料来源：</b>译自官方 Wiki <a href="https://wiki.uooutlands.com/Commands" target="_blank" rel="noopener">wiki.uooutlands.com/Commands</a>，非官方整理，仅供学习交流；命令以官方最新版本为准，如有出入欢迎反馈。</div>
  <div>UO Outlands 中文资料库 · 非官方粉丝翻译，版权归 Outlands 官方所有 · 2026-09-13</div>
</footer>
</body>
</html>
'''
    out_path = os.path.join(HERE, 'index.html')
    with open(out_path, 'w', encoding='utf-8', newline='') as f:
        f.write(html_out)
    print(f'已生成 {out_path}  ({len(html_out):,} 字节)')
    print(f'  ClassicUO 命令 {len(CLASSICUO)} 条')
    for en, cn, _, _, rows in SECTIONS:
        print(f'  {cn:<8} {en:<14} {len(rows):>3} 条')
    print(f'  合计 Outlands 命令 {total} 条')


if __name__ == '__main__':
    build()

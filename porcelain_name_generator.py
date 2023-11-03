import random

# 制作年代
EraValue = [
    "旧石器时代",
    "新石器时代",
    "夏",
    "商",
    "周",
    "西周",
    "东周",
    "春秋时代",
    "战国时代",
    "秦",
    "汉",
    "西汉",
    "新朝",
    "东汉",
    "三国",
    "魏",
    "蜀",
    "吴",
    "晋",
    "西晋",
    "东晋",
    "十六国",
    "前赵(汉赵)",
    "成汉",
    "前凉",
    "后赵",
    "前燕",
    "前秦",
    "后秦",
    "后燕",
    "西秦",
    "后凉",
    "南凉",
    "南燕",
    "西凉",
    "胡夏（大夏或北夏）",
    "北燕",
    "北凉",
    "南北朝",
    "南朝",
    "宋",
    "齐",
    "梁",
    "陈",
    "北朝",
    "北魏",
    "东魏",
    "西魏",
    "北齐",
    "北周",
    "隋",
    "唐",
    "五代十国",
    "后梁",
    "后唐",
    "后晋",
    "后汉",
    "后周",
    "十国",
    "宋",
    "北宋",
    "南宋",
    "辽",
    "大理",
    "西夏",
    "金",
    "元",
    "明",
    "清",
    "中华民国",
]
# 年号
eraName = [
    "建元",
    "元光",
    "元朔",
    "元狩",
    "元鼎",
    "元封",
    "太初",
    "天汉",
    "太始",
    "征和",
    "后元",
    "始元",
    "元凤",
    "元平",
    "本始",
    "地节",
    "元康",
    "神爵",
    "五凤",
    "甘露",
    "黄龙",
    "初元",
    "永光",
    "建昭",
    "竟宁",
    "建始",
    "河平",
    "阳朔",
    "鸿嘉",
    "永始",
    "元延",
    "绥和",
    "建平",
    "太初元将",
    "元寿",
    "元始",
    "居摄",
    "初始",
    "新朝及更始",
    "新朝",
    "始建国",
    "天凤",
    "地皇",
    "更始",
    "复汉",
    "龙兴",
    "建世",
    "东汉",
    "建武",
    "建武中元",
    "永平",
    "建初",
    "元和",
    "章和",
    "永元",
    "元兴",
    "延平",
    "永初",
    "元初",
    "永宁",
    "建光",
    "延光",
    "永建",
    "阳嘉",
    "永和",
    "汉安",
    "建康",
    "永嘉",
    "本初",
    "建和",
    "和平",
    "元嘉",
    "永兴",
    "永寿",
    "延熹",
    "永康",
    "建宁",
    "熹平",
    "光和",
    "中平",
    "光熹",
    "昭宁",
    "永汉",
    "初平",
    "兴平",
    "建安",
    "延康",
    "神上",
    "三国",
    "曹魏",
    "黄初",
    "太和",
    "青龙",
    "景初",
    "正始",
    "嘉平",
    "正元",
    "景元",
    "咸熙",
    "绍汉",
    "蜀汉",
    "章武",
    "延熙",
    "景耀",
    "炎兴",
    "孙吴",
    "黄武",
    "嘉禾",
    "赤乌",
    "太元",
    "神凤",
    "太平",
    "永安",
    "宝鼎",
    "建衡",
    "凤凰",
    "天册",
    "天玺",
    "天纪",
    "晋朝",
    "西晋",
    "泰始",
    "咸宁",
    "太康",
    "太熙",
    "永熙",
    "太安",
    "光熙",
    "东晋",
    "大兴",
    "永昌",
    "太宁",
    "咸和",
    "咸康",
    "升平",
    "隆和",
    "兴宁",
    "咸安",
    "宁康",
    "隆安",
    "大亨",
    "义熙",
    "元熙",
    "天康",
    "十六国",
    "汉赵",
    "永凤",
    "河瑞",
    "光兴",
    "麟嘉",
    "汉昌",
    "光初",
    "平赵",
    "成汉",
    "晏平",
    "玉衡",
    "大武",
    "玉恒",
    "汉兴",
    "嘉宁",
    "前凉",
    "建兴",
    "后赵",
    "延兴",
    "冉魏",
    "建国",
    "前燕",
    "燕元",
    "元玺",
    "光寿",
    "建熙",
    "前秦",
    "皇始",
    "寿光",
    "延初",
    "建昌",
    "黑龙",
    "后秦",
    "白雀",
    "皇初",
    "弘始",
    "后燕",
    "长乐",
    "光始",
    "定鼎",
    "西燕",
    "慕容泓",
    "燕兴",
    "昌平",
    "建明",
    "中兴",
    "西秦",
    "建义",
    "建弘",
    "永弘",
    "后凉",
    "龙飞",
    "承康",
    "神鼎",
    "南凉",
    "弘昌",
    "南燕",
    "燕平",
    "太上",
    "西凉",
    "庚子",
    "嘉兴",
    "夏",
    "龙昇",
    "凤翔",
    "昌武",
    "真兴",
    "承光",
    "胜光",
    "北燕",
    "太兴",
    "北凉",
    "神玺",
    "玄始",
    "承玄",
    "义和",
    "承阳",
    "缘禾",
    "承和",
    "太缘",
    "承平",
    "南北朝",
    "宋",
    "景平",
    "孝建",
    "大明",
    "景和",
    "泰豫",
    "元徽",
    "昇明",
    "义嘉",
    "开明",
    "齐",
    "永明",
    "隆昌",
    "永泰",
    "梁",
    "天监",
    "普通",
    "大通",
    "中大通",
    "大同",
    "中大同",
    "太清",
    "大宝",
    "天正",
    "承圣",
    "天成",
    "绍泰",
    "上愿",
    "天德",
    "正平",
    "天启",
    "西梁",
    "大定",
    "天保",
    "广运",
    "陈",
    "永定",
    "天嘉",
    "光大",
    "太建",
    "至德",
    "祯明",
    "北魏",
    "登国",
    "天兴",
    "天赐",
    "神瑞",
    "泰常",
    "始光",
    "神䴥",
    "延和",
    "太延",
    "太平真君",
    "兴安",
    "兴光",
    "天安",
    "皇兴",
    "承明",
    "景明",
    "延昌",
    "熙平",
    "神龟",
    "正光",
    "孝昌",
    "武泰",
    "普泰",
    "太昌",
    "圣君",
    "圣明",
    "大乘",
    "真王",
    "天建",
    "神嘉",
    "鲁兴",
    "始建",
    "广安",
    "天授",
    "隆绪",
    "天统",
    "神兽",
    "皇武",
    "孝基",
    "更兴",
    "东魏",
    "天平",
    "元象",
    "兴和",
    "武定",
    "平都",
    "西魏",
    "大统",
    "乾明",
    "北齐",
    "皇建",
    "河清",
    "武平",
    "隆化",
    "德昌",
    "安太",
    "北周",
    "武成",
    "保定",
    "天和",
    "建德",
    "宣政",
    "大成",
    "大象",
    "石平",
    "政通",
    "高句丽",
    "永乐",
    "延寿",
    "延嘉",
    "景□",
    "□熙",
    "柔然",
    "柔然[注",
    "高昌用该。",
    "始平",
    "高昌",
    "重光",
    "隋朝",
    "开皇",
    "仁寿",
    "大业",
    "义宁",
    "皇泰",
    "白乌",
    "大世",
    "始兴",
    "丁丑",
    "秦兴",
    "安乐",
    "鸣凤",
    "通圣",
    "永隆",
    "唐朝",
    "武德",
    "贞观",
    "永徽",
    "显庆",
    "龙朔",
    "麟德",
    "乾封",
    "总章",
    "咸亨",
    "上元",
    "仪凤",
    "乾通",
    "调露",
    "开耀",
    "永淳",
    "弘道",
    "嗣圣",
    "文明",
    "光宅",
    "垂拱",
    "载初",
    "武周",
    "如意",
    "长寿",
    "延载",
    "证圣",
    "天册万岁",
    "万岁登封",
    "万岁通天",
    "神功",
    "圣历",
    "久视",
    "大足",
    "长安",
    "神龙",
    "续唐朝",
    "景龙",
    "唐隆",
    "景云",
    "太极",
    "先天",
    "开元",
    "天宝",
    "乾元",
    "宝应",
    "广德",
    "大历",
    "建中",
    "兴元",
    "贞元",
    "永贞",
    "永新",
    "长庆",
    "宝历",
    "大和",
    "开成",
    "会昌",
    "大中",
    "咸通",
    "乾符",
    "广明",
    "中和",
    "光启",
    "文德",
    "龙纪",
    "大顺",
    "景福",
    "乾宁",
    "光化",
    "天复",
    "天祐",
    "天寿",
    "昌达",
    "法轮",
    "明政",
    "天造",
    "天明",
    "乾德",
    "进通",
    "中元克复",
    "圣武",
    "应天",
    "顺天",
    "显圣",
    "正德",
    "宝胜",
    "天皇",
    "罗平",
    "王霸",
    "金统",
    "建贞",
    "吐蕃",
    "彝泰",
    "于阗",
    "同庆",
    "天尊",
    "渤海",
    "仁安",
    "正历",
    "永德",
    "朱雀",
    "东丹",
    "定安",
    "南诏及大理",
    "南诏",
    "赞普钟",
    "见龙",
    "应道",
    "全义",
    "大丰",
    "保和",
    "建极",
    "法尧",
    "嵯耶",
    "大长和",
    "安国",
    "孝治[注",
    "天瑞景星",
    "安和",
    "贞祐",
    "初历",
    "天应",
    "大天兴",
    "尊圣",
    "大义宁",
    "兴圣",
    "鼎新",
    "光圣",
    "大理",
    "神武",
    "文经",
    "至治",
    "明德",
    "顺德",
    "明圣",
    "明统",
    "明治",
    "明应",
    "明法",
    "明运",
    "明启",
    "乾兴",
    "明通",
    "正治",
    "保安",
    "政安",
    "保德",
    "明侯",
    "上德",
    "上明",
    "保立",
    "上治",
    "后大理",
    "明开",
    "天政",
    "文安",
    "日新",
    "文治",
    "嘉永",
    "保天",
    "盛明",
    "利贞",
    "盛德",
    "嘉会",
    "元亨",
    "亨时",
    "凤历",
    "天开",
    "天辅",
    "道隆",
    "天定",
    "利正",
    "兴正",
    "大本",
    "锺元",
    "越政",
    "隆德",
    "永道",
    "圣□",
    "五代十国",
    "后梁",
    "开平",
    "乾化",
    "贞明",
    "龙德",
    "后唐",
    "前晋",
    "同光",
    "长兴",
    "应顺",
    "清泰",
    "后晋",
    "天福",
    "开运",
    "通容",
    "后汉",
    "乾祐",
    "后周",
    "广顺",
    "显德",
    "吴",
    "武义",
    "顺义",
    "乾贞",
    "天祚",
    "南唐",
    "昇元",
    "保大",
    "交泰",
    "建隆",
    "开宝",
    "吴越",
    "宝大",
    "宝正",
    "广初",
    "正明",
    "会同",
    "太平兴国",
    "楚",
    "闽",
    "龙启",
    "通文",
    "南汉",
    "乾亨",
    "白龙",
    "大有",
    "光天",
    "应乾",
    "乾和",
    "前蜀",
    "通正",
    "后蜀",
    "广政",
    "荆南",
    "北汉",
    "天会",
    "宋朝",
    "北宋",
    "雍熙",
    "端拱",
    "淳化",
    "至道",
    "咸平",
    "景德",
    "大中祥符",
    "天禧",
    "天圣",
    "明道",
    "景祐",
    "宝元",
    "康定",
    "庆历",
    "皇祐",
    "至和",
    "嘉祐",
    "治平",
    "熙宁",
    "元丰",
    "元祐",
    "绍圣",
    "元符",
    "建中靖国",
    "崇宁",
    "大观",
    "政和",
    "重和",
    "宣和",
    "靖康",
    "应运",
    "化顺",
    "得圣",
    "景瑞",
    "启历",
    "端懿",
    "隆兴",
    "风和",
    "南宋",
    "建炎",
    "绍兴",
    "乾道",
    "纯熙",
    "淳熙",
    "绍熙",
    "庆元",
    "嘉泰",
    "开禧",
    "嘉定",
    "宝庆",
    "绍定",
    "端平",
    "嘉熙",
    "淳祐",
    "宝祐",
    "开庆",
    "景定",
    "咸淳",
    "德祐",
    "景炎",
    "祥兴",
    "明受",
    "天载",
    "天战",
    "正法",
    "人知",
    "阜昌",
    "大圣天王",
    "庚戌",
    "转运",
    "重德",
    "辽朝",
    "神册",
    "天赞",
    "天显",
    "天禄",
    "应历",
    "保宁",
    "统和",
    "开泰",
    "重熙",
    "清宁",
    "咸雍",
    "大康",
    "大安",
    "寿昌",
    "乾统",
    "天庆",
    "北辽",
    "建福",
    "德兴",
    "西北辽",
    "神历",
    "隆基",
    "天嗣",
    "西辽",
    "延庆",
    "康国",
    "咸清",
    "感天",
    "续兴",
    "崇福",
    "皇德",
    "天喜",
    "西夏",
    "显道",
    "大庆",
    "广熙",
    "广民",
    "延嗣宁国",
    "天祐垂圣",
    "福圣承道",
    "奲都",
    "拱化",
    "天安礼定",
    "西安",
    "天仪治平",
    "天祐民安",
    "雍宁",
    "元德",
    "大德",
    "人庆",
    "天盛",
    "光定",
    "乾定",
    "宝义",
    "广僖",
    "清平",
    "成都",
    "大礼平定",
    "金朝",
    "收国",
    "天眷",
    "皇统",
    "正隆",
    "兴庆",
    "明昌",
    "承安",
    "泰和",
    "崇庆",
    "至宁",
    "兴定",
    "正大",
    "开兴",
    "盛昌",
    "新德",
    "身圣",
    "天顺",
    "天泰",
    "大汉",
    "兴隆",
    "天威",
    "元朝",
    "中统",
    "至元",
    "元贞",
    "至大",
    "皇庆",
    "延祐",
    "泰定",
    "致和",
    "天历",
    "至顺",
    "元统",
    "至正",
    "北元",
    "宣光",
    "天元",
    "万乘",
    "昌泰",
    "安定",
    "赤符",
    "正朔",
    "天佑",
    "龙凤",
    "大义",
    "德寿",
    "开熙",
    "甲辰",
    "吴元",
    "明朝",
    "洪武",
    "建文",
    "洪熙",
    "宣德",
    "正统",
    "景泰",
    "成化",
    "弘治",
    "嘉靖",
    "隆庆",
    "万历",
    "泰昌",
    "崇祯",
    "永天",
    "涌安",
    "东阳",
    "玄武",
    "添元",
    "天绣",
    "武烈",
    "宏闰",
    "德胜",
    "明正",
    "大顺平定",
    "大中天武",
    "天渊",
    "造历",
    "圆明大宝",
    "弘武",
    "天真混",
    "瑞应",
    "大成兴胜",
    "一统",
    "玄静",
    "懿德",
    "宽和",
    "灵宝",
    "兴武",
    "天运",
    "义兴",
    "天令",
    "义武",
    "南明",
    "弘光",
    "隆武",
    "永历",
    "兴业",
    "庚寅",
    "定武",
    "绍武",
    "东武",
    "清朝",
    "后金",
    "天命",
    "天聪",
    "崇德",
    "顺治",
    "康熙",
    "雍正",
    "乾隆",
    "嘉庆",
    "道光",
    "咸丰",
    "祺祥",
    "同治",
    "光绪",
    "宣统",
    "重兴",
    "清光",
    "兴朝",
    "周启",
    "昭武",
    "利用",
    "洪化",
    "裕民",
    "文兴",
    "仙大",
    "万利",
    "光明",
    "晏朝",
    "大明主",
    "奉天",
    "洪顺",
    "江汉",
    "太平天德",
    "洪德",
    "全福",
    "嗣统",
    "华汉",
    "天纵",
    "成正",
    "永清",
    "保庆",
    "兴洪",
    "汉德",
    "共戴",
    "洪宪",
    "通治",
    "和兴",
    "熙顺",
    "康德",
]
# 窑别
Kiln = [
    "汝窑",
    "官窑",
    "哥窑",
    "定窑",
    "钧窑",
    "景德镇窑",
    "耀州窑",
    "磁州窑",
    "巩县窑",
    "龙泉窑",
    "越窑",
    "建窑",
    "邢窑",
    "铜官窑",
    "邛窑",
    "西村窑",
    "当阳峪窑",
    "鹤壁窑",
    "德化窑",
    "瓯窑",
    "余杭窑",
    "婺州窑",
    "德清窑",
    "鄞县窑",
    "武义窑",
    "西山窑",
    "吴兴窑",
    "象山窑",
    "富盛窑",
    "黄岩窑",
    "绍兴窑",
    "萧山窑",
    "丽水窑",
    "泰顺窑",
    "临汝窑",
    "鹤壁窑",
    "密县窑",
    "登封窑",
    "鲁山窑",
    "郏县窑",
    "巩县窑",
    "宜阳窑",
    "宝丰窑",
    "安阳窑",
    "同安窑",
    "泉州窑",
    "安溪窑",
    "南安窑",
    "崇安窑",
    "福清窑",
    "光泽窑",
    "连江窑",
    "闽清窑",
    "莆田窑",
    "乐平窑",
    "吉州窑",
    "白浒窑",
    "南丰窑",
    "平定窑",
    "介休窑",
    "大同窑",
    "怀仁窑",
    "阳城窑",
    "蒲州窑",
    "长治窑",
    "交城窑",
    "榆次窑",
    "浦城窑",
    "白舍窑",
    "丰城窑",
    "赣州窑",
    "浑源窑",
    "盂县窑",
    "旬邑窑",
    "林东窑",
    "安口窑",
    "岳州窑",
    "湘阴窑",
    "寿州窑",
    "繁昌窑",
    "淮南窑",
    "泗州窑",
    "彭县窑",
    "广元窑",
    "大邑窑",
    "华阳窑",
    "玉溪窑",
    "西村窑",
    "潮州窑",
    "惠阳窑",
    "永福窑",
    "藤县窑",
    "容县窑",
    "兴安窑",
    "淄博窑",
    "曲阳窑",
    "辽阳窑",
    "赤峰窑",
    "长沙窑",
    "均山窑",
]
# 器型
Shape = [
    "鬲式炉",
    "博山炉",
    "熏炉",
    "曲足炉",
    "筒式炉",
    "鼎式炉",
    "出戟尊",
    "太白尊",
    "观音尊",
    "萝卜尊",
    "苹果尊",
    "牛头尊",
    "无档尊",
    "鱼篓尊",
    "石榴尊",
    "马蹄尊",
    "凤尾尊",
    "唾壶",
    "盘口壶",
    "鸡头壶",
    "执壶",
    "鸡心壶",
    "提梁壶",
    "僧帽壶",
    "贲巴壶",
    "梨壶",
    "军持",
    "四系罐",
    "小口折肩罐",
    "鼓腹小罐",
    "天字罐",
    "将军罐",
    "荷叶盖罐",
    "梅瓶",
    "玉壶春瓶",
    "蒜头瓶",
    "宝月瓶",
    "棒槌瓶",
    "多管瓶",
    "琮式瓶",
    "胆式瓶",
    "象腿瓶",
    "天球瓶",
    "橄榄瓶",
    "凤尾瓶",
    "油锤瓶",
    "柳叶瓶",
    "葫芦瓶",
    "洗口瓶",
    "瓜棱瓶",
    "双耳瓶",
    "卷口瓶",
    "花口瓶",
    "连座瓶",
    "直颈六棱瓶",
    "撇口大瓶",
    "鸡缸杯",
    "压手杯",
    "爵杯",
    "高足杯",
    "高足碗",
    "宫碗",
    "鸡心碗",
    "斗笠碗",
    "折腰碗",
    "卧足碗",
    "孔明碗",
    "豆",
    "花觚",
    "砚",
    "盒",
    "折沿盘",
    "枕",
    "花浇",
    "渣斗",
    "谷仓",
    "瓷塑（俑）",
    "虎子",
    "海棠式盆",
    "烛台",
    "灯盏",
    "盘",
    "瓮",
    "盂",
    "钵",
    "盆",
]
# 釉彩
GlazeColor = [
    "青釉",
    "粉青",
    "梅子青",
    "月白",
    "天青",
    "豆青",
    "冬青",
    "豆绿",
    "翠青",
    "卵白釉",
    "甜白釉",
    "象牙白釉",
    "青白釉",
    "纯黑釉",
    "青黑釉",
    "灰黑釉",
    "灰白釉",
    "兔毫釉",
    "油滴釉",
    "曜变釉",
    "结晶冰花纹釉",
    "郎红",
    "豇豆红",
    "祭红",
    "钧红",
    "珊瑚红",
    "胭脂红",
    "娇黄",
    "姜黄",
    "蜜蜡黄",
    "蛋黄釉",
    "鳝鱼黄",
    "茶叶末",
    "松石绿",
    "孔雀绿",
    "孔雀蓝釉",
    "祭蓝釉",
    "洒蓝釉",
    "霁蓝釉",
    "天蓝釉",
    "釉上彩",
    "釉上五彩",
    "粉彩",
    "素云彩",
    "珐琅彩",
    "新彩",
    "墨彩",
    "釉下彩",
    "青釉褐绿彩",
    "青花",
    "釉里红",
    "釉下三彩",
    "釉下五彩",
    "斗彩",
    "釉中彩",
]
# 纹饰
Decorate = []
# 胎质
procelainMaterial = ["陶胎", "瓷胎", "浆胎", "缸胎"]


def generate_porcelain_names(count):
    """
    Generate a list of random porcelain names.

    This function creates porcelain names by randomly combining elements from
    predefined lists of eras, kilns, shapes, and colors. Each porcelain name is
    generated by concatenating one element from each list and the list of names
    is returned.

    Parameters:
    count : int
        The number of porcelain names to generate.

    Returns:
    list
        A list of generated porcelain names.
    """
    er = random.choices(eraName, k=count)
    kiln = random.choices(Kiln, k=count)
    color = random.choices(GlazeColor, k=count)
    shape = random.choices(Shape, k=count)

    porcelain_names = [f"{e}{k}{c}{s}" for e, k, c, s in zip(er, kiln, color, shape)]
    return porcelain_names


if __name__ == "__main__":
    count = int(input("输入需要生成的数量: "))
    names = generate_porcelain_names(count)
    for name in names:
        print(name)
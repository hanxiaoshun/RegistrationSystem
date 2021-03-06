/**
 * 首先选择将要申报的级别
 */

chemical_industry = ["工业废水处理工", "无机化学反应生产工", "有机合成工", "防腐蚀工", "工业固体废物处理处置工"];
not_chemical_industry = ["钳工", "电工", '焊工', "保育员", "育婴员", '劳动关系协调员'];
electromechanical = ["钳工", "电工", '焊工'];
// # 经营管理类型
administration = ['劳动关系协调员'];
// # 育儿管理;
parenting = ["保育员", "育婴员"];

worker_level = {
    '1': '高级技工',
    '2': '技工',
    '3': '高级',
    '4': '中级',
    '5': '初级',
    '99': '无级别信息'
};

political_status = {
    '0': '中共党员',
    '1': '中共预备党员',
    '2': '共青团员',
    '3': '民革党员',
    '4': '民盟盟员',
    '5': '民建会员',
    '6': '民进会员',
    '7': '农工党党员',
    '8': '致公党党员',
    '9': '九三学社社员',
    '10': '台盟盟员',
    '11': '无党派人士',
    '12': '群众(普通居民)'
};

// # 电焊相关专业
electric_welding = {'0': '焊接加工', '1': '焊接技术应用', '2': '金属热加工（焊接）', '3': '焊接技术与自动化', '4': '焊接技术与工程'}

// # 电工相关专业
electrician_relevant = {
    '0': '数控机床装配与维修',
    '1': '机械设备装配与自动控制',
    '2': '制冷设备运用与维修',
    '3': '机电设备安装与维修',
    '4': '机电一体化',
    '5': '电气自动化设备安装与维修',
    '6': '电梯工程技术',
    '7': '城市轨道交通车辆运用与检修',
    '8': '致公党党员',
    '9': '九三学社社员',
    '10': '台盟盟员',
    '11': '无党派人士',
    '12': '群众(普通居民)',
    '13': '煤矿电气设备维修',
    '14': '工业机器人应用与维护',
    '15': '工业网络技术',
    '16': '机电技术应用',
    '17': '电气运行与控制',
    '18': '电气技术应用',
    '19': '纺织机电技术',
    '20': '铁道供电技术',
    '21': '农业电气化技术'
};
// # 钳工目前没有相关专业

// # 劳动关系协调员相关职业
let labor_relations_relevant_job = {'0': '人力资源管理', '1': '劳动保障事务处理', '2': '社会工作等职业'};
// # 劳动关系协调员相关职业;
let labor_relations_relevant_majors = {
    '0': '劳动与社会保障',
    '1': '劳动经济学',
    '2': '人力资源管理',
    '3': '工商企业管理',
    '4': '法学',
    '5': '社会学'
};
// # 劳动关系协调员相关职业资格证书
let labor_relations_voc_qual_certi = {'0': '企业人力资源管理师', '1': '劳动保障协理员', '2': '劳动保障专理员', '3': '社会工作者'};
// # 防腐蚀工相关职业
let anticorrosive_worker_relevant_job = {
    '0': '耐蚀衬胶工', '1': '耐蚀喷涂工', '2': '耐蚀砖板衬里工', '3': '耐蚀塑料工', '4': '耐蚀纤维增强塑料工',
    '5': '耐蚀混凝土工'
};
// # 无机化学反应生产工相关职业
let icrp_anticorrosive_worker = {
    '0': '电化学反应工', '1': '窑炉反应工', '2': '黄磷生产工', '3': '电石生产工', '4': '钛白粉生产工', '5': '高频等离子工',
    '6': '二硫化碳生产工', '7': '炭黑生产工'
};

let title_switch = {
    '1': "电工",
    '2': "焊工",
    '3': "钳工",
    '4': "育婴员",
    '5': "保育员",
    '6': "劳动关系协调员",
    '7': '防腐蚀工',
    '8': '有机合成工',
    '9': '工业废水处理工',
    '10': '无机化学反应生产工',
    '11': '固体废物处理工',
};


/**
 * 检测申报资格名称以及职级
 * @param obj
 */
function check_identification_level(obj) {
    // 获取申报的职业信息
    let worker = $("#declaration_of_occupation").val();
// 级别按钮
    let identification_level = $("#identification_level");
    let worker_level = $(".worker_level_desc");
    let worker_level_desc_label = $(".worker_level_desc_label");
    let worker_level_content = $(".worker_level_desc_content");
    let worker_level_desc_content_textarea = $(".worker_level_desc_content_textarea");

//是否需要
    let has_qualification_class = $('.has_qualification');
    let graduation_status_class = $('.graduation_status');
    let condition_selected_class = $('.condition_selected');
//职业年限
    let career_life_class = $(".career_life");
//术等级（原级别）
    let primary_level_class = $(".primary_level");
// 现持有职业资格证书编号(原证书编号)
    let original_certificate_number_class = $(".original_certificate_number");
// 现有证件发证单位
    let issue_unit_class = $(".issue_unit");
//现有职业资格证发证时间
    let issuance_time_class = $(".issuance_time");
//从事本职业工作开始时间
    let start_the_work_of_this_occupation_class = $(".start_the_work_of_this_occupation");
// 职业资格证图片上传
    let certificate_photos_class = $('.certificate_photos');
//=========================================================================================

// 学历程度
    let education_degree_class = $(".education_degree");
//毕业（应届）院校名称
    let school_name_class = $(".school_name");
// 毕业时间(或即将毕业时间)
    let graduation_time_class = $(".graduation_time");
//专业工种(或相关专业工种)
    let profession_class = $(".profession");
//被授予毕业资格证书名称
    let diploma_granted_class = $(".diploma_granted");
// 报名单位负责人
    let person_in_charge_class = $(".person_in_charge");
// 毕业证图片上传
    let diploma_certificate_photos_class = $('.diploma_certificate_photos');
    let title_level = {
        '3': "高级工",
        '4': "中级工",
        '5': "初级工"
    };

    if (parseInt(obj) === 0) {
        alert("请您选择申报-" + worker + "的等级");
    } else {
        if (worker === "电工") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "dg03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "dg04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "dg05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "焊工") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "dhg03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "dhg04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "dhg05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "钳工") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "qg03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "qg04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "qg05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "育婴员") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "yyy03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "yyy04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "yyy05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "保育员") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "byy03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "byy04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "byy05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "劳动关系协调员") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "ldgxxty03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "ldgxxty04";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "防腐蚀工") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "hg03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "hg04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "hg05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "有机合成工") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "hg03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "hg04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "hg05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "工业废水处理工") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "hg03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "hg04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "hg05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "无机化学反应生产工") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "hg03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "hg04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "hg05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else if (worker === "固体废物处理工") {
            if (parseInt(obj) === 3) {
                // 高级工
                let work_level_tag = "hg03";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 4) {
                // 中级工
                let work_level_tag = "hg04";
                put_select(work_level_tag, parseInt(obj));

            } else if (parseInt(obj) === 5) {
                // 初级工
                let work_level_tag = "hg05";
                put_select(work_level_tag, parseInt(obj));

            } else {
                put_select('null', 0);
            }
        } else {
            worker_level.hide();
            worker_level_content.hide();
        }

    }
}

function put_select(work_level_tag, index) {

    // 获取申报的职业信息
    let worker = $("#declaration_of_occupation").val();
// 级别按钮
    let identification_level = $("#identification_level");
    let worker_level = $(".worker_level_desc");
    let worker_level_desc_label = $(".worker_level_desc_label");
    let worker_level_content = $(".worker_level_desc_content");
    let worker_level_desc_content_textarea = $(".worker_level_desc_content_textarea");

//是否需要
    let has_qualification_class = $('.has_qualification');
    let graduation_status_class = $('.graduation_status');
    let condition_selected_class = $('.condition_selected');
//职业年限
    let career_life_class = $(".career_life");
//术等级（原级别）
    let primary_level_class = $(".primary_level");
// 现持有职业资格证书编号(原证书编号)
    let original_certificate_number_class = $(".original_certificate_number");
// 现有证件发证单位
    let issue_unit_class = $(".issue_unit");
//现有职业资格证发证时间
    let issuance_time_class = $(".issuance_time");
//从事本职业工作开始时间
    let start_the_work_of_this_occupation_class = $(".start_the_work_of_this_occupation");
// 职业资格证图片上传
    let certificate_photos_class = $('.certificate_photos');
//=========================================================================================

// 学历程度
    let education_degree_class = $(".education_degree");
//毕业（应届）院校名称
    let school_name_class = $(".school_name");
// 毕业时间(或即将毕业时间)
    let graduation_time_class = $(".graduation_time");
//专业工种(或相关专业工种)
    let profession_class = $(".profession");
//被授予毕业资格证书名称
    let diploma_granted_class = $(".diploma_granted");
// 报名单位负责人
    let person_in_charge_class = $(".person_in_charge");
// 毕业证图片上传
    let diploma_certificate_photos_class = $('.diploma_certificate_photos');
    let title_level = {
        '3': "高级工",
        '4': "中级工",
        '5': "初级工"
    };


    worker_level.show();
    worker_level_content.show();
    if (work_level_tag === 'null') {
        let worker_level_desc = '申报-' + worker + '-' + "未分级" + "条件说明";
        worker_level_desc_label.text(worker_level_desc);
        worker_level_desc_content_textarea.val("暂无相关介绍信息，您可能未选择申报职业资格级别，请选择申报职业资格级别在尝试！");
        identification_level.focus();
    } else {
        let worker_level_desc = '申报-' + worker + '-' + title_level[index.toString()] + "条件说明";
        let worker_level_desc_content = get_worker_level_info(work_level_tag);
        worker_level_desc_label.text(worker_level_desc);
        worker_level_desc_content_textarea.val(worker_level_desc_content);

        let condition_selected = "";
        $.each(get_worker_level_condition_selected(work_level_tag), function (i, n) {
            if (n.indexOf("注：") > -1) {
                condition_selected = condition_selected +
                    "<label style='color:honeydew' title=" + n + ">" + n +
                    "</label>" +
                    "<br>"
            } else {
                let work_level_tag_index = work_level_tag + "_" + i.toString();
                condition_selected = condition_selected +
                    "<input type='radio' name='condition_selected'" +
                    " value=" + work_level_tag_index +
                    "id=" + work_level_tag_index +
                    " onclick='condition_selected(" + work_level_tag_index + ");'/>" +
                    "<label for='" + work_level_tag_index +
                    "' style='color:white' title=" + n + ">" + n +
                    "</label>" +
                    "<br>"
            }
        });

        condition_selected_class.empty("");
        condition_selected_class.append(condition_selected);
    }

}

function get_worker_level_info(obj) {
    let m = new Map();
    m.set('dhg05', '五级/初级工 ( 具备以下条件之一者 )\n' +
        '(1) 累计从事本职业工作１年( 含)以上。\n' +
        '(2) 本职业学徒期满。');
    m.set('dhg04', '四级/中级工( 具备以下条件之一者 )\n' +
        '(1) 取得本职业五级/ 初级工职业资格证书( 技能等级证书)后，累计从事本职业工作４年(含)以上。\n' +
        '(2) 累计从事本职业工作６年(含)以上。\n' +
        '(3) 取得技工学校本专业或相关专业毕业证书( 含尚未取得毕业证书的在校应届毕业生)；' +
        '或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ' +
        '( 含尚未取得毕业证书的在校应届毕业生)。注：相关专业：' +
        '焊接加工、焊接技术应用、金属热加工（焊接）、焊接技术与自动化、焊接技术与工程。');
    m.set('dhg03', '三级/高级工( 具备以下条件之一者 )\n' +
        '(1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作５ 年( 含) 以上。\n' +
        '(2) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；' +
        '或取得本职业四级/ 中级工职业资格证书，并具有经评估论证、 以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 (含尚未取得毕业证书的在校应届毕业生)。 \n' +
        '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业工作２年( 含) 以上。');
    m.set('dg05', '五级/初级工 ( 具备以下条件之一者 )\n' +
        '(1) 累计从事本职业工作１年( 含)以上。\n' +
        '(2) 本职业学徒期满。');
    m.set('dg04', '四级/中级工( 具备以下条件之一者 )\n' +
        '(1) 取得本职业五级/ 初级工职业资格证书( 技能等级证书)后，累计从事本职业工作４年(含)以上。\n' +
        '(2) 累计从事本职业工作６年(含)以上。\n' +
        '(3) 取得技工学校本专业或相关专业毕业证书( 含尚未取得毕业证书的在校应届毕业生)；或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。');
    m.set('dg03', '三级/高级工( 具备以下条件之一者 )\n' +
        '(1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作５ 年( 含) 以上。\n' +
        '(2) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；' +
        '或取得本职业四级/ 中级工职业资格证书，并具有经评估论证、 以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 (含尚未取得毕业证书的在校应届毕业生)。 \n' +
        '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业工作２年( 含) 以上。注：本专业或相关专业: ' +
        '数控机床装配与维修、机械设备装配与自动控制、制冷设备运用与维修、机电设备安装与维修、机电一体化、电气自动化设备安装与维修 、电梯工程技术、城市轨道交通车辆运用与检修 、煤矿电气设备维修、' +
        '工业机器人应用与维护、工业网络技术、机电技术应用、电气运行与控制、电气技术应用、纺织机电技术、铁道供电技术、农业电气化技术等专业。');
    m.set('qg05', '初级 ( 具备以下条件之一者 )\n' +
        '(1) 经本职业初级正规培训达规定标准学时数，并取得结业证书。\n' +
        '(2) 在本职业连续见习工作 2 年以上。\n' +
        '(3) 本职业学徒期满。');
    m.set('qg04', '中级 ( 具备下列条件之一者 )\n' +
        '(1) 取得本职业初级职业资格证书后，连续从事本职业工作 3 年以上，经本职业中级正规培训达规定标准学时数，并取得结业证书。\n' +
        '(2) 取得本职业初级职业资格证书后，连续从事本职业工作 5 年以上。\n' +
        '(3) 连续从事本职业工作 7 年以上。\n' +
        '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。');
    m.set('qg03', '高级 ( 具备下列条件之一者〉\n' +
        '(1) 取得本职业中级职业资格证书后，连续从事本职业工作 4 年以上，经本职业高级正规培训达规定标准学时数，并取得结业证书。\n' +
        '(2) 取得本职业中级职业资格证书后，连续从事本职业工作 7 年以上。\n' +
        '(3) 取得高级技工学校或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校或高级技工学校本职业 ( 专业 ) 毕业证书。\n' +
        '(4) 大专以上本专业或相关专业毕业生取得本职业中级职业资格证书后, 连续从事本职业工作 2 年以上。');
    m.set('yyy05', '初级(具备以下条件之一者)\n' +
        '(1)经本职业初级正规培训达规定标准学时数，并取得结业证书。\n' +
        '（2）在本职业连续见习工作2年以上。\n' +
        '（3）本职业学徒期满。');
    m.set('yyy04', '中级(具备以下条件之一者)\n' +
        '(1)取得本职业初级职业资格证书后，连续从事本职业工作3年以上，经本职业中级正规培训达规定标准学时数，并取得结业证书。\n' +
        '（2）取得本职业初级职业资格证书后，连续从事本职业工作5年以上。\n' +
        '（3）连续从事本职业工作7年以上。\n' +
        '（4）取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业(专业)毕业证书。');
    m.set('yyy03', '高级(具备以下条件之一者)\n' +
        '(1)取得本职业中级职业资格证书后，连续从事本职业工作4年以上，经本职业高级正规培训达规定标准学时数，并取得结业证书。\n' +
        '（2）取得本职业中级职业资格证书后，连续从事本职业工作6年以上。\n' +
        '（3）取得高级技工学校或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业(专业)毕业证书。\n' +
        '（4）取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生，连续从事本职业工作2年以上。');
    m.set('byy05', '初级 ( 具备以下条件之一者 )\n' +
        '(1) 经本职业初级正规培训达规定标准学时数，并取得结业证书。\n' +
        '(2) 在本职业连续见习工作2年以上。\n' +
        '(3) 本职业学徒期满。');
    m.set('byy04', '中级 ( 具备以下条件之一者 )\n' +
        '(1) 取得本职业初级职业资格证书后，连续从事本职业工作 3 年以上，经本职业中级正规培训达规定标准学时数，并取得结业证书。\n' +
        '(2) 取得本职业初级职业资格证书后，连续从事本职业工作 5 年以上。\n' +
        '(3) 连续从事本职业工作 7 年以上。\n' +
        '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。');
    m.set('byy03', '高级 ( 具备以下条件之一者 )\n' +
        '(1) 取得本职业中级职业资格证书后，连续从事本职业工作 4 年以上，经本职业高级正规培训达规定标准学时数，并取得结业证书。\n' +
        '(2) 取得本职业中级职业资格证书后，连续从事本职业工作 6 年以上。\n' +
        '(3) 取得高级技工学校或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。\n' +
        '(4) 取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生，连续从事本职业工作 2 年以上。');
    m.set('ldgxxty04', '四级/中级工（具备以下条件之一者） \n' +
        '（1） 累计从事本职业或相关职业工作 4 年（含）以上。 \n' +
        '（2） 取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。 \n' +
        '（3）高等院校本专业或相关专业在校生。 ');
    m.set('ldgxxty03', '三级/高级工（ 具备以下条件之一者 ） \n' +
        '（1）取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作５年（含）以上。 \n' +
        '（2）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。 \n' +
        '（3）具有大学专科本专业或相关专业毕业证书，并取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书） 后，累计从事本职业或相关职业工作２年（含）以上。 \n' +
        '（4）具有大学本科本专业或相关专业学历证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作 1 年（含）以上。 \n' +
        '（5）具有硕士研究生及以上本专业或相关专业学历证书（含尚未取得毕业证书的在校应届研究生毕业生）。');
    m.set('hg05', '1、具备以下条件之一者，可申报五级/初级工：\n' +
        '（1）累计从事本职业或相关职业工作1年（含）以上。\n' +
        '（2）本职业或相关职业学徒期满。');
    m.set('hg04', '2、具备以下条件之一者，可申报四级/中级工：\n' +
        '（1）取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。\n' +
        '（2）累计从事本职业或相关职业工作6年（含）以上。\n' +
        '（3）取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。');
    m.set('hg03', '3、具备以下条件之一者，可申报三级/高级工：\n' +
        '（1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作5年（含）以上。\n' +
        '（2）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。\n' +
        '（3）具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作2年（含）以上。');
    return m.get(obj);
}

let dhg05 = ['(1) 累计从事本职业工作１年( 含)以上。', '(2) 本职业学徒期满。'];
let dhg04 = ['(1) 取得本职业五级/ 初级工职业资格证书( 技能等级证书)后，累计从事本职业工作４年(含)以上。', '(2) 累计从事本职业工作６年(含)以上。', '(3) 取得技工学校本专业或相关专业毕业证书(含尚未取得毕业证书的在校应届毕业生)；' +
'或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ' +
'( 含尚未取得毕业证书的在校应届毕业生)。'
];
let dhg03 = ['(1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作５ 年( 含) 以上。',
    '(2) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；或取得本职业四级/ 中级工职业资格证书，并具有经评估论证、 以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 (含尚未取得毕业证书的在校应届毕业生)。',
    '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业工作２年( 含) 以上。'];

let dg05 = ['(1) 累计从事本职业工作１年( 含)以上。', '(2) 本职业学徒期满。'];
let dg04 = ['(1) 取得本职业五级/ 初级工职业资格证书( 技能等级证书)后，累计从事本职业工作４年(含)以上。',
    '(2) 累计从事本职业工作６年(含)以上。',
    '(3) 取得技工学校本专业或相关专业毕业证书( 含尚未取得毕业证书的在校应届毕业生)；或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。'];
let dg03 = ['(1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作５ 年( 含) 以上',
    '(2) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；' +
    '或取得本职业四级/ 中级工职业资格证书，并具有经评估论证、 以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 (含尚未取得毕业证书的在校应届毕业生)。',
    '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业工作２年( 含) 以上。',
    '注：本专业或相关专业: 数控机床装配与维修、机械设备装配与自动控制、制冷设备运用与维修、机电设备安装与维修、机电一体化、电气自动化设备安装与维修 、电梯工程技术、城市轨道交通车辆运用与检修 、煤矿电气设备维修、' +
    ' 工业机器人应用与维护、工业网络技术、机电技术应用、电气运行与控制、电气技术应用、纺织机电技术、铁道供电技术、农业电气化技术等专业。'];

    let qg05 = ['(1) 经本职业初级正规培训达规定标准学时数，并取得结业证书。', '(2) 本职业学徒期满。'];
let qg04 = ['(1) 取得本职业初级职业资格证书后，连续从事本职业工作 3 年以上，经本职业中级正规培训达规定标准学时数，并取得结业证书。', '(2) 取得本职业初级职业资格证书后，连续从事本职业工作 5 年以上。',
    '(3) 连续从事本职业工作 7 年以上。',
    '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。'];
let qg03 = ['(1) 取得本职业中级职业资格证书后，连续从事本职业工作 4 年以上，经本职业高级正规培训达规定标准学时数，并取得结业证书。',
    '(2) 取得本职业中级职业资格证书后，连续从事本职业工作 7 年以上。',
    '(3) 取得高级技工学校或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校或高级技工学校本职业 ( 专业 ) 毕业证书。',
    '(4) 大专以上本专业或相关专业毕业生取得本职业中级职业资格证书后, 连续从事本职业工作 2 年以上。'];
let yyy05 = ['(1)经本职业初级正规培训达规定标准学时数，并取得结业证书。', '（2）在本职业连续见习工作2年以上。', '（3）本职业学徒期满。'];
let yyy04 = ['(1)取得本职业初级职业资格证书后，连续从事本职业工作3年以上，经本职业中级正规培训达规定标准学时数，并取得结业证书。',
    '（2）取得本职业初级职业资格证书后，连续从事本职业工作5年以上。',
    '（3）连续从事本职业工作7年以上。',
    '（4）取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业(专业)毕业证书。'];
let yyy03 = ['(1)取得本职业中级职业资格证书后，连续从事本职业工作4年以上，经本职业高级正规培训达规定标准学时数，并取得结业证书。',
    '（2）取得本职业中级职业资格证书后，连续从事本职业工作6年以上。',
    '（3）取得高级技工学校或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业(专业)毕业证书。',
    '（4）取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生，连续从事本职业工作2年以上。'];

let byy05 = ['(1) 经本职业初级正规培训达规定标准学时数，并取得结业证书。',
    '(2) 本职业学徒期满。'];
let byy04 = ['(1) 取得本职业初级职业资格证书后，连续从事本职业工作 3 年以上，经本职业中级正规培训达规定标准学时数，并取得结业证书。',
    '(2) 取得本职业初级职业资格证书后，连续从事本职业工作 5 年以上。',
    '(3) 连续从事本职业工作 7 年以上。',
    '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。'];
let byy03 = ['(1) 取得本职业中级职业资格证书后，连续从事本职业工作 4 年以上，经本职业高级正规培训达规定标准学时数，并取得结业证书。',
    '(2) 取得本职业中级职业资格证书后，连续从事本职业工作 6 年以上。',
    '(3) 取得高级技工学校或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
    '(4) 取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生，连续从事本职业工作 2 年以上。'];
let ldgxxty04 = ['（1） 累计从事本职业或相关职业工作 4 年（含）以上。 ',
    '（2） 取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
    '（3）高等院校本专业或相关专业在校生。 '];
let ldgxxty03 = ['（1）取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作５年（含）以上。 ',
    '（2）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
    '（3）具有大学专科本专业或相关专业毕业证书，并取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书） 后，累计从事本职业或相关职业工作２年（含）以上。',
    '（4）具有大学本科本专业或相关专业学历证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作 1 年（含）以上。 ',
    '（5）具有硕士研究生及以上本专业或相关专业学历证书（含尚未取得毕业证书的在校应届研究生毕业生）。'];
let hg05 = ['（1）累计从事本职业或相关职业工作1年（含）以上。',
    '（2）本职业或相关职业学徒期满。'];
let hg04 = ['（1）取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
    '（2）累计从事本职业或相关职业工作6年（含）以上。',
    '（3）取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。'];
let hg03 = ['（1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作5年（含）以上。',
    '（2）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
    '（3）具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作2年（含）以上。'];

function get_worker_level_condition_selected(obj) {
    let m = new Map();
    m.set('dhg05', dhg05);
    m.set('dhg04', dhg04);
    m.set('dhg03', dhg03);

    m.set('dg05', dg05);
    m.set('dg04', dg04);
    m.set('dg03', dg03);
    m.set('qg05', qg05);
    m.set('qg04', qg04);
    m.set('qg03', qg03);
    m.set('yyy05', yyy05);
    m.set('yyy04', yyy04);
    m.set('yyy03', yyy03);
    m.set('byy05', byy05);
    m.set('byy04', byy04);
    m.set('byy03', byy03);
    m.set('ldgxxty04', ldgxxty04);
    m.set('ldgxxty03', ldgxxty03);
    m.set('hg05', hg05);
    m.set('hg04', hg04);
    m.set('hg03', hg03);
    return m.get(obj);
}
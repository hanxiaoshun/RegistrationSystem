/***
 * 检测申报资格名称以及职级匹配的各项数据
 */
function check_final() {
    let date = new Date();
    let year = date.getFullYear();

    //是否需要
    let has_qualification_class = $('.has_qualification');
    let graduation_status_class = $('.graduation_status');

    // let title_switch = {
    //     '1': "电工",
    //     '2': "焊工",
    //     '3': "钳工",
    //     '4': "育婴员",
    //     '5': "保育员",
    //     '6': "劳动关系协调员",
    //     '7': '防腐蚀工',
    //     '8': '有机合成工',
    //     '9': '工业废水处理工',
    //     '10': '无机化学反应生产工',
    //     '11': '固体废物处理工',
    // };
    // 获取申报的职业信息
    let select_worker = $("#declaration_of_occupation");
    let worker = select_worker.val();
    //获取级别
    let identification_level = $("#identification_level");
    let obj = identification_level.val();
    let worker_level = $(".worker_level_desc");
    let worker_level_desc_label = $(".worker_level_desc_label");
    let worker_level_content = $(".worker_level_desc_content");
    let worker_level_desc_content_textarea = $(".worker_level_desc_content_textarea");


    //职业年限
    let career_life_class = $(".career_life");
    //技术等级（原级别）
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


    //职业年限
    let career_life = $("#career_life");
    //技术等级（原级别）
    let primary_level = $("#primary_level");
    // 现持有职业资格证书编号(原证书编号)
    let original_certificate_number = $("#original_certificate_number");
    // 现有证件发证单位
    let issue_unit = $("#issue_unit");
    //现有职业资格证发证时间
    let issuance_time = $("#issuance_time");
    //从事本职业工作开始时间
    let start_the_work_of_this_occupation = $("#start_the_work_of_this_occupation");

    //=========================================================================================

    // 学历程度
    let education_degree = $("#education_degree");
    //毕业（应届）院校名称
    let school_name = $("#school_name");
    // 毕业时间(或即将毕业时间)
    let graduation_time = $("#graduation_time");
    //专业工种(或相关专业工种)
    let profession = $("#profession");
    //被授予毕业资格证书名称
    let diploma_granted = $("#diploma_granted");
    // 报名单位负责人
    let person_in_charge = $("#person_in_charge");

//value=================================================
    //职业年限
    let career_life_val = parseInt(career_life.val());
    //技术等级（原级别）
    let primary_level_val = parseInt(primary_level.val());
    // 现持有职业资格证书编号(原证书编号)
    let original_certificate_number_val = original_certificate_number.val();
    // 现有证件发证单位
    let issue_unit_val = issue_unit.val();
    //现有职业资格证发证时间
    let issuance_time_val = issuance_time.val();
    //从事本职业工作开始时间
    let start_the_work_of_this_occupation_val = start_the_work_of_this_occupation.val();
    let vars = start_the_work_of_this_occupation_val.split('-');
    let count_year = year - parseInt(vars[0]);
    //资格证书
    let certificate_photos_val = $("#certificate_photos").val();
    //=========================================================================================

    // 学历程度
    let education_degree_val = education_degree.val();
    //毕业（应届）院校名称
    let school_name_val = school_name.val();
    // 毕业时间(或即将毕业时间)
    let graduation_time_val = graduation_time.val();
    //专业工种(或相关专业工种)
    let profession_val = profession.val();
    //被授予毕业资格证书名称
    let diploma_granted_val = diploma_granted.val();
    // 报名单位负责人
    let person_in_charge_val = person_in_charge.val();
    // 毕业证书
    let diploma_certificate_photos_val = $("#diploma_certificate_photos").val();
    let title_level = {
        '1': "高级技师",
        '2': "技师",
        '3': "高级工",
        '4': "中级工",
        '5': "初级工"
    };

    if (worker.length === 0) {
        alert("请您在导航栏中选择所要申报的工种-如：电工");
    } else if (typeof obj === undefined || obj.toString() === '') {
        alert("请您选择申报-" + worker + "的等级");
    } else if (parseInt(obj) === 0) {
        alert("请您选择申报-" + worker + "的等级");
    } else if (person_in_charge_val.length < 2) {
        alert("请您正确填写报名单位负责人姓名！");
    } else if (career_life_val > count_year) {
        //如果所填写职业年限大于系统计算出来的年限
        alert("您的职业年限" + career_life_val + "年，与系统参考计算从事本职业工作开始时间年限" + count_year + "年 所得结果不一致，请确认信息再核验！");
    } else if (worker === "电工") {
        if (parseInt(obj) === 1) {
            // 高级技师
            if (primary_level_val === 2) {
                if (count_year >= 4) {
                    // # 职业年限大于等于四年
                    if (original_certificate_number_val.length > 0) {
                        if (issue_unit_val.length > 0) {
                            if (issuance_time_val.length > 0) {
                                if (certificate_photos_val.length >= 0) {
                                    alert("恭喜通过初步核验，请继续填报！");
                                    $(".more_info").show();
                                } else {
                                    alert('申报-' + worker + '-' + title_level[obj.toString()] + "的原级别 资格证书图片 上传失败，请重试或联系报名单位负责人！");
                                    return false;
                                }
                            } else {
                                alert('申报-' + worker + '-' + title_level[obj.toString()] + "的原级别资格证书发放 时间 获取失败，请重新填写完整！");
                                return false;
                            }
                        } else {
                            alert('申报-' + worker + '-' + title_level[obj.toString()] + "的原级别资格证书 发放单位 获取失败，请重新填写完整！");
                            return false;
                        }
                    } else {
                        alert('申报-' + worker + '-' + title_level[obj.toString()] + "的原级别资格证书编号获取失败，请重新填写完整！");
                        return false;
                    }
                } else {
                    alert('申报-' + worker + '-' + title_level[obj.toString()] + "的从事本职业工作年限不足，请仔细阅读本工种申报本级别的报名条件！");
                    return false;
                }
            } else {
                alert('申报-' + worker + '-' + title_level[obj.toString()] + "的原资格证书级别未选择或不符合规范，请重新选择");
                primary_level.css('border', '1px;');
                primary_level.css('',);
                primary_level.focus();
                // return false;
            }

        } else if (parseInt(obj) === 2) {
            // 中级技师
            console.log();
        } else if (parseInt(obj) === 3) {
            // 高级工
            // 中级技师
            console.log();
        } else if (parseInt(obj) === 4) {
            // 中级工
            // 中级技师
            console.log();
        } else if (parseInt(obj) === 5) {
            // 初级工
            // 中级技师
            console.log();
        } else {

        }
    } else if (worker === "焊工") {
        if (parseInt(obj) === 1) {
            // 高级技师
           // 中级技师
            console.log();
        } else if (parseInt(obj) === 2) {
            // 中级技师
            // 中级技师
            console.log();
        } else if (parseInt(obj) === 3) {
            // 高级工
            // 中级技师
            console.log();
        } else if (parseInt(obj) === 4) {
            // 中级工
            // 中级技师
            console.log();
        } else if (parseInt(obj) === 5) {
            // 初级工
            // 中级技师
            console.log();
        } else {
            // 中级技师
            console.log();
        }
    } else if (worker === "钳工") {
        if (parseInt(obj) === 1) {
            // 高级技师
            // 中级技师
            console.log();
        } else if (parseInt(obj) === 2) {
            // 中级技师
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('qg02');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 3) {
            // 高级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('qg03');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 4) {
            // 中级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('qg04');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 5) {
            // 初级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('qg05');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else {
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = "";
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val("暂无相关介绍信息！！！");
        }
    } else if (worker === "育婴员") {
        if (parseInt(obj) === 1) {
            // 高级技师
            alert("育婴员无一级高级技师资格等级申报事宜");
        } else if (parseInt(obj) === 2) {
            // 中级技师
            alert("育婴员无二级技师资格等级申报事宜");
        } else if (parseInt(obj) === 3) {
            // 高级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('yyy03');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 4) {
            // 中级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('yyy04');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 5) {
            // 初级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('yyy05');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else {
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = "";
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val("暂无相关介绍信息！！！");
        }
    } else if (worker === "保育员") {
        if (parseInt(obj) === 1) {
            // 高级技师
            alert("保育员无一级高级技师资格等级申报事宜");
        } else if (parseInt(obj) === 2) {
            // 中级技师
            alert("保育员无二级技师资格等级申报事宜");
        } else if (parseInt(obj) === 3) {
            // 高级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('byy03');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 4) {
            // 中级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('byy04');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 5) {
            // 初级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('byy05');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else {
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = "";
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val("暂无相关介绍信息！！！");
        }
    } else if (worker === "劳动关系协调员") {
        if (parseInt(obj) === 1) {
            // 高级技师
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('ldgxxty01');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 2) {
            // 中级技师
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('ldgxxty02');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 3) {
            // 高级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('ldgxxty03');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 4) {
            // 中级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('ldgxxty04');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 5) {
            // 初级工
            alert("劳动关系协调员无五级初级工资格等级申报事宜");
        } else {
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = "";
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val("暂无相关介绍信息！！！");
        }
    } else if (worker === "防腐蚀工") {
        if (parseInt(obj) === 1) {
            // 高级技师
            alert(worker + " 无一级高级技师资格等级申报事宜");
        } else if (parseInt(obj) === 2) {
            // 中级技师
            alert(worker + " 无二级技师资格等级申报事宜");
        } else if (parseInt(obj) === 3) {
            // 高级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg03');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 4) {
            // 中级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg04');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 5) {
            // 初级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg05');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else {
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = "";
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val("暂无相关介绍信息！！！");
        }
    } else if (worker === "有机合成工") {
        if (parseInt(obj) === 1) {
            // 高级技师
            alert(worker + " 无一级高级技师资格等级申报事宜");
        } else if (parseInt(obj) === 2) {
            // 中级技师
            alert(worker + " 无二级技师资格等级申报事宜");
        } else if (parseInt(obj) === 3) {
            // 高级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg03');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 4) {
            // 中级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg04');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 5) {
            // 初级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg05');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else {
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = "";
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val("暂无相关介绍信息！！！");
        }
    } else if (worker === "工业废水处理工") {
        if (parseInt(obj) === 1) {
            // 高级技师
            alert(worker + " 无一级高级技师资格等级申报事宜");
        } else if (parseInt(obj) === 2) {
            // 中级技师
            alert(worker + " 无二级技师资格等级申报事宜");
        } else if (parseInt(obj) === 3) {
            // 高级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg03');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 4) {
            // 中级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg04');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 5) {
            // 初级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg05');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else {
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = "";
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val("暂无相关介绍信息！！！");
        }
    } else if (worker === "无机化学反应生产工") {

        if (parseInt(obj) === 1) {
            // 高级技师
            alert(worker + " 无一级高级技师资格等级申报事宜");
        } else if (parseInt(obj) === 2) {
            // 中级技师
            alert(worker + " 无二级技师资格等级申报事宜");
        } else if (parseInt(obj) === 3) {
            // 高级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg03');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 4) {
            // 中级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg04');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 5) {
            // 初级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg05');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else {
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = "";
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val("暂无相关介绍信息！！！");
        }
    } else if (worker === "固体废物处理工") {
        if (parseInt(obj) === 1) {
            // 高级技师
            alert(worker + " 无一级高级技师资格等级申报事宜");
        } else if (parseInt(obj) === 2) {
            // 中级技师
            alert(worker + " 无二级技师资格等级申报事宜");
        } else if (parseInt(obj) === 3) {
            // 高级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg03');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 4) {
            // 中级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg04');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else if (parseInt(obj) === 5) {
            // 初级工
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = get_worker_level_info('hg05');
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val(worker_level_desc_content);
        } else {
            worker_level.show();
            worker_level_content.show();
            let worker_level_desc = '申报-' + worker + '-' + title_level[obj.toString()] + "条件说明";
            let worker_level_desc_content = "";
            worker_level_desc_label.text(worker_level_desc);
            worker_level_desc_content_textarea.val("暂无相关介绍信息！！！");
        }
    } else {
        worker_level.hide();
        worker_level_content.hide();
    }

}

function get_worker_level_info(obj) {
    let m = new Map();
    m.set('hg05', '五级/初级工 ( 具备以下条件之一者 )\n' +
        '(1) 累计从事本职业工作１年( 含)以上。\n' +
        '(2) 本职业学徒期满。');
    m.set('hg04', '四级/中级工( 具备以下条件之一者 )\n' +
        '(1) 取得本职业五级/ 初级工职业资格证书( 技能等级证书)后，累计从事本职业工作４年(含)以上。\n' +
        '(2) 累计从事本职业工作６年(含)以上。\n' +
        '(3) 取得技工学校本专业或相关专业毕业证书( 含尚未取得毕业证书的在校应届毕业生)；' +
        '或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ' +
        '( 含尚未取得毕业证书的在校应届毕业生)。注：相关专业：' +
        '焊接加工、焊接技术应用、金属热加工（焊接）、焊接技术与自动化、焊接技术与工程。');
    m.set('hg03', '三级/高级工( 具备以下条件之一者 )\n' +
        '(1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作５ 年( 含) 以上。\n' +
        '(2) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；' +
        '或取得本职业四级/ 中级工职业资格证书，并具有经评估论证、 以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 (含尚未取得毕业证书的在校应届毕业生)。 \n' +
        '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业工作２年( 含) 以上。');
    m.set('hg02', '二级/技师( 具备以下条件之一者 )\n' +
        '(1) 取得本职业三级/ 高级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作４年( 含) 以上。\n' +
        '(2) 取得本职业三级/ 高级工职业资格证书 ( 技能等级证书) 的高级技工学校、技师学院毕业生，累计从事本职业工作３年( 含) 以上；或取得本职业预备技师证书的技师学院毕业生，累计从事本职业工作２年( 含) 以上。');
    m.set('hg01', '一级/高级技师\n' +
        '取得本职业二级/ 技师职业资格证书 ( 技能等级证书) 后，累计从事本职业工作４年 ( 含) 以上。');
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
    m.set('dg02', '二级/技师( 具备以下条件之一者 )\n' +
        '(1) 取得本职业三级/ 高级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作４年( 含) 以上。\n' +
        '(2) 取得本职业三级/ 高级工职业资格证书 ( 技能等级证书) 的高级技工学校、技师学院毕业生，累计从事本职业工作３年( 含) 以上；' +
        '或取得本职业预备技师证书的技师学院毕业生，累计从事本职业工作２年( 含) 以上。');
    m.set('dg01', '一级/高级技师\n' +
        '取得本职业二级/ 技师职业资格证书 ( 技能等级证书) 后，累计从事本职业工作４年 ( 含) 以上。');
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
    m.set('qg02', '技师 ( 具备下列条件之一者 )\n' +
        '(1) 取得本职业高级职业资格证书后，连续从事本职业工作 5 年以上，经本职业技师正规培训达规定标准学时数，并取得结业证书。\n' +
        '(2) 取得本职业高级职业资格证书后，连续从事本职业工作 8 年以上。\n' +
        '(3) 高级技工学校本职业（专业）毕业生和大专以上本专业或相关专业毕业生取得本职业高级职业资格证书后，连续从事本职业工作满 2 年。');
    m.set('qg01', '高级技师 ( 具备下列条件之一者 )\n' +
        '(1) 取得本职业技师职业资格证书后，连续从事本职业工作 3 年以上，经本职业高级技师正规培训达规定标准学时数，并取得结业证书。\n' +
        '(2) 取得本职业技师职业资格证书后，连续从事本职业工作 5 年以上。');
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
    m.set('ldgxxty02', '二级/技师（具备以下条件之一者） \n' +
        '（1）取得本职业或相关职业三级/高级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作４年（含）以上。 \n' +
        '（2）取得本职业或相关职业三级/高级工职业资格证书（技能等级证书）的高级技工学校、技师学院毕业生，累计从事本职业或相关职业工作３年（含）以上；或取得本职业或相关职业预备技师证书的技师学院毕业生，累计从事本职业或相关职业工作２年（含）以上。 \n' +
        '（3）具有大学本科本专业或相关专业学历证书，并取得本职业或相关职业三级/高级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作 2 年（含）以上。 \n' +
        '（4）具有硕士研究生本专业或相关专业学历证书，并取得本职业或相关职业三级/高级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作 1 年（含）以上。 \n' +
        '（5）具有博士研究生本专业或相关专业学历证书，累计从事本职业或相关职业工作 2 年（含）以上。');
    m.set('ldgxxty01', '一级/高级技师 \n' +
        '取得本职业或相关职业二级/ 技师职业资格证书（技能等级 证书）后，累计从事本职业或相关职业工作４年（含）以上。 \n' +
        '注：\n' +
        '1、相关职业：人力资源管理、劳动保障事务处理、社会工作等职业。 \n' +
        '2、相关专业：劳动与社会保障、劳动经济学、人力资源管理、工商企业管理、法学、社会学等专业。 \n' +
        '3、相关职业资格证书（技能等级证书）:企业人力资源管理师、劳动保障协理员、劳动保障专理员、社会工作者等与劳动关系协调员职业功能具有关联性的职业资格证书。 ');
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

//获取当前时间，格式YYYY-MM-DD
function getNowFormatDate() {
    let date = new Date();
    let seperator1 = "-";
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    return year + seperator1 + month + seperator1 + strDate;
}
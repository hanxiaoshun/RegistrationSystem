/**
 *   检测申报资格名称以及职级
 * @param condition_level
 */
function check_identification_level(condition_level) {
    // 级别按钮
    let identification_level = $("#identification_level");
    let worker_level = $(".worker_level_desc");
    let worker_level_desc_label = $(".worker_level_desc_label");
    let worker_level_content = $(".worker_level_desc_content");
    let worker_level_desc_content_textarea = $(
        ".worker_level_desc_content_textarea"
    );
    let course_hours_class = $(".course_hours");
    course_hours_class.hide();
    //是否需要
    let has_qualification_class = $(".has_qualification");
    let graduation_status_class = $(".graduation_status");
    let condition_selected_class = $(".condition_selected");
    let profession_class = $(".profession");
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
    let start_the_work_of_this_occupation_class = $(
        ".start_the_work_of_this_occupation"
    );
    // 职业资格证图片上传
    let certificate_photos_class = $(".certificate_photos");
    //=========================================================================================

    // 学历程度
    let education_degree_class = $(".education_degree");
    //毕业（应届）院校名称
    let school_name_class = $(".school_name");
    // 毕业时间(或即将毕业时间)
    let graduation_time_class = $(".graduation_time");
    //专业工种(或相关专业工种)

    let major = $(".major");
    //被授予毕业资格证书名称
    let diploma_granted_class = $(".diploma_granted");
    // 报名单位负责人
    let person_in_charge_class = $(".person_in_charge");
    // 毕业证图片上传
    let diploma_certificate_photos_class = $(".diploma_certificate_photos");
    let title_level = {
        "3": "高级（三级）",
        "4": "中级（四级）",
        "5": "初级（五级）",
    };
    // 获取申报的职业信息
    let skill_name = $("#declaration_of_occupation").val();
    let skill_id = $("#id_skill_id").val();
    console.log(skill_id, condition_level);
    if (parseInt(condition_level) === 0) {
        alert("请您选择申报-" + skill_name + "的等级");
    } else {
        let form_inputs = $("#add-student-info-id input");
        for (let i = 0; i < form_inputs.length; i++) {
            form_inputs[i].required = false;
            console.log(form_inputs[i].required);
        }
        $("#identification-level").val(condition_level);
        $("#identification-level-label").html(title_level[condition_level]);
        skill_condition(skill_id, condition_level);
    }
    //原级别
}

/**
 * 生成条件选项
 * @param {*} skill_id
 * @param {*} condition_level
 */
function skill_condition(skill_id, condition_level) {
    console.log(skill_id, condition_level);
    let url = "/report/report_condition_info/";
    // let form = document.querySelector("#report-condition-info-id");
    let form_data = new FormData();
    // form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    form_data.append("condition_level", condition_level.toString());
    form_data.append("skill_id", skill_id.toString());
    console.log(form_data);
    $.ajax({
        url: url,
        dataType: "json",
        type: "get",
        data: {
            skill_id: skill_id,
            condition_level: condition_level,
        },
        success: function(res) {
            if (res.status == false) {
                alert(res.message);
            } else {
                // conditionlist = JSON.parse(res.data);
                let condition_selected = "";
                console.log(res);
                var data_json = JSON.parse(res.data);
                conditionlist = data_json;
                $.each(data_json, function(i, n) {
                    console.log(n.condition_id);
                    var id_condition_radio = n.condition_id.toString() + "_condition_radio";
                    var id_str = n.condition_id.toString();
                    condition_selected =
                        condition_selected +
                        "<input type='radio' required='required' name='condition_selected'" +
                        " value=" +
                        id_str +
                        " id=" +
                        id_condition_radio +
                        " onclick='condition_controller_enhance(this.value, \"add\");'/>" +
                        "<label for='" +
                        id_condition_radio +
                        "' style='color:white'><span>" +
                        n.condition_name +
                        "</span></label>" +
                        "<hr>";
                });
                let condition_selected_class = $(".condition_selected");
                condition_selected_class.empty("");
                condition_selected_class.append(condition_selected);
                console.log(res); //在console中查看数据
            }
        },
        error: function() {
            alert("failed!");
        },
    });
}



/**
 * 清空输入框
 * 
 */
function clear_input_label() {
    $("#apprentice_start").val("");
    $("#apprentice_end").val("");
    $("#apprentice_year").val("");
    $("#start_the_work_of_this_occupation").val("");
    $("#career_life").val("");
    $("#career_life_time").val("");
    $("#original_certificate_number").val("");
    $("#issue_unit").val("");
    $("#issuance_time").val("");
    $("#original_certificate_worker_year").val("");
    $("#from_certificate_need_year").val("");
    $("#school_name").val("");
    $("#major").val("");
    $("#course_hours").val("");
    $("#graduation_time").val("");
    $("#certificate_photos").val("");
    $("#diploma_certificate_photos").val("");

    $("#career_life_label_value").text("");
    $("#apprentice_year_label").text("");
    $("#apprentice_month_label").text("");
    $("#original_certificate_worker_year_value").text("");
    $("#career_life_label").text("");
    $("#original_certificate_worker_year_label").text("");
}
/**
 * 按照条件显示输入框
 * @param condition_id_str 填报选项
 * @param status 条件生成状态
 */
function condition_controller_enhance(condition_id_str, status) {
    if (status === "add") {
        clear_input_label();
    } else {
        // 重新获取一下条列表
        console.log("修改不需要清空数据");
    }

    let form_inputs = $("#add-student-info-id input");
    for (let i = 0; i < form_inputs.length; i++) {
        form_inputs[i].required = false;
        // form_inputs[i].value = "";
    }

    $("#condition_selected_value").val(condition_id_str);
    let apprentice_class = $(".apprentice");

    let apprentice_start_class = $(".apprentice_start").hide();
    $(".apprentice_end").hide();
    //========================================================================================
    //是否需要
    let qualification_class = $(".has_qualification");
    let graduation_status_class = $(".graduation_status");
    let condition_selected_class = $(".condition_selected");
    //职业年限
    let career_life_class = $(".career_life");
    //从事本职业工作开始时间
    let start_the_work_of_this_occupation_class = $(
        ".start_the_work_of_this_occupation"
    );
    //术等级（原级别）
    let primary_level_class = $(".primary_level");
    // 现持有职业资格证书编号(原证书编号)
    let original_certificate_number_class = $(".original_certificate_number");
    // 现有证件发证单位
    let issue_unit_class = $(".issue_unit");
    //现有职业资格证发证时间
    let issuance_time_class = $(".issuance_time");

    // 职业资格证图片上传
    let certificate_photos_class = $(".certificate_photos");
    //=========================================================================================

    // // 学历程度
    //     let education_degree_class = $(".education_degree");
    //毕业（应届）院校名称
    let school_name_class = $(".school_name");
    // 毕业时间(或即将毕业时间)
    let graduation_time_class = $(".graduation_time");
    //专业工种(或相关专业工种)
    let profession_class = $(".profession");

    //被授予毕业资格证书名称
    let diploma_granted_class = $(".diploma_granted");
    // 毕业证图片上传
    let diploma_certificate_photos_class = $(".diploma_certificate_photos");

    apprentice_class.hide();
    career_life_class.hide();
    start_the_work_of_this_occupation_class.hide();

    graduation_status_class.hide();
    // 职业年限情况
    career_life_class.hide();
    profession_class.hide();
    start_the_work_of_this_occupation_class.hide();
    $(".career_life_time").hide();
    $(".course_hours").hide();
    //有关证书情况
    primary_level_class.hide();
    original_certificate_number_class.hide();
    issue_unit_class.hide();
    issuance_time_class.hide();
    $(".from_certificate_need_year").hide();
    $(".original_certificate_worker_time").hide();

    certificate_photos_class.hide();
    // 院校毕业证书情况
    $(".education_degree_form").hide();
    school_name_class.hide();
    graduation_time_class.hide();
    $(".graduation_worker_time").hide();
    $(".strict_status").hide();
    $(".major").hide();

    diploma_certificate_photos_class.hide();

    console.log(condition_id_str);
    console.log(conditionlist);
    // apprentice_status: "1" 学徒信息
    // certificate_photos_status: "1"资格证件照片
    // condition_for_skill_id: 3
    // condition_id: 8
    // condition_level: "4"
    // condition_name: "(3) 取得技工学校本专业或相关专业毕业证书( 含尚未取得毕业证书的在校应届毕业生)；或取得经评估论"
    // create_time: "2020-04-14"
    // diploma_certificate_photos_status: "1"毕业证件照片
    // explain: "(3) 取得技工学校本专业或相关专业毕业证书( 含尚未取得毕业证书的在校应届毕业生)；"
    // graduation_time_status: "1"毕业(结业)信息
    // original_certificate_info_status: "1"原证书详细信息
    // original_certificate_worker_time_requirement: 0 获得现有资格证书后工作年限要求
    // original_certificate_worker_time_status: "1"获得现有资格证书后工作年限
    // primary_level_status: "1"原证书级别
    // record_status: "1"
    // school_info_status: "1"
    // user_operator_id: 1
    // work_of_this_occupation_requirement: 0 从事本工作时间要求
    // work_of_this_occupation_status: "1" 从事本工作时间
    $.each(conditionlist, function(i, n) {
        if (n.condition_id === parseInt(condition_id_str)) {
            if (status == "update") {
                let condition_selected_class = $(".condition_selected_update_class");
                var condition_selected =
                    "<label style='color:red'>备注：<label><br> <label style='color:yellow'>" +
                    n.explain_condition +
                    "</label>";
                condition_selected_class.append(condition_selected);
            } else {
                let condition_selected_class = $(".condition_selected_explain");
                var condition_selected =
                    "<label style='color:yellow'>" +
                    n.explain_condition +
                    "</label>";
                if (n.explain_condition.length > 0) {
                    condition_selected_class.html(condition_selected);
                } else {
                    condition_selected_class.html('无');
                }

            }

            // 从事本工作时间
            if (n.work_of_this_occupation_status === "1") {
                career_life_time(n.work_of_this_occupation_requirement);
            } else {
                career_life_time();
            }
            // 学徒期
            if (n.apprentice_status === "1") {
                apprentice_check(true);
            } else {
                apprentice_check(false);
            }
            // 证书级及信息
            if (n.primary_level_status === "1") {
                check_has_qualification(
                    1,
                    parseInt(n.primary_level_requirement),
                    n.original_certificate_worker_time_requirement
                );
            } else {
                check_has_qualification(2);
            }
            // 毕业信息
            if (n.graduation_time_status === "1") {
                if (n.graduation_lowest === "1") {
                    if (n.graduation_is_Fresh === "1") {
                        check_graduation_status(
                            1,
                            parseInt(n.graduation_low_requirement),
                            true,
                            true,
                            parseInt(n.graduation_extra_two),
                            parseInt(n.graduation_extra_three)
                        );
                    } else {
                        check_graduation_status(
                            1,
                            parseInt(n.graduation_low_requirement),
                            true,
                            false,
                            parseInt(n.graduation_extra_two),
                            parseInt(n.graduation_extra_three)
                        );
                    }
                } else {
                    if (n.graduation_is_Fresh === "1") {
                        check_graduation_status(
                            1,
                            parseInt(n.graduation_low_requirement),
                            false,
                            true,
                            parseInt(n.graduation_extra_two),
                            parseInt(n.graduation_extra_three)
                        );
                    } else {
                        check_graduation_status(
                            1,
                            parseInt(n.graduation_low_requirement),
                            false,
                            false,
                            parseInt(n.graduation_extra_two),
                            parseInt(n.graduation_extra_three)
                        );
                    }
                }
            } else {
                check_graduation_status(2);
            }
        }
    });

    // check_graduation_status(1, 3, true, false); //===============================

    // career_life_time(1);
    // apprentice_check(false);
    // check_has_qualification(1);
    // check_graduation_status(1, 3, true, false); //===============================
}


/**
 * 按照条件显示输入框
 * @param condition_id_str 填报选项
 * @param status 条件生成状态
 */
function condition_controller_update(condition_id_str, status) {
    let form_inputs = $("#add-student-info-id input");
    for (let i = 0; i < form_inputs.length; i++) {
        form_inputs[i].required = false;
        // form_inputs[i].value = "";
    }

    $("#condition_selected_value").val(condition_id_str);
    let apprentice_class = $(".apprentice");

    let apprentice_start_class = $(".apprentice_start").hide();
    $(".apprentice_end").hide();
    //========================================================================================
    //是否需要
    let qualification_class = $(".has_qualification");
    let graduation_status_class = $(".graduation_status");
    let condition_selected_class = $(".condition_selected");
    //职业年限
    let career_life_class = $(".career_life");
    //从事本职业工作开始时间
    let start_the_work_of_this_occupation_class = $(
        ".start_the_work_of_this_occupation"
    );
    //术等级（原级别）
    let primary_level_class = $(".primary_level");
    // 现持有职业资格证书编号(原证书编号)
    let original_certificate_number_class = $(".original_certificate_number");
    // 现有证件发证单位
    let issue_unit_class = $(".issue_unit");
    //现有职业资格证发证时间
    let issuance_time_class = $(".issuance_time");

    // 职业资格证图片上传
    let certificate_photos_class = $(".certificate_photos");
    //=========================================================================================

    // // 学历程度
    //     let education_degree_class = $(".education_degree");
    //毕业（应届）院校名称
    let school_name_class = $(".school_name");
    // 毕业时间(或即将毕业时间)
    let graduation_time_class = $(".graduation_time");
    //专业工种(或相关专业工种)
    let profession_class = $(".profession");

    //被授予毕业资格证书名称
    let diploma_granted_class = $(".diploma_granted");
    // 毕业证图片上传
    let diploma_certificate_photos_class = $(".diploma_certificate_photos");

    apprentice_class.hide();
    career_life_class.hide();
    start_the_work_of_this_occupation_class.hide();

    graduation_status_class.hide();
    // 职业年限情况
    career_life_class.hide();
    profession_class.hide();
    start_the_work_of_this_occupation_class.hide();
    $(".career_life_time").hide();
    $(".course_hours").hide();
    //有关证书情况
    primary_level_class.hide();
    original_certificate_number_class.hide();
    issue_unit_class.hide();
    issuance_time_class.hide();
    $(".from_certificate_need_year").hide();
    $(".original_certificate_worker_time").hide();

    certificate_photos_class.hide();
    // 院校毕业证书情况
    $(".education_degree_form").hide();
    school_name_class.hide();
    graduation_time_class.hide();
    $(".graduation_worker_time").hide();
    $(".strict_status").hide();
    $(".major").hide();
    diploma_certificate_photos_class.hide();
    let url = "/report/report_condition_info/";
    $.ajax({
        url: url,
        dataType: "json",
        type: "get",
        data: {
            condition_id: condition_id_str,
        },
        success: function(res) {
            var data_json = JSON.parse(res.data);
            $.each(data_json, function(i, n) {
                if (n.condition_id === parseInt(condition_id_str)) {

                    let condition_selected_class = $(".condition_selected_explain_update");
                    var condition_selected =
                        "<label style='color:yellow'>" +
                        n.explain_condition +
                        "</label>";
                    if (n.explain_condition.length > 0) {
                        condition_selected_class.html(condition_selected);
                    } else {
                        condition_selected_class.html('无');
                    }


                    // 从事本工作时间
                    if (n.work_of_this_occupation_status === "1") {
                        career_life_time(n.work_of_this_occupation_requirement);
                    } else {
                        career_life_time();
                    }
                    // 学徒期
                    if (n.apprentice_status === "1") {
                        apprentice_check(true);
                    } else {
                        apprentice_check(false);
                    }
                    // 证书级及信息
                    if (n.primary_level_status === "1") {
                        alert(n.primary_level_requirement);
                        check_has_qualification(
                            1,
                            parseInt(n.primary_level_requirement),
                            n.original_certificate_worker_time_requirement
                        );
                    } else {
                        check_has_qualification(2);
                    }
                    // 毕业信息
                    if (n.graduation_time_status === "1") {
                        if (n.graduation_lowest === "1") {
                            if (n.graduation_is_Fresh === "1") {
                                check_graduation_status(
                                    1,
                                    parseInt(n.graduation_low_requirement),
                                    true,
                                    true,
                                    parseInt(n.graduation_extra_two),
                                    parseInt(n.graduation_extra_three)
                                );
                            } else {
                                check_graduation_status(
                                    1,
                                    parseInt(n.graduation_low_requirement),
                                    true,
                                    false,
                                    parseInt(n.graduation_extra_two),
                                    parseInt(n.graduation_extra_three)
                                );
                            }
                        } else {
                            if (n.graduation_is_Fresh === "1") {
                                check_graduation_status(
                                    1,
                                    parseInt(n.graduation_low_requirement),
                                    false,
                                    true,
                                    parseInt(n.graduation_extra_two),
                                    parseInt(n.graduation_extra_three)
                                );
                            } else {
                                check_graduation_status(
                                    1,
                                    parseInt(n.graduation_low_requirement),
                                    false,
                                    false,
                                    parseInt(n.graduation_extra_two),
                                    parseInt(n.graduation_extra_three)
                                );
                            }
                        }
                    } else {
                        check_graduation_status(2);
                    }
                }
            });
        },
        error: function() {
            alert("failed!");
        },
    });
    // check_graduation_status(1, 3, true, false); //===============================

    // career_life_time(1);
    // apprentice_check(false);
    // check_has_qualification(1);
    // check_graduation_status(1, 3, true, false); //===============================
}
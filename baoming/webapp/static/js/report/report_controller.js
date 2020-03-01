/**
 * 有无资格证书
 */
function check_has_qualification(obj, primary_level, need_year, relevant_occupations) {
    /**
     * 1,有
     * 2,无
     */

    if (parseInt(obj) === 1) {
        $("#condition-a").val("condition-a");
        $("#condition-a-update").val("condition-b-update");
        //有关证书情况
        $('.primary_level').show();
        $('.original_certificate_number').show();
        $('.issue_unit').show();
        $('.issuance_time').show();
        $('.from_certificate_need_year').hide();
        $('.original_certificate_worker_time').show();
        $('.certificate_photos').show();
        $('.former_occupation').show();

        let primary_level_id = $('#primary_level');
        primary_level_id.val(primary_level);
        let primary_level_value = $("#primary_level_value");
        if (primary_level === 4) {
            primary_level_value.text("_中级_");
            // $('.original_certificate_worker_time').hide()
        } else if (primary_level === 5) {
            primary_level_value.text("_初级_");
        }


        $('#former_occupation').attr("required", "required");
        $('#original_certificate_number').attr("required", "required");
        $('#issue_unit').attr("required", "required");
        $('#issuance_time').attr("required", "required");
        $('#original_certificate_worker_time').attr("required", "required");
        if (typeof need_year === "undefined") {
            $("#from_certificate_need_year").val(0);
        } else {
            $("#from_certificate_need_year").val(need_year);
        }

    } else if (parseInt(obj) === 2) {
        // 取消掉原级别项目
        let primary_level_id = $('#primary_level');
        primary_level_id.val("");
        let primary_level_value = $("#primary_level_value");
        primary_level_value.text("");


        $("#condition-a").val("");
        $("#condition-a-update").val("");
        // 如果没有证件，那么只显示职业生涯
        $('.primary_level').hide();
        $('.former_occupation').hide();
        $('.original_certificate_number').hide();
        $('.issue_unit').hide();
        $('.issuance_time').hide();
        $('.original_certificate_worker_time').hide();
        $('.certificate_photos').hide();
        $('.from_certificate_need_year').hide();

        let original_certificate_number = $('#original_certificate_number');
        let issue_unit = $('#issue_unit');
        let issuance_time = $('#issuance_time');
        let original_certificate_worker_time = $('#original_certificate_worker_time');
        let original_certificate_worker_year = $('#original_certificate_worker_year');
        let former_occupation = $('#former_occupation');
        former_occupation.removeAttr("required");
        former_occupation.val("");

        original_certificate_worker_year.removeAttr("required");
        original_certificate_number.removeAttr("required");
        issue_unit.removeAttr("required");
        issuance_time.removeAttr("required");
        original_certificate_worker_time.removeAttr("required");

        $("#certificate_photos").val("");
        original_certificate_number.val("");
        issue_unit.val("");
        issuance_time.val("");
        original_certificate_worker_time.val("");
        original_certificate_worker_year.val("");
    } else {
        let primary_level_id = $('#primary_level');
        primary_level_id.val("");
        let primary_level_value = $("#primary_level_value");
        primary_level_value.text("");

        $("#condition-a-update").val("condition-b-update");
        $("#condition-a").val("condition-b");
        $('.primary_level').hide();
        $('.former_occupation').hide();
        $('.original_certificate_number').hide();
        $('.issue_unit').hide();
        $('.issuance_time').hide();
        $('.original_certificate_worker_time').hide();
        $('.certificate_photos').hide();
        $('.from_certificate_need_year').hide();
        let original_certificate_worker_year = $('#original_certificate_worker_year');
        original_certificate_worker_year.removeAttr("required");

        let original_certificate_number = $('#original_certificate_number');
        let issue_unit = $('#issue_unit');
        let issuance_time = $('#issuance_time');
        let original_certificate_worker_time = $('#original_certificate_worker_time');

        let former_occupation = $('#former_occupation');
        former_occupation.removeAttr("required");
        former_occupation.val("");

        original_certificate_worker_year.val("");
        $("#certificate_photos").val("");
        original_certificate_number.removeAttr("required");
        issue_unit.removeAttr("required");
        issuance_time.removeAttr("required");
        original_certificate_worker_time.removeAttr("required");

        original_certificate_number.val("");
        issue_unit.val("");
        issuance_time.val("");
        original_certificate_worker_time.val("");
        alert("尚未选择有无资格证件，请选择");
        this.focus();
    }
}

/**
 * 是否毕业
 */
function check_graduation_status(obj, graduation_status, more_status, strict, two, thrid) {

    $('.strict_status').hide();
    $("#graduation_result_0").removeAttr("checked");
    $("#graduation_result_1").removeAttr("checked");
    $('#diploma_certificate_photos').removeAttr('required');
    let graduation_status_id = $("#graduation_status");
    graduation_status_id.removeAttr('data-strict');

    if (strict) {
        graduation_status_id.attr('data-strict', "true");
        $("#condition-b").val("condition-b");
        $("#condition-b-update").val("condition-b-update");

    } else {
        graduation_status_id.attr('data-strict', "false");
    }
    let selects = "<select class='form-select' style=\"font-size:10px;width: 250px\" title=\"毕业状态\"\n" +
        "                            id=\"graduation_status\">\n" +
        "                        <option value=\"0\">---请选择---</option>\n" +
        "                        <option value=\"1\">-初级中学-</option>\n" +
        "                        <option value=\"2\">-技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-</option>\n" +
        "                        <option value=\"3\">-中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-</option>\n" +
        "                        <option value=\"4\">-高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）-</option>\n" +
        "                        <option value=\"5\">-高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-</option>\n" +
        "                        <option value=\"6\">-大专及以上本专业或相关专业毕业证书-</option>\n" +
        "                        <option value=\"7\">-大学本科本专业或相关专业毕业证书-</option>\n" +
        "                        <option value=\"8\">-硕士研究生及以上本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-</option>\n" +
        "                        <option value=\"9\">-本职业初级正规培训-</option>\n" +
        "                        <option value=\"10\">-本职业中级正规培训结业证书-</option>\n" +
        "                        <option value=\"11\">-本职业高级正规培训结业证书-</option>\n" +
        "                    </select>";

    let options = ['---请选择---',
        '-初级中学-',
        '-技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-',
        '-中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-',
        '-高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）-',
        '-高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-',
        '-大专及以上本专业或相关专业毕业证书-',
        '-大学本科本专业或相关专业毕业证书-',
        '-硕士研究生及以上本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）-',
        '-本职业初级正规培训-',
        '-本职业中级正规培训结业证书-',
        '-本职业高级正规培训结业证书-'];
    /**
     * 1,毕业
     * 2,应届生
     */
    let education_degree_form = $('#education_degree_form');
    let school_name = $('#school_name');
    let graduation_time = $('#graduation_time');
    let profession = $('#profession');
    let graduation_worker_time = $('#graduation_worker_time');
    let course_hours = $('#course_hours');
    let major = $('#major');

    if (parseInt(obj) === 1) {
        // alert(obj+","+graduation_status+","+more_status+","+strict);
        $('.graduation_status').show();

        $('.education_degree_form').show();
        $('.school_name').show();
        $('.graduation_time').show();
        $('.profession').show();
        $('.graduation_worker_time').show();
        $('.major').show();
        $('.course_hours').show();
        education_degree_form.attr('required', 'required');
        school_name.attr('required', 'required');
        graduation_time.attr('required', 'required');
        profession.attr('required', 'required');
        graduation_worker_time.attr('required', 'required');
        major.attr('required', 'required');
        course_hours.attr('required', 'required');

        $('.diploma_certificate_photos').show();

        graduation_status_id.empty("");
        let px = [9, 10, 11];
        if (px.indexOf(graduation_status) > -1) {
            $.each(options, function (i, n) {
                if (i === graduation_status) {
                    graduation_status_id.append("<option value=" + i.toString() + ">" + n + "</option>");
                } else if (i >= graduation_status) {
                    console.log("未匹配！");
                }
            });
            $('.major').hide();
            $('.course_hours').show();
            major.removeAttr('required');
            $("#graduation_time_value").html("结业时间");
            $("#school_name_value").html("结业院校名称");
            $("#val3").val("上传结业证件照");
        } else {
            $('.major').show();
            $('.course_hours').hide();
            course_hours.removeAttr('required');
            $("#graduation_time_value").html("毕业时间");
            $("#school_name_value").html("毕业院校名称");
            $("#val3").val("上传毕业证件照");
            if (more_status) {
                graduation_status_id.empty("");
                $.each(options, function (i, n) {
                    if (i >= graduation_status && i < 9) {
                        graduation_status_id.append("<option value=" + i.toString() + ">" + n + "</option>");
                    } else {
                        console.log("未匹配！");
                    }
                });
            } else {
                graduation_status_id.empty("");
                $.each(options, function (i, n) {
                    if (i === graduation_status) {
                        graduation_status_id.append("<option value=" + i.toString() + ">" + n + "</option>");
                    }
                    if (typeof two !== "undefined" && i === two) {
                        graduation_status_id.append("<option value=" + i.toString() + ">" + n + "</option>");
                    }
                    if (typeof thrid !== "undefined" && i === thrid) {
                        graduation_status_id.append("<option value=" + i.toString() + ">" + n + "</option>");
                    } else {
                        console.log("未匹配！");
                    }
                });
            }
        }

        //
        //
        // let graduation_status_id = $('#graduation_status');
        // graduation_status_id.val(graduation_status);
        // graduation_status_id.attr('disabled', 'disabled');

    } else if (parseInt(obj) === 2) {
        $("#condition-b").val("");
        graduation_status_id.removeAttr('data-strict');
        $('.graduation_status').hide();
        $('.education_degree_form').hide();
        $('.school_name').hide();
        $('.graduation_time').hide();
        $('.profession').hide();
        $('.graduation_worker_time').hide();
        $('.diploma_certificate_photos').hide();
        $('.major').hide();
        $('.strict_status').hide();
        education_degree_form.removeAttr('required');
        school_name.removeAttr('required');
        graduation_time.removeAttr('required');
        profession.removeAttr('required');
        graduation_worker_time.removeAttr('required');
        major.removeAttr('required');
        this.focus();
    } else {
        $("#condition-b").val("");
        graduation_status_id.removeAttr('data-strict');
        $('.graduation_status').hide();
        $('.education_degree_form').hide();
        $('.school_name').hide();
        $('.graduation_time').hide();
        $('.profession').hide();
        $('.graduation_worker_time').hide();
        $('.major').hide();
        $('.strict_status').hide();
        education_degree_form.removeAttr('required');
        school_name.removeAttr('required');
        graduation_time.removeAttr('required');
        profession.removeAttr('required');
        graduation_worker_time.removeAttr('required');

        major.removeAttr('required');
        $("#diploma_certificate_photos").val("");
        $('.diploma_certificate_photos').hide();
        alert("尚未选择毕业状态，请选择");
    }
}

function career_life_time(need_year) {


    if (typeof need_year === "undefined") {
        let start_the_work_of_this_occupation_id = $('#start_the_work_of_this_occupation');
        start_the_work_of_this_occupation_id.val("");
        start_the_work_of_this_occupation_id.removeAttr("required");
        $('#career_life').val("");
        $('#career_life_time').val("");
    } else {
        $("#start_the_work_of_this_occupation").attr("required", "required");
        $('#career_life_time').val(need_year);
        $('.career_life').show();
        $('.start_the_work_of_this_occupation').show();
        $('.career_life_time').hide();
    }
}

function apprentice_check(status) {

    let apprentice_start = $("#apprentice_start");
    let apprentice_end = $("#apprentice_end");
    if (status) {
        $('.apprentice').show();
        apprentice_start.attr('required', 'required');
        apprentice_end.attr('required', 'required');
    } else {
        apprentice_start.removeAttr('required');
        apprentice_start.val("");
        apprentice_end.removeAttr('required');
        apprentice_end.val("");
        $("#apprentice_year").val("");
        $("#apprentice_month").val("");


    }
}

function condition_label_style() {
    this.css('color', 'green');
}


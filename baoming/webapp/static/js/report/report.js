$(document).ready(function() {
    getEducationDegree(0, null);
    getUnitNature(0, null);
    province(0, null);
    update_report();
    cancel_search();


    $('.update_status_ok').hide();
    $('.update_status_fail').hide();
    $(".reset_password").show();
    $(".receiver_search_div").hide();
    $(".search_div").hide();
    // $('.identification_level_search').val("");
    // $('.education_degree_search').val("");
    // $('.teacher_info_search').val("");

    // 发送消息初始化设置
    let message_range_id = $("#message_range_id").val();
    message_range_select(message_range_id);
});

/**
 * 更新性别的时候自动补全
 */
function update_report() {
    // 写死的下拉框
    $("#sex").val($("#update_sex").val());
    $("#political_status").val($("#update_political_status").val());
    $("#primary_level").val($("#update_primary_level").val());
    $("#identification_level_update").val($("#update_identification_level").val());
    $("#teacher_info_update").val($("#update_teacher_info").val());

    $("#identification_level_search").val($("#search_identification_level").val());

    $("#teacher_info_search").val($("#search_teacher_info").val());

    let graduation_status = $("#update_graduation_status").val();
    if (parseInt(graduation_status) > 0) {
        $("#graduation_status").val(graduation_status);
    }

    let condition_selected_update = $("#condition_selected_update").val();
    if (typeof condition_selected_update !== "undefined" && condition_selected_update.length > 0) {
        // 如果时修改的话不需要清空数据
        // condition_controller(condition_selected, "update");
        condition_controller_update(condition_selected_update, "update");

    }

    let graduation_result = $('#update_graduation_result').val();
    if (parseInt(graduation_result) === 1) {
        $('#graduation_result_1').prop("checked", "checked");
    } else {
        $("#graduation_result_0").prop("checked", "checked");
    }

    // 异步加载的下拉框
    getEducationDegree(1, parseInt($("#update_education_degree").val()));
    getUnitNature(1, parseInt($("#update_unit_nature").val()));

    getNationInfo(1, parseInt($("#update_nation_info").val()));
    // getTeacherInfo(1, parseInt($("#update_teacher_info").val()));

    let province_id = parseInt($("#update_hukou_province").val());
    if (isNaN(province_id)) {
        province(1);
    } else {
        province(1, province_id);
    }

}

function delete_history(obj) {
    /**
     * 删除工作经历
     * @type {string}
     */
    let url = '/report/delete_history/';
    let form_data = new FormData();
    form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    form_data.append("uid", obj.id);
    $.ajax({
        url: url,
        type: 'POST',
        data: form_data,
        processData: false, // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function(data) {
            if (data.status) {
                alert("删除成功！");
                window.location.reload();
            } else {
                alert("删除失败！");
            }
        }
    });
}

function check_career_life(obj) {
    /**
     * 判断工种的年限
     */
    let worker = $("#declaration_of_occupation").val();
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
    let str = "其中电工、焊工需连续6年以上工作经验，若有初级证书则需要4年工作经验；" +
        "钳工需连续7年以上工作经验，若有初级证书，则需要3年以上工作经验；" +
        "育婴员需连续2年以上工作经验；保育员需连续2年以上工作经验；劳动关系协调员需连续6年以上工作经验";
    if (worker === '焊工') {
        if (obj === 0) {
            alert("请添加 焊工 工种工龄职业年限");
        } else if (obj >= 6) {
            alert("您 焊工 以满6年工作经验，请继续填报");
            $("#certificate_photos_td01").hide();
            $("#certificate_photos_td02").hide();
            $(".more_info").show();
        } else if (obj >= 4) {
            alert('您 焊工 需连续6年以上工作经验，若有初级证书则需要4年工作经验;请上传初级证书证明图片！');
            $("#certificate_photos_td01").show();
            $("#certificate_photos_td02").show();
            $("#val2").removeAttr("disabled");
            $("#val2").attr("title", "请上传毕业证照片！");
        } else {
            alert('您 焊工 工作经验尚未满4年，不要继续填报！！！');
            $("#career_life").val("");
            $(".more_info").hide();
        }
    } else if (worker === '电工') {
        if (obj === 0) {
            alert("请添加 电工 工种工龄职业年限");
        } else if (obj >= 6) {
            alert("您 电工 以满6年工作经验，请继续填报");
            $("#certificate_photos_td01").hide();
            $("#certificate_photos_td02").hide();
            $(".more_info").show();
        } else if (obj >= 4) {
            alert('电工 需连续6年以上工作经验，若有初级证书则需要4年工作经验;请上传初级证书证明图片！');
            $("#certificate_photos_td01").show();
            $("#certificate_photos_td02").show();
            $("#val2").removeAttr("disabled");
            $("#val2").attr("title", "请上传毕业证照片！");
        } else {
            alert('您工作经验尚未满4年，不要继续填报！！！');
            $("#career_life").val("");
            $(".more_info").hide();
        }
    } else if (worker === '钳工') {
        if (obj === 0) {
            alert("请添加 钳工 工种工龄职业年限");
        } else if (obj >= 7) {
            alert("您以满7年工作经验，请继续填报");
            $("#certificate_photos_td01").hide();
            $("#certificate_photos_td02").hide();
            $(".more_info").show();
        } else if (obj >= 3) {
            alert('钳工 需连续7年以上工作经验，若有初级证书则需要3年工作经验;请上传初级证书证明图片！');
            $("#certificate_photos_td01").show();
            $("#certificate_photos_td02").show();
            $("#val2").removeAttr("disabled");
            $("#val2").attr("title", "请上传毕业证照片！");
        } else {
            alert('您 钳工 工作经验尚未满3年，不要继续填报！！！');
            $("#career_life").val("");
            $(".more_info").hide();
        }
    } else if (worker === '育婴员') {
        if (obj === 0) {
            alert("请添加 育婴员 工种工龄职业年限");
        } else if (obj >= 2) {
            alert("您 育婴员 以满2年工作经验，请继续填报");
            $("#certificate_photos_td01").hide();
            $("#certificate_photos_td02").hide();
            $(".more_info").show();
        } else {
            alert('您 育婴员 工作经验尚未满2年，不要继续填报！！！');
            $("#career_life").val("");
            $(".more_info").hide();
        }
    } else if (worker === '保育员') {
        if (obj === 0) {
            alert("请添加 保育员 工种工龄职业年限");
        } else if (obj >= 2) {
            alert("您 保育员 以满2年工作经验，请继续填报");
            $("#certificate_photos_td01").hide();
            $("#certificate_photos_td02").hide();
            $(".more_info").show();
        } else {
            alert('您 保育员 工作经验尚未满2年，不要继续填报！！！');
            $("#career_life").val("");
            $(".more_info").hide();
        }
    } else if (worker === '劳动关系协调员') {
        if (obj === 0) {
            alert("请添加 劳动关系协调员 工种工龄职业年限");
        } else if (obj >= 2) {
            alert("您 劳动关系协调员 以满2年工作经验，请继续填报");
            $("#certificate_photos_td01").hide();
            $("#certificate_photos_td02").hide();
            $(".more_info").show();
        } else {
            alert('您 劳动关系协调员 劳动关系协调员 工作经验尚未满2年，不要继续填报！！！');
            $("#career_life").val("");
            $(".more_info").hide();
        }
    } else if (worker === '化工') {
        if (obj === 0) {
            alert("请添加 化工 工种工龄职业年限");
        } else if (obj >= 6) {
            alert("您 化工 以满7年工作经验，请继续填报");
            $("#certificate_photos_td01").hide();
            $("#certificate_photos_td02").hide();
            $(".more_info").show();
        } else if (obj >= 1) {
            alert('您 化工 工作经验尚已满1年，未满7年，请上传初级证书之后继续填报！！！');
            $("#certificate_photos_td01").show();
            $("#certificate_photos_td02").show();
            $("#val2").removeAttr("disabled");
            $("#val2").attr("title", "请上传毕业证照片！");
        } else {
            alert('您 化工 工作经验尚未满1年，不要继续填报！！！');
            $("#career_life").val("");
            $(".more_info").hide();
        }
    } else {
        alert('您尚未选择任何申报方向，请选择申报职业方向在继续填报，否则不要继续填报！！！');
    }
}


// function level_change(obj) {
//     /**
//      * 级别联动
//      */
//     let next_obj = obj + 1;
//     $("#identification_level").val(next_obj);
// }

function add_work() {
    let form = document.querySelector("#add_work_history");
    let form_data = new FormData(form);
    form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    let url = '/report/add_work_history/';
    $.ajax({
        url: url,
        type: 'POST',
        data: form_data,
        processData: false, // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function(data) {
            if (data.status) {
                alert("添加成功！");
                let data_list = JSON.parse(data.data);
                $("#worker_tbody").empty("");
                $.each(data_list, function(i, n) {
                    let tr_str = "<tr>\n" +
                        "            <td class=\"form-label\">\n" +
                        "                <label style='color:white'>" + n.start_year + "</label>\n" +
                        "                <span style='display: inline-block;color:black'>&nbsp;年&nbsp;</span>\n" +
                        "                <label style='color:white'>" + n.start_month + "</label>\n" +
                        "                <span style='display: inline-block;color:black'>&nbsp;月&nbsp;</span>\n" +
                        "            </td>\n" +
                        "            <td class=\"form-label\">\n" +
                        "                <label style='color:white'>" + n.end_year + "</label>\n" +
                        "                <span style='display: inline-block;color:black'>&nbsp;年&nbsp;</span>\n" +
                        "                <label style='color:white'>" + n.end_month + "</label>\n" +
                        "                <span style='display: inline-block;color:black'>&nbsp;月&nbsp;</span>\n" +
                        "            </td>\n" +
                        "            <td class=\"form-label\">\n" +
                        "                <label style='color:white'>" + n.unit_name + "</label>\n" +
                        "            </td>\n" +
                        "            <td class=\"form-label td-input\">\n" +
                        "                <label style='color:white'>" + n.region_name + "</label>\n" +
                        "            </td>\n" +
                        "            <td class=\"form-label\">\n" +
                        "                <label style='color:white'>" + n.job_content + "</label>\n" +
                        "            </td>\n" +
                        "            <td>\n" +
                        "                <input type='button' style=\"color: #ff0000;width: 30px;height: 25px; font-size: 10px\" value='删除'\n" +
                        "                       class='submitBtn form-button' onclick='delete_work(" + n.id + ")'/>\n" +
                        "            </td>\n" +
                        "        </tr>";
                    $("#worker_tbody").append(tr_str);
                })
            } else {
                console.log();
            }
        }
    });
}


function cancel_search() {
    $('.form-table-search').hide();
    $('.a-search').hide();
    $('.a-search-cancel').hide();
    $('.hr-search').hide();
    $('.p-search').show();
}

function recover_search() {
    $('.form-table-search').show();
    $('.a-search').show();
    $('.a-search-cancel').show();
    $('.hr-search').show();
    $('.p-search').hide();

}

function identification_level_search_f(obj) {
    let declaration_of_occupation_search = $("#declaration_of_occupation_search");
    let declaration_of_occupation_search_value = declaration_of_occupation_search.val();
    if (declaration_of_occupation_search_value.length > 0) {
        if (parseInt(obj) > 0) {
            $('.identification_level_search').val(parseInt(obj));
        } else if (parseInt(obj) === 0) {
            $('#identification_level_search').val(0);
        }
    } else {
        alert("请先填写申报职业的查询项！");
        $('#identification_level_search').val(0);
        declaration_of_occupation_search.focus();
    }
}

function education_degree_search() {
    if (parseInt(obj) > 0) {
        $('.education_degree_search').val(parseInt(obj));
    } else {
        $('.education_degree_search').val(0);
    }
}

function teacher_info_a_search(obj) {
    if (parseInt(obj) > 0) {
        $('#search_teacher_info').val(parseInt(obj));
    } else if (parseInt(obj) === 0) {
        $('#search_teacher_info').val(0);
    }
}

function school_term_a_search(obj, school_terms) {
    let array_school_terms = JSON.parse(school_terms);
    if (parseInt(obj) > 0) {
        $('#search_school_term').val(parseInt(obj));
        $.each(array_school_terms, function(i, n) {
            if (n.id_str == parseInt(obj)) {
                console.log(n.school_term_name);
                console.log(n.school_term_start);
                console.log(n.school_term_end);
                $('.school_term_name').html(n.school_term_name);
                $('.school_term_start').html(n.school_term_start);
                $('.school_term_end').html(n.school_term_end);
            }
        })
    } else if (parseInt(obj) === 0) {
        $('.school_term_name').html(array_school_terms[0].school_term_name);
        $('.school_term_start').html(array_school_terms[0].school_term_start);
        $('.school_term_end').html(array_school_terms[0].school_term_end);
        $('#search_school_term').val(0);
    }
}

function declaration_of_occupation_clear_search(value) {
    if (typeof value === "undefined") {
        $('#identification_level_search').val(0);
    }
    if (value.length === 0) {
        $('#identification_level_search').val(0);
    }
    if (value === '') {
        $('#identification_level_search').val(0);
    }
    if (value === '') {
        $("#search_identification_level").val("")
    }
    if (value.length === 0) {
        $("#search_identification_level").val("")
    }
}
/**
 * 学员缴费
 * @param obj_id
 * @param school_term_name
 * @param declaration_of_occupation
 * @param identification_level
 * @param teacher_info_real_name
 * @param user_info_real_name
 * @param payment_amount
 * @param unpaid_amount
 */
function payment(obj_id,
                 school_term_name,
                 declaration_of_occupation,
                 identification_level,
                 teacher_info_real_name,
                 user_info_real_name,
                 payment_amount,
                 unpaid_amount) {
    let left = ($(window).width() * (1 - 0.35)) / 2;//box弹出框距离左边的额距离
    let height = ($(window).height() * (1 - 0.5)) / 2;
    $(".box_payment").addClass("animated bounceIn").show().css({left: left, top: height});
    $(".opacity_bg").css("opacity", "0.3").show();

    let payment_id = $("#payment_id");
    payment_id.val(obj_id);
    let payment_amount_tag = $("#payment_amount");
    payment_amount_tag.val(payment_amount);
    let unpaid_amount_tag = $("#unpaid_amount");
    unpaid_amount_tag.val(unpaid_amount);
    let payment_real_name = $("#payment_real_name");
    payment_real_name.text(user_info_real_name);
    let teacher_payment = $("#teacher_payment");
    teacher_payment.text(teacher_info_real_name);
    let declaration_of_occupation_payment = $("#declaration_of_occupation_payment");
    declaration_of_occupation_payment.text(declaration_of_occupation);
    let identification_level_payment = $("#identification_level_payment");
    identification_level_payment.text(identification_level);
    // let form_button = $('#payment_button');
    // form_button.attr('onclick', "add_payment_button();");
}

/**
 * 学员缴费
 * @param obj_id
 * @param school_term_name
 * @param declaration_of_occupation
 * @param identification_level
 * @param teacher_info_real_name
 * @param user_info_real_name
 * @param payment_amount
 * @param unpaid_amount
 */
function teacher_update_payment(obj_id,
                                school_term_name,
                                declaration_of_occupation,
                                identification_level,
                                teacher_info_real_name,
                                user_info_real_name,
                                payment_amount,
                                unpaid_amount) {
    let left = ($(window).width() * (1 - 0.35)) / 2;//box弹出框距离左边的额距离
    let height = ($(window).height() * (1 - 0.5)) / 2;
    $(".box_payment_teacher").addClass("animated bounceIn").show().css({left: left, top: height});
    $(".opacity_bg").css("opacity", "0.3").show();

    let payment_id = $("#payment_id");
    payment_id.val(obj_id);
    let payment_amount_tag = $("#payment_amount");
    payment_amount_tag.val(payment_amount);
    let unpaid_amount_tag = $("#unpaid_amount");
    unpaid_amount_tag.val(unpaid_amount);
    let payment_real_name = $("#payment_real_name");
    payment_real_name.text(user_info_real_name);
    let teacher_payment = $("#teacher_payment");
    teacher_payment.text(teacher_info_real_name);
    let declaration_of_occupation_payment = $("#declaration_of_occupation_payment");
    declaration_of_occupation_payment.text(declaration_of_occupation);
    let identification_level_payment = $("#identification_level_payment");
    identification_level_payment.text(identification_level);
    // let form_button = $('#payment_button');
    // form_button.attr('onclick', "add_payment_button();");
}


function add_payment() {
    let record_id = 0;
    let payment_id = $("#payment_id").val();
    let payment_amount_value = $("#payment_amount").val();
    let unpaid_amount_value = $("#unpaid_amount").val();
    if (typeof payment_id === "string") {
        record_id = parseInt(payment_id);
    } else {
        record_id = payment_id;
    }
    if (payment_id > 0) {
        if (parseInt(payment_amount_value) > 0) {
            let confirm_result = confirm("确定对本次报名记录缴费?");
            if (confirm_result) {
                let form_data = new FormData();
                let url = '/report/report_student_payment/';
                form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
                form_data.append("record_id", record_id);
                form_data.append("payment_amount", payment_amount_value);
                form_data.append("unpaid_amount", unpaid_amount_value);

                $.ajax({
                    url: url,
                    type: 'POST',
                    data: form_data,
                    processData: false,  // tell jquery not to process the data
                    contentType: false, // tell jquery not to set contentType
                    success: function (data) {
                        if (data.status) {
                            alert(data.message);
                            window.location.reload();
                        } else {
                            alert(data.message);
                        }
                    }
                });
            }
        } else {
            alert("缴费数额为 0 ，请不要继续操作");
        }
    }

}
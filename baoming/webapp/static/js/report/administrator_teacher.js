function add_teacher() {
    //关闭弹窗
    let formElement = document.querySelector('#register-form-teacher');
    let formData = new FormData(formElement);

    // let form_data = $('#register-form-teacher').serialize();
    console.log(formData);
    let url = '/report/register_teacher/';
    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        processData: false,  // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function (data) {
            if (data.status) {
                alert(data.message);
                //关闭模态框
                let left = ($(window).width() * (1 - 0.35)) / 2;
                let top = ($(window).height() * (1 - 0.5)) / 2;
                $(".box_teacher").show().animate({
                    width: "-$(window).width()*0.35",
                    height: "-$(window).height()*0.5",
                    left: "-" + left + "px",
                    top: "-" + top + "px"
                }, 1000, function () {
                    let width1 = $(window).width() * 0.35;
                    let height1 = $(window).height() * 0.5;
                    console.log(width1);
                    $(this).css({width: width1, height: height1}).hide();
                });
                window.location.reload();
            } else {
                alert(data.message);
            }
        }
    });
}

/**
 * 修改
 */
function to_update_teacher(obj) {
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    formData.append('teacher_id', obj);
    // let form_data = $('#register-form-teacher').serialize();
    console.log(formData);
    let url = '/report/to_update_teacher/';
    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        processData: false,  // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function (data) {
            if (data.status) {
                let data0 = data.data;
                let jd = JSON.parse(data0);
                console.log(jd);
                json2form('register-form-teacher', jd);
                let form_button = $('#teacher_button');
                $('.passwordReg-teacher').hide();
                $('.finalPWD-teacher').hide();
                let username_teacher = $("#username-teacher");
                username_teacher.attr('readonly','readonly');
                username_teacher.removeAttr('onblur');
                username_teacher.removeAttr('onchange');
                form_button.removeAttr("disabled");

                let nickname_teacher = $("#nickname-teacher");
                nickname_teacher.attr('readonly','readonly');
                nickname_teacher.removeAttr('onblur');
                nickname_teacher.removeAttr('onchange');

                let passwordReg_teacher = $("#passwordReg-teacher");
                passwordReg_teacher.removeAttr('onblur');
                passwordReg_teacher.removeAttr('onchange');
                passwordReg_teacher.removeAttr('required');
                let finalPWD_teacher = $("#finalPWD-teacher");
                finalPWD_teacher.removeAttr('onblur');
                finalPWD_teacher.removeAttr('onchange');
                finalPWD_teacher.removeAttr('required');

                $('#username-teacher-label').html("");

                $('#update-id').val(jd['id']);
                form_button.attr('onclick', "update_object_teacher();");
                let left = ($(window).width() * (1 - 0.35)) / 2;//box弹出框距离左边的额距离
                let height = ($(window).height() * (1 - 0.5)) / 2;
                let box_school_term = $(".box_teacher");
                box_school_term.addClass("animated bounceIn").show().css({left: left, top: top});
                $(".opacity_bg").css("opacity", "0.3").show();
            } else {
                alert(data.message);
            }
        }
    });

}


function update_object_teacher() {
    //关闭弹窗
    let formElement = document.querySelector('#register-form-teacher');
    let formData = new FormData(formElement);

    // let form_data = $('#register-form-teacher').serialize();
    console.log(formData);
    let url = '/report/update_teacher_info/';
    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        processData: false,  // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function (data) {
            if (data.status) {
                alert(data.message);
                let left = ($(window).width() * (1 - 0.35)) / 2;//box弹出框距离左边的额距离
                let height = ($(window).height() * (1 - 0.5)) / 2;
                let box_school_term = $(".box_teacher");
                box_school_term.show().animate({
                    width: "-$(window).width()*0.35",
                    height: "-$(window).height()*0.5",
                    left: "-" + left + "px",
                    top: "-" + top + "px"
                }, 1000, function () {
                    let width1 = $(window).width() * 0.35;
                    let height1 = $(window).height() * 0.5;
                    console.log(width1);
                    $(this).css({width: width1, height: height1}).hide();
                });
                $("#username-teacher").removeAttr('readonly');
                window.location.reload();
            } else {
                alert(data.message);
                window.location.reload();
            }
        }
    });
}

/**
 * 删除
 */
function cancel_teacher(obj) {
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    formData.append('teacher_id', obj);
    // let form_data = $('#register-form-teacher').serialize();
    console.log(formData);
    let url = '/report/cancel_teacher/';
    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        processData: false,  // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function (data) {
            if (data.status) {
                alert(data.message);
                window.location.reload();
            }else{
                alert(data.message);
            }
        }
    });
}
function start_teacher(obj){
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    formData.append('teacher_id', obj);
    // let form_data = $('#register-form-teacher').serialize();
    console.log(formData);
    let url = '/report/start_teacher/';
    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        processData: false,  // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function (data) {
            if (data.status) {
                alert(data.message);
                window.location.reload();
            }else{
                alert(data.message);
            }
        }
    });
}
/**
 * 添加角色
 */
function add_register() {
    //关闭弹窗
    let formElement = document.querySelector('#form-register');
    let formData = new FormData(formElement);
    let url = '/report/add_register/';
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
                $(".box_register").show().animate({
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

function to_update_register(obj) {
    //关闭弹窗
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    formData.append('update_id', obj);
    let url = '/report/to_update_register/';
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
                json2form('form-register', jd);
                let form_button = $('#register_button');
                $('#update-id').val(jd['id']);
                form_button.attr('onclick', "update_register);");
                let left = ($(window).width() * (1 - 0.35)) / 2;//box弹出框距离左边的额距离
                let height = ($(window).height() * (1 - 0.5)) / 2;
                let box_register = $(".box_register");
                box_register.addClass("animated bounceIn").show().css({left: left, top: top});
                $(".opacity_bg").css("opacity", "0.3").show();
            } else {
                alert(data.message);
            }
        }
    });
}

function update_register() {
    //关闭弹窗
    let formElement = document.querySelector('#form-register');
    let formData = new FormData(formElement);
    console.log(formData);
    let url = '/report/update_register_info/';
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
                let box_register = $(".box_register");
                box_register.show().animate({
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

function reset_password() {
    //关闭弹窗
    let formElement = document.querySelector('#form-register');
    let formData = new FormData(formElement);
    console.log(formData);
    let url = '/report/update_register_info/';
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
                let box_register = $(".box_register");
                box_register.show().animate({
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
 * 按照id 删除此账户下所有关联数据
 * @param obj_id
 */
function del_deep_register(obj_id) {
    let url = '/report/del_register_info/';
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof record_id === "number") {
        let confirm_result = confirm("彻底删除本账号所有相关记录?");
        if (confirm_result) {
            let form_data = new FormData();
            form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
            form_data.append("record_id", record_id);
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
    }
}
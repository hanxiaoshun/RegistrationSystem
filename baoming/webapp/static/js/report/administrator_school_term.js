function add_school_term() {
    //关闭弹窗
    let formElement = document.querySelector('#form-school-term');
    let formData = new FormData(formElement);

    // let form_data = $('#register-form-teacher').serialize();
    console.log(formData);
    let url = '/report/add_school_term/';
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
                $(".box_school_term").show().animate({
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

function to_update_term_info(obj) {
    //关闭弹窗
    // let formElement = document.querySelector('#add-form-school-term');
    // let formData = new FormData(formElement);
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    formData.append('term_id', obj);
    // let form_data = $('#register-form-teacher').serialize();
    let url = '/report/to_update_term_info/';
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
                json2form('form-school-term', jd);
                let form_button = $('#school_term_button');
                $('#update-id').val(jd['id']);
                form_button.attr('onclick', "update_school_term();");
                let left = ($(window).width() * (1 - 0.35)) / 2;//box弹出框距离左边的额距离
                let height = ($(window).height() * (1 - 0.5)) / 2;
                let box_school_term = $(".box_school_term");
                box_school_term.addClass("animated bounceIn").show().css({left: left, top: height});
                $(".opacity_bg").css("opacity", "0.3").show();
            } else {
                alert(data.message);
            }
        }
    });
}

function update_school_term() {
    //关闭弹窗
    let formElement = document.querySelector('#form-school-term');
    let formData = new FormData(formElement);

    // let form_data = $('#register-form-teacher').serialize();
    console.log(formData);
    let url = '/report/update_school_term/';
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
                let box_school_term = $(".box_school_term");
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
                window.location.reload();
            } else {
                alert(data.message);
            }
        }
    });
}

/**
 * 删除
 */
function del_term_info(obj){
    del('/report/del_term_info/',obj);
}

function del_term_info_data(obj_id){
    let record_id = 0;
    let url = '/report/admin_del_term_info_data/';
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof record_id === "number") {
        let confirm_result = confirm("确定删除本学期的学员填报数据?");
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


function refresh_term_info(obj) {
    //关闭弹窗
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    formData.append('term_id', obj);

    console.log(formData);
    let url = '/report/refresh_school_term_data/';
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
                window.location.reload();
            }
        }
    });
}
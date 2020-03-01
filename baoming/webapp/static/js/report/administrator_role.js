/**
 * 添加角色
 */
function add_role() {
    //关闭弹窗
    let formElement = document.querySelector('#form-role');
    let formData = new FormData(formElement);
    let url = '/report/add_role/';
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
                $(".box_role").show().animate({
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

function to_update_role(obj) {
    //关闭弹窗
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    formData.append('update_id', obj);
    let url = '/report/to_update_role/';
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
                json2form('form-role', jd);
                let form_button = $('#role_button');
                $('#update-id').val(jd['id']);
                form_button.attr('onclick', "update_role);");
                let left = ($(window).width() * (1 - 0.35)) / 2;//box弹出框距离左边的额距离
                let height = ($(window).height() * (1 - 0.5)) / 2;
                let box_role = $(".box_role");
                box_role.addClass("animated bounceIn").show().css({left: left, top: top});
                $(".opacity_bg").css("opacity", "0.3").show();
            } else {
                alert(data.message);
            }
        }
    });
}

function update_role() {
    //关闭弹窗
    let formElement = document.querySelector('#form-role');
    let formData = new FormData(formElement);
    console.log(formData);
    let url = '/report/update_role_info/';
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
                let box_role = $(".box_role");
                box_role.show().animate({
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
function del_role(obj) {
    del('/report/del_role_info/', obj);
}
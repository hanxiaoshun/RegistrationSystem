/**
 * 关于用户注册时的一些验证
 */
//--------------------------------------------
function check_username_index() {
    /**
     * 检查用户名使用情况
     * @type {string}
     */
    let url = '/report/check_username/';
    let username = $("#username_index");
    let value = username.val().trim();


    if (value.length === 0) {
        username.css("border", "0.8px");
        username.css("solid", '#ff9dcb');
        $(".submit_index").attr("disabled", "disabled");
        let message_label = username.parent().next().children("span:first-child");
        message_label.text("用户名不能为空");
        message_label.css("color", "red");
    } else if (!CheckPassUsername(value)) {
        username.css("border", "0.8px");
        username.css("solid", '#ff9dcb');
        $(".submit_index").attr("disabled", "disabled");
        let message_label = username.parent().next().children("span:first-child");
        message_label.text("用户名由数字、字母或字母数字组合，且长度>3");
        message_label.css("color", "red");
    } else {
        // {register: {username: value}}
        $.ajax({
            url: url,
            type: 'POST',
            tradition: true,
            data: $("#register-form-index").serialize(),
            success: function (data) {
                /*var callback_dic = $.parseJSON(arg);*/
                /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
                // var strs = JSON.stringify(arg);
                if (data.status) {
                    username.css("border", "0.8px");
                    username.css("solid", '#9bff14');
                    $(".submit_index").removeAttr('disabled');
                    let message_label = username.parent().next().children("span:first-child");
                    message_label.text("恭喜用户名可以使用");
                    message_label.css("color", "#d0ffc7");
                } else {
                    username.css("border", "0.8px");
                    username.css("solid", '#ff9dcb');
                    $(".submit_index").attr("disabled", "disabled");
                    let message_label = username.parent().next().children("span:first-child");
                    message_label.text("用户名已被使用，请您更换！");
                    message_label.css("color", "red");
                }
            }
        });
    }
}

//--------------------------------------------
function check_nickname_index() {
    /**
     * 检查昵称是否有人注册
     * @type {string}
     */
    let url = '/report/check_nickname/';
    let nickname = $("#nickname_index");
    let value = nickname.val().trim();
    if (value.length === 0) {
        nickname.css("border", "0.8px");
        nickname.css("solid", '#ff9dcb');
        $(".submit_index").attr("disabled", "disabled");
        let message_label = nickname.parent().next().children("span:first-child");
        message_label.text("昵称不能为空");
        message_label.css("color", "red");
    } else {
        $.ajax({
            url: url,
            type: 'POST',
            tradition: true,
            data: $("#register-form-index").serialize(),
            success: function (data) {
                /*var callback_dic = $.parseJSON(arg);*/
                /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
                // var strs = JSON.stringify(arg);
                if (data.status) {
                    nickname.css("border", "0.8px");
                    nickname.css("solid", '#9bff14');
                    $(".submit_index").removeAttr('disabled');
                    let message_label = nickname.parent().next().children("span:first-child");
                    message_label.text("恭喜昵称可以使用");
                    message_label.css("color", "#d0ffc7");
                } else {
                    nickname.css("border", "0.8px");
                    nickname.css("solid", '#ff9dcb');
                    $(".submit_index").attr("disabled", "disabled");
                    let message_label = nickname.parent().next().children("span:first-child");
                    message_label.text("用户名已被使用，请您更换！");
                    message_label.css("color", "red");
                }
            }
        });
    }
}

function check_password_index() {
    /**
     * 检查密码的质量以及是否一致
     */
    let passwordReg = $("#passwordReg_index");
    let finalPWD = $("#finalPWD_index");
    let patt = new RegExp("[0-9A-Za-z_]{0,?}");
    if (!CheckPassWord(passwordReg.val().trim())) {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#ff9dcb');
        $(".submit_index").attr("disabled", "disabled");
        let message_label = passwordReg.parent().next().children("span:first-child");
        message_label.text("密码长度不小于6，只允许包含数字、字母！");
        message_label.css("color", "red");
    } else {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#9bff14');
        $(".submit_index").removeAttr('disabled');
        let message_label = passwordReg.parent().next().children("span:first-child");
        message_label.text("恭喜密码验证通过");
        message_label.css("color", "#d0ffc7");
    }
}

function check_equal_index() {
    /**
     * 检查两次密码是否一致
     * @type {*|jQuery.fn.init|jQuery|HTMLElement}
     */
    let passwordReg = $("#passwordReg_index");
    let finalPWD = $("#finalPWD_index");
    let value = passwordReg.val();
    if (value.length === 0) {
        passwordReg.css("border", "1px");
        passwordReg.css("solid", '#ff9dcb');
        $(".submit_index").attr("disabled", "disabled");
        let message_label = passwordReg.parent().next().children("span:first-child");
        message_label.text("密码不能为空");
        message_label.css("color", "red");
    } else if (value === finalPWD.val()) {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#9bff14');
        finalPWD.css("border", "0.8px");
        finalPWD.css("solid", '#9bff14');
        $(".submit_index").removeAttr('disabled');
        let message_label = finalPWD.parent().next().children("span:first-child");
        message_label.text("恭喜密码验证通过");
        message_label.css("color", "#d0ffc7");
    } else {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#ff9dcb');
        finalPWD.css("border", "0.8px");
        finalPWD.css("solid", '#ff9dcb');
        $(".submit_index").attr("disabled", "disabled");
        let message_label = finalPWD.parent().next().children("span:first-child");
        message_label.text("两次输入的密码不一致！");
        message_label.css("color", "red");
    }

}

function CheckPassUsername_index(username) {//必须为字母加数字且长度不小于8位
    let str = username;
    let flag = true;
    if (str == null || str.length < 1) {
        flag = false;
    }
    let reg1 = new RegExp(/^[0-9A-Za-z]+$/);
    if (!reg1.test(str)) {
        flag = false;
    }
    // let reg = new RegExp(/[A-Za-z].*[0-9]|[0-9].*[A-Za-z]/);
    // if (reg.test(str)) {
    //     flag = false;
    // } else {
    //     flag = false;
    // }
    return flag;
}

function CheckPassNickname_index(nickname) {
    /**
     *
     */
    let str = nickname;
    let flag = true;
    if (str == null || str.length < 1) {
        flag = false;
    }
    return flag;
}

function CheckPassWord_index(password) {//必须为字母加数字且长度不小于8位
    let str = password;
    let flag = true;
    if (str == null || str.length < 6) {
        flag = false;
    }
    let reg1 = new RegExp(/^[0-9A-Za-z]+$/);
    if (!reg1.test(str)) {
        flag = false;
    }
    // let reg = new RegExp(/[A-Za-z].*[0-9]|[0-9].*[A-Za-z]/);
    // if (reg.test(str)) {
    //     flag = false;
    // } else {
    //     flag = false;
    // }
    return flag;
}
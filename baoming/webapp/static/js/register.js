/**
 * 关于用户注册时的一些验证
 */
//--------------------------------------------
function check_username() {
    /**
     * 检查用户名使用情况
     * @type {string}
     */
    let url = '/report/check_username/';
    let username = $("#username");
    let value = username.val().trim();
    if (value.length === 0) {
        username.css("border", "0.8px");
        username.css("solid", '#ff9dcb');
        $(".submit").attr("disabled", "disabled");
        let message_label = username.parent().next().children("span:first-child");
        message_label.text("用户名不能为空");
        message_label.css("color", "red");
    } else if (!CheckPassUsername(value)) {
        username.css("border", "0.8px");
        username.css("solid", '#ff9dcb');
        $(".submit").attr("disabled", "disabled");
        let message_label = username.parent().next().children("span:first-child");
        message_label.text("用户名由数字、字母或字母数字组合，且长度>3");
        message_label.css("color", "red");
    } else {
        // {register: {username: value}}
        $.ajax({
            url: url,
            type: 'POST',
            tradition: true,
            data: $("#register-form").serialize(),
            success: function (data) {
                /*var callback_dic = $.parseJSON(arg);*/
                /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
                // var strs = JSON.stringify(arg);
                if (data.status) {
                    username.css("border", "0.8px");
                    username.css("solid", '#9bff14');
                    $(".submit").removeAttr('disabled');
                    let message_label = username.parent().next().children("span:first-child");
                    message_label.text("恭喜用户名可以使用");
                    message_label.css("color", "#d0ffc7");
                } else {
                    username.css("border", "0.8px");
                    username.css("solid", '#ff9dcb');
                    $(".submit").attr("disabled", "disabled");
                    let message_label = username.parent().next().children("span:first-child");
                    message_label.text("用户名已被使用，请您更换！");
                    message_label.css("color", "red");
                }
            }
        });
    }
}

//--------------------------------------------
function check_nickname() {
    /**
     * 检查昵称是否有人注册
     * @type {string}
     */
    let url = '/report/check_nickname/';
    let nickname = $("#nickname");
    let value = nickname.val().trim();
    if (value.length === 0) {
        nickname.css("border", "0.8px");
        nickname.css("solid", '#ff9dcb');
        $(".submit").attr("disabled", "disabled");
        let message_label = nickname.parent().next().children("span:first-child");
        message_label.text("昵称不能为空");
        message_label.css("color", "red");
    } else {
        $.ajax({
            url: url,
            type: 'POST',
            tradition: true,
            data: $("#register-form").serialize(),
            success: function (data) {
                /*var callback_dic = $.parseJSON(arg);*/
                /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
                // var strs = JSON.stringify(arg);
                if (data.status) {
                    nickname.css("border", "0.8px");
                    nickname.css("solid", '#9bff14');
                    $(".submit").removeAttr('disabled');
                    let message_label = nickname.parent().next().children("span:first-child");
                    message_label.text("恭喜昵称可以使用");
                    message_label.css("color", "#d0ffc7");
                } else {
                    nickname.css("border", "0.8px");
                    nickname.css("solid", '#ff9dcb');
                    $(".submit").attr("disabled", "disabled");
                    let message_label = nickname.parent().next().children("span:first-child");
                    message_label.text("昵称已被使用，请您更换！");
                    message_label.css("color", "red");
                }
            }
        });
    }
}

function check_password() {
    /**
     * 检查密码的质量以及是否一致
     */
    let passwordReg = $("#passwordReg");
    let finalPWD = $("#finalPWD");
    let message_register = $("#message-register");
    let patt = new RegExp("[0-9A-Za-z_]{0,?}");
    if (!CheckPassWord(passwordReg.val().trim())) {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#ff9dcb');
        $(".submit").attr("disabled", "disabled");
        let message_label = passwordReg.parent().next().children("span:first-child");
        message_label.text("密码长度不小于6，只允许包含数字、字母！");
        message_label.css("color", "red");
    } else {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#9bff14');
        $(".submit").removeAttr('disabled');
        let message_label = passwordReg.parent().next().children("span:first-child");
        message_label.text("恭喜密码验证通过");
        message_label.css("color", "#d0ffc7");
    }
}

function check_equal() {
    /**
     * 检查两次密码是否一致
     * @type {*|jQuery.fn.init|jQuery|HTMLElement}
     */
    let passwordReg = $("#passwordReg");
    let finalPWD = $("#finalPWD");
    let value = passwordReg.val();
    let message_register = $("#message-register");
    if (value.length === 0) {
        passwordReg.css("border", "1px");
        passwordReg.css("solid", '#ff9dcb');
        $(".submit").attr("disabled", "disabled");
        let message_label = passwordReg.parent().next().children("span:first-child");
        message_label.text("密码不能为空");
        message_label.css("color", "red");
    } else if (value === finalPWD.val()) {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#9bff14');
        finalPWD.css("border", "0.8px");
        finalPWD.css("solid", '#9bff14');
        $(".submit").removeAttr('disabled');
        let message_label = finalPWD.parent().next().children("span:first-child");
        message_label.text("恭喜密码验证通过");
        message_label.css("color", "#d0ffc7");
    } else {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#ff9dcb');
        finalPWD.css("border", "0.8px");
        finalPWD.css("solid", '#ff9dcb');
        $(".submit").attr("disabled", "disabled");
        let message_label = finalPWD.parent().next().children("span:first-child");
        message_label.text("两次输入的密码不一致！");
        message_label.css("color", "red");
    }

}

function CheckPassUsername(username) {//必须为字母加数字且长度不小于8位
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

function CheckPassNickname(nickname) {
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

function CheckPassWord(password) {//必须为字母加数字且长度不小于8位
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

function check_new_password() {
    /**
     * 检查密码的质量以及是否一致
     */
    let passwordReg = $("#new_passwordReg");
    let finalPWD = $("#new_finalPWD");
    let message_register = $("#message-register");
    let patt = new RegExp("[0-9A-Za-z_]{0,?}");
    if (!CheckPassWord(passwordReg.val().trim())) {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#ff9dcb');
        $(".new_submit").attr("disabled", "disabled");
        let message_label = passwordReg.parent().next().children("span:first-child");
        message_label.text("密码长度不小于6，只允许包含数字、字母！");
        message_label.css("color", "red");
    } else {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#9bff14');
        $(".new_submit").removeAttr('disabled');
        let message_label = passwordReg.parent().next().children("span:first-child");
        message_label.text("恭喜密码验证通过");
        message_label.css("color", "#d0ffc7");
    }
}

function check_new_equal() {
    let new_submit = $(".new_submit");
    new_submit.attr("type", "submit");
    new_submit.removeAttr('onclick');
    /**
     * 检查两次密码是否一致
     * @type {*|jQuery.fn.init|jQuery|HTMLElement}
     */
    let passwordReg = $("#new_passwordReg");
    let finalPWD = $("#new_finalPWD");
    let value = passwordReg.val();
    let message_register = $("#message-register");
    if (value.length === 0) {
        passwordReg.css("border", "1px");
        passwordReg.css("solid", '#ff9dcb');
        new_submit.attr("disabled", "disabled");
        let message_label = passwordReg.parent().next().children("span:first-child");
        message_label.text("密码不能为空");
        message_label.css("color", "red");
    } else if (value === finalPWD.val()) {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#9bff14');
        finalPWD.css("border", "0.8px");
        finalPWD.css("solid", '#9bff14');
        new_submit.removeAttr('disabled');
        new_submit.attr("type", "button");
        new_submit.attr("onclick", "change_pwd();");
        let message_label = finalPWD.parent().next().children("span:first-child");
        message_label.text("恭喜密码验证通过");
        message_label.css("color", "#d0ffc7");
    } else {
        passwordReg.css("border", "0.8px");
        passwordReg.css("solid", '#ff9dcb');
        finalPWD.css("border", "0.8px");
        finalPWD.css("solid", '#ff9dcb');
        new_submit.attr("disabled", "disabled");
        let message_label = finalPWD.parent().next().children("span:first-child");
        message_label.text("两次输入的密码不一致！");
        message_label.css("color", "red");
    }

}

function check_origin_password() {
    /**
     * 检查原始密码是否正确
     * @type {string}
     */
    let url = '/report/check_origin_password/';
    let origin_password = $("#origin_password");
    let value = origin_password.val().trim();
    if (value.length === 0) {
        origin_password.css("border", "0.8px");
        origin_password.css("solid", '#ff9dcb');
        $(".new_submit").attr("disabled", "disabled");
        let message_label = origin_password.parent().next().children("span:first-child");
        message_label.text("原不能为空");
        message_label.css("color", "red");
    } else {
        $.ajax({
            url: url,
            type: 'POST',
            tradition: true,
            data: $("#register-form-reset-pwd").serialize(),
            success: function (data) {
                /*var callback_dic = $.parseJSON(arg);*/
                /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
                // var strs = JSON.stringify(arg);
                if (data.status) {
                    origin_password.css("border", "0.8px");
                    origin_password.css("solid", '#9bff14');
                    $(".new_submit").removeAttr('disabled');
                    let message_label = origin_password.parent().next().children("span:first-child");
                    message_label.text(data.message);
                    message_label.css("color", "#d0ffc7");
                } else {
                    origin_password.css("border", "0.8px");
                    origin_password.css("solid", '#ff9dcb');
                    $(".new_submit").attr("disabled", "disabled");
                    let message_label = origin_password.parent().next().children("span:first-child");
                    message_label.text(data.message);
                    message_label.css("color", "red");
                }
            }
        });
    }
}



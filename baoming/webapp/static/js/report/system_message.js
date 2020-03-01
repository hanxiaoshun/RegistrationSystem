function message_range_select(obj) {
    let hidden_selected = ['1', '2', '3', '5', '6', '8'];
    if (typeof obj === "undefined") {
        return false;
    } else if (obj.length === 0) {
        return false;
    } else {
        if (typeof obj === "string") {
            if (hidden_selected.indexOf(obj) > -1) {
                $(".receiver_search").hide();
                $(".receiver_search_content").hide();
                $(".receiver_search_result").hide();

                // 清空所有之前的收信人选择
                let search_div = $(".search_div");
                search_div.html("");
                let search_result_div = $(".search_result_div");
                search_result_div.html("");
                $("#receiver_ids").val("");
                let search_result_receiver = $("#search_result_receiver");
                search_result_receiver.val("");
                search_result_receiver.removeAttr('required')

            } else {
                $(".receiver_search").show();
                $(".receiver_search_result").show();
                $("#search_result_receiver").attr('required','required')
            }
        }
    }
}

/**
 * 根据用户名、昵称、姓名进行模糊搜索并生成对应的列表供选择
 * @param obj
 */
function receiver_search_f(obj) {
    if (typeof obj === "undefined") {
        return false;
    } else if (obj.length === 0) {
        return false;
    } else {
        if (typeof obj === "string") {
            let form_data = new FormData();
            let url = '/report/get_like_user_info/';
            form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
            form_data.append("record", obj);
            let message_range = $('#message_range_id').val();
            form_data.append('message_range', message_range);
            $.ajax({
                url: url,
                type: 'POST',
                data: form_data,
                processData: false,  // tell jquery not to process the data
                contentType: false, // tell jquery not to set contentType
                success: function (data) {
                    if (data.status) {
                        let search_results = '';
                        let json_data = JSON.parse(data.data);
                        $.each(json_data, function (i, n) {
                            let username = n.register_user_info__username;
                            let real_name = n.real_name;
                            let username_real_name = username + "@" + real_name;
                            search_results = search_results
                                + "<a href='javascript:void(0);' onclick=\"put_ids('" + n.id + "','" + username + "','" + real_name + "');\">" +
                                "<span style='color: orangered'>" + username_real_name + ";</span></a><hr>";
                            console.log(search_results);
                        });
                        let search_div = $(".search_div");
                        search_div.html(search_results);
                        search_div.show();
                        $(".receiver_search_content").show();
                        $('#message_save_id').removeAttr("disabled")
                    } else {
                        let search_div = $(".search_div");
                        search_div.html(data.message);
                        search_div.show();
                        $(".receiver_search_content").show();
                        $('#message_save_id').attr("disabled", "disabled")
                    }
                }
            });
        }
    }
}

/**
 * 将选择结果保存到面板展示
 * @param obj
 * @param username
 * @param real_name
 */
function put_ids(obj, username, real_name) {
    let receiver_ids = $("#receiver_ids");
    let receiver_ids_value = receiver_ids.val();
    if (receiver_ids_value.length > 0) {
        receiver_ids_value = receiver_ids_value + '-' + obj;
    } else {
        receiver_ids_value = obj;
    }
    console.log("receiver_ids_value:::" + receiver_ids_value);
    let username_real_name = username + "@" + real_name;
    receiver_ids.val(receiver_ids_value);
    let result = "<span style='color: mediumspringgreen'>" + username_real_name + ";</span><br>";
    $('.search_result_div').append(result);
    let search_div = $(".search_div");
    search_div.html("");
    search_div.hide();
    $(".receiver_search_content").hide();
    $('#search_result_receiver').val(real_name);
}

function system_message_confirm(obj_id) {
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    let url = '/report/system_message_confirm/';
    if (typeof url === "string" && typeof record_id === "number") {
        let confirm_result = confirm("确认查看？");
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

function system_message_hidden(obj_id, hidden_user) {
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    let url = '/report/system_message_hidden/';
    if (typeof record_id === "number") {
        let confirm_result = confirm("确认不再显示？");
        if (confirm_result) {
            let form_data = new FormData();
            form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
            form_data.append("record_id", record_id);
            form_data.append("hidden_user", hidden_user);
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
/**
 * 按照id 删除一条记录
 * @param url
 * @param obj_id
 */
function del(url, obj_id) {
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof url === "string" && typeof record_id === "number") {
        let confirm_result = confirm("确定删除本条记录?");
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

/**
 * 按照提交一条记录
 * @param url
 * @param obj_id
 */
function submit(url, obj_id) {
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof url === "string" && typeof record_id === "number") {
        let confirm_result = confirm("确定提交填报记录?提交之后将进入负责人审核系统.");
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

/**
 * 按照id 注销一条提交记录
 * @param url
 * @param obj_id
 */
function cancel(url, obj_id) {
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof url === "string" && typeof record_id === "number") {
        let confirm_result = confirm("确定注销本次提交申请?");
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

function cancel_return(url, obj_id) {
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof url === "string" && typeof record_id === "number") {
        let confirm_result = confirm("确定撤销注销提交记录的申请?");
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


function review(url, obj_id) {
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof url === "string" && typeof record_id === "number") {
        let confirm_result = confirm("确定审核通过本次信息?");
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

/**
 * 取消确认审核
 * @param url
 * @param obj_id
 */
function review_cancel(url, obj_id) {
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof url === "string" && typeof record_id === "number") {
        let confirm_result = confirm("确定取消对本记录的审核?");
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

function report_confirm(url, obj_id) {
    let record_id = 0;
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof url === "string" && typeof record_id === "number") {
        let confirm_result = confirm("确定通过本次信息?");
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
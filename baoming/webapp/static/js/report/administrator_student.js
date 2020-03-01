/**
 * 按照id 删除一条记录
 * @param url
 * @param obj_id
 */
function admin_del_student(obj_id) {
    let record_id = 0;
    let url = '/report/admin_del_student/';
    if (typeof obj_id === "string") {
        record_id = parseInt(obj_id);
    } else {
        record_id = obj_id;
    }
    if (typeof record_id === "number") {
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

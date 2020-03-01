function delete_force(type) {
    let url = '/report/delete_force/';
    let confirm_result = confirm("确定要执行本次删除操作?");
    if (confirm_result) {
        let form_data = new FormData();
        form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
        form_data.append('delete_force_type', type);
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
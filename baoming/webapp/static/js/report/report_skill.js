function report_skill() {
    /**
     * 获取技能列表
     * @type {string}
     */
    let url = '/report/report_kill_info/';
    // let form_data = new FormData();
    // form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
    // form_data.append("uid", obj.id);
    $.ajax({
        url: url,
        type: 'GET',
        // data: form_data,
        data: {},
        processData: false, // tell jquery not to process the data
        contentType: false, // tell jquery not to set contentType
        success: function(data) {
            alert(data);
            if (data.status) {
                console.log(data);
            } else {
                alert("删除失败！");
            }
        }
    });

}
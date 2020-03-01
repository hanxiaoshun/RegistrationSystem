/**
 * json 到 form 表单的渲染
 * @param form_id
 * @param json_obj
 */
function json2form(form_id, json_obj) {
    // 为对应的input 赋值
    let form_inputs = $("#" + form_id + " input");
    for (let i = 0; i < form_inputs.length; i++) {
        for (let k in json_obj) {
            if (form_inputs[i].name === k) {
                form_inputs[i].value = json_obj[k];
            }
        }
    }
    // 为对应的textarea 赋值
    let form_textarea = $("#" + form_id + " textarea");
    for (let i = 0; i < form_textarea.length; i++) {
        for (let k in json_obj) {
            if (form_textarea[i].name === k) {
                form_textarea[i].value = json_obj[k];
            }
        }
    }
}
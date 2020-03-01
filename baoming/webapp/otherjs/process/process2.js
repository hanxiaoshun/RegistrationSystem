var baseImport = "../../api/importExcel/";
var create = baseImport + "create";
var importFile = baseImport + "import";

/**
 * 创建数据批次
 */
function ajaxButton_create_data_batch(){
    $.ajax({
        url: create,
        type: 'POST',
        tradition: true,
        data: $("#editForm").serialize(),
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            var strs = JSON.stringify(arg);
            // var obj_data = JSON.parse(arg);
            if (arg > 0) {
                alert("操作成功");
            } else {
                alert("操作失败");
            }
        }
    });
}
function create_data_batch() {
    var className = "bounceInDown";
    $('#dialogBg').fadeIn(100);
    $('#dialog').removeAttr('class').addClass('animated ' + className + '').fadeIn();
    $("#editForm").empty("");
    var addContent = "<ul class='editInfos'>"+
        "<li><label><font color='#ff0000'>* </font>核查名称：<input type='text' name='name' required='required' value='' id='add_real_name' class='ipt' /></label><label style='color:red' id='val_add_real_name'></label></li>"+
        "<li><input type='button' value='确认提交' onclick='ajaxButton_create_data_batch();' class='submitBtn' /></li></ul>";
    $("#editForm").append(addContent);
}



/**
 * 备案数据导入
 */
function ajaxButton_import_data_batch(){
	var formData = new FormData($("#uploadForm")[0]);
     $.ajax({
         url: "../../api/importExcel/import",
         type: 'POST',
         data: formData,
         contentType: false,
         processData: false,
         success: function (arg) {
             /*var callback_dic = $.parseJSON(arg);*/
             /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
             // var strs = JSON.stringify(arg);
             // var obj_data = JSON.parse(arg);
             if (arg == 1) {
                 alert("操作成功");
             } else {
                 alert("操作失败");
             }
         }
     });
}
//onclick='ajaxButton_import_data_batch();'
function import_access_data() {
    var className = "bounceInDown";
    $('#dialogBg').fadeIn(100);
    $('#dialog').removeAttr('class').addClass('animated ' + className + '').fadeIn();
    $("#editForm").empty("");
    var addContent = "<ul class='editInfos'>"+
        "<li><label><font color='#ff0000'>* </font>选择文件：<input type='file' name='file' id='uploadForm' required='required' value='' id='add_real_name' class='ipt' /></label><label style='color:red' id='val_add_real_name'></label></li>"+
        "<li><input type='submit' value='确认导入'  class='submitBtn' /></li></ul>";
    $("#editForm").attr("action",importFile);
    $("#editForm").attr("method","POST");
    $("#editForm").attr("enctype","multipart/form-data");
    $("#editForm").append(addContent);
}

//--------------------------------------------
var baseexportCsv = "../../api/exportCsv/";
var move = baseexportCsv + "move";
var batchid = $("#batchid").val();
function data_ready_sampled(){
	var cybatchid = $("#cybatchid").val();
    $.ajax({
        url: move,
        type: 'POST',
        tradition: true,
        data: {cybatchid:cybatchid},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            // var strs = JSON.stringify(arg);
            // var obj_data = JSON.parse(arg);
            if (arg == 1) {
                alert("操作成功");
            } else {
                alert("操作失败");
            }
        }
    });
}

var baseipCheck= "../../api/ipCheck/";
var ipcheck = baseipCheck + "ipcheck";
function check_ip_domain(){
	var cybatchid = $("#cybatchid").val();
    $.ajax({
        url: ipcheck,
        type: 'POST',
        tradition: true,
        data: {cybatchid:cybatchid},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            // var strs = JSON.stringify(arg);
            // var obj_data = JSON.parse(arg);
            if (arg == 1) {
                alert("操作成功");
            } else {
                alert("操作失败");
            }
        }
    });
}

var baseaccessResult= "../../api/accessResult/";
var resultUrl = baseaccessResult + "result";
function check_access_info(){
	var cybatchid = $("#cybatchid").val();
    $.ajax({
        url: resultUrl,
        type: 'POST',
        tradition: true,
        data: {cybatchid:cybatchid},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            // var strs = JSON.stringify(arg);
            // var obj_data = JSON.parse(arg);
            if (arg == 1) {
                alert("操作成功");
            } else {
                alert("操作失败");
            }
        }
    });
}

var basesubjectResult= "../../api/subjectResult/";
var resultUrl2 = basesubjectResult + "result";
function check_mainBody_info(){
	var cybatchid = $("#cybatchid").val();
    $.ajax({
        url: resultUrl2,
        type: 'POST',
        tradition: true,
        data: {cybatchid:cybatchid},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            // var strs = JSON.stringify(arg);
            // var obj_data = JSON.parse(arg);
            if (arg == 1) {
                alert("操作成功");
            } else {
                alert("操作失败");
            }
        }
    });
}

var basecontactResult= "../../api/contactResult/";
var resultUrl3 = basecontactResult + "result";
function check_contacts_info(){
	var cybatchid = $("#cybatchid").val();
    $.ajax({
        url: resultUrl3,
        type: 'POST',
        tradition: true,
        data: {cybatchid:cybatchid},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            // var strs = JSON.stringify(arg);
            // var obj_data = JSON.parse(arg);
            if (arg == 1) {
                alert("操作成功");
            } else {
                alert("操作失败");
            }
        }
    });
}



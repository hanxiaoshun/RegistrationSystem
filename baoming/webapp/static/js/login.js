/*
function $(id){return document.getElementById(id)}

function user_input(){
	var name = $("id").value;
	var password = $("password").value;
	if(name=="" || password==""){
		alert("用户名或密码不能为空！");
		return false;
		}else{
			return true;
			}
	}

*/
function LoadBlogParts(){
	var swfUrl = "http://localhost:8080/icpcheck-web/static/swf/honehone_clock_tr.swf";
	var swfTitle = "honehoneclock";
	var sUrl = swfUrl;
	var sHtml = "";
	sHtml += '<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://localhost:8080/icpcheck-web/static/swf/swflash.cab#version=8,0,0,0" width="160" height="70" id="' + swfTitle + '" align="middle">';
	sHtml += '<param name="allowScriptAccess" value="always" />';
	sHtml += '<param name="movie" value="' + sUrl + '" />';
	sHtml += '<param name="quality" value="high" />';
	sHtml += '<param name="bgcolor" value="#ffffff" />';
	sHtml += '<param name="wmode" value="transparent" />';
	sHtml += '<embed wmode="transparent" src="' + sUrl + '" quality="high" bgcolor="#ffffff" width="160" height="70" name="' + swfTitle + '" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" />';
	sHtml += '</object>';
	document.write(sHtml);
}
function getBasePath(){ 
	var obj=window.location; 
	var contextPath=obj.pathname.split("/")[1]; 
	var basePath=obj.protocol+"//"+obj.host+"/"+contextPath; 
	return basePath; 
}
function loginUser(){
	
//	loginUrl = "../api/user/loginUser";
	loginUrl = "../api/user/loginUserAuth";
//	$("#id").val = 
	$.ajax({
        url:loginUrl,
        type:'POST',
        tradition:true,
        data:$('#loginForm').serialize(),
        //processData: false,  // 不处理数据
        //contentType: false   // 不设置内容类型
        success: function (arg) {    //如果程序执行成功就会执行这里的函数
            /*var callback_dic = $.parseJSON(arg);*/
            /*var strs = JSON.stringify(arg)*/
        	console.info(arg);
            var obj = JSON.parse(arg);
            if(obj){
            	console.info(obj.response_time);
            	console.info(obj._grwitness);
            	console.info(obj._grsole);
            	console.info(obj.username);
            	console.info(obj.accountId);
//            	var cookietime = new Date();
//            	cookietime.setTime(date.getTime() + (60 * 60 * 1000)); //保存一个小时
            	$.cookie("response_time", obj.response_time, {expires:2,path:"/"}); //保存两天
            	$.cookie("_grwitness", obj._grwitness, {expires:2,path:"/"});
            	$.cookie("_grsole", obj._grsole, {expires:2,path:"/"});
            	$.cookie("username", obj.username, {expires:2,path:"/"});
            	$.cookie("accountId", obj.accountId, {expires:2,path:"/"});
            	$.session.set("session_time", obj.response_time);
                $.session.set("username", obj.username);
                $.session.set("accountId", obj.accountId);
                window.location.replace("../page/index.html");
                /*window.location.reload();*/
            }else{
                alert('失败');
                alert(obj.error); //把错误的信息从后台提出展示出来
            }
        }
    });
}


/**********HTML初始化后为其按钮绑定函数**********/



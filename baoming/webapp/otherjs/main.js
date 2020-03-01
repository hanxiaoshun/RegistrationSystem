$(function($){
	
	var username = $.session.get("username");
	if(username){
		$("#welcome_user").text("欢迎:  "+username);
		console.log(username);
	}else{
		$("#userLogin").attr("href","../main/to_login")
		$("#welcome_user").text("请登录");
	}
});


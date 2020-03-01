var manage_theme = '密码';
var base_url = "../../api/user/";
$('#manage_title').text(manage_theme+'管理');	
function getSeesionName(){
	return $.session.get("username");
}	
var w,h,className;
function getSrceenWH(){
    w = $(window).width();
    h = $(window).height();
    $('#dialogBg').width(w).height(h);
}

window.onresize = function(){
    getSrceenWH();
}
$(window).resize();

$(function(){
	$('#sideMenu').sideToggle({
        moving: '#sideMenuContainer',
        direction: 'right'
    });
    getSrceenWH();
    //显示弹框
    $('.box a').click(function(){
        className = $(this).attr('class');
        $('#dialogBg').fadeIn(100);
        $('#dialog').removeAttr('class').addClass('animated '+className+'').fadeIn();
        /*$("#editForm").attr('action',addUrl);*/
        var textStr = $("#operationTitle").text();
        if (textStr !== null || textStr !== undefined || textStr !== '' || textStr != "添加"+manage_theme) {
        $("#operationTitle").text('添加'+manage_theme);
        }
        $("#editForm").empty();
        $('#editForm').append(addContent);
    });

     //关闭弹窗
    $('.claseDialogBtn').click(function(){
    $('#dialog').addClass('bounceOutUp').fadeOut();
        $('#dialog').addClass('bounceOutUp').fadeOut();
        $('#dialogBg').fadeOut();
        /*$('#dialogBg').fadeOut(50,function(){
            $('#dialog').addClass('bounceOutUp').fadeOut();
        });*/
        $("#operationTitle").text("");
    });

	var username = getSeesionName();
	if(username){
		$("#welcome_user").text("欢迎:  "+username);
//		console.log(username);
	}else{
		$("#username").attr("href","../main/to_login")
		$("#welcome_user").text("请登录");
	}
	
	
     getData1();
 });
 
function getData1(){
    var uid=$.Request("uid");
    return uid;
}

function resetpass(){
	var uid = getData1();
	var new_pass = $("#new_pass").val();
	var resetUrl = base_url+"resetPasswd";
	$.ajax({
        url:resetUrl,
        type:'POST',
        tradition:true,
        data:{"uid":uid, "new_pass":new_pass},
        //processData: false,  // 不处理数据
        //contentType: false   // 不设置内容类型
        success: function (arg) {    //如果程序执行成功就会执行这里的函数
            /*var callback_dic = $.parseJSON(arg);*/
            /*var strs = JSON.stringify(arg)*/
            var obj = JSON.parse(arg)
            console.info(obj)
            if(obj == 1){
                console.log('-----------------------',obj)
                $("#resetpass").attr("hidden","hidden");
                $("#resetStatus").removeAttr("hidden");
//                window.location.reload();
//                var set_id = 'set_'+ obj.website_identification_code
//                $('#'+set_id).text('进行中...')
//                $('#'+set_id).attr('disabled','disabled')
            }else{
                alert('失败');
                alert(obj); //把错误的信息从后台提出展示出来
            }
        }
    });
}
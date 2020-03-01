	var base_url = "../api/user/";
	var data_list_role = "../api/role/list";
	var addUrl = base_url+"addUser";
	var cancelUser = base_url+"cancelUser";
	var detailUrl = base_url+"findById";
	var updateUrl = base_url+"updateUser";
	var getOrganizationInfoUrl = base_url+"getOrganizationInfo";
	var accessProviderlist = "../api/user/accessProviderlist";
	var provincialAdministrationlist = "../api/user/provincialAdministrationlist";
	var verificationInstitutionlist = "../api/user/verificationInstitutionlist";
	var deleteUrl = '/delete_business_users/';
	var update_pass_Url = '/update_users_passwd/';
	
	var manage_theme = '用户';
	$('#manage_title').text(manage_theme+'管理');	

function getSessionName(){
	return $.session.get("username");
}	

function checkUndefined(obj){
	if(obj == undefined){
		return "";
	}else if(obj == "undefined"){
		return "";
	}else if(obj == "null"){
		return "";
	}else{
		return obj;
	}
}

	var sessionName = getSessionName();
	
    var addContent = "<ul class='editInfos'><li><label><font color='#ff0000'>* </font>账户：<input type='text' name='account' required='required' value='' id='add_real_account' class='ipt' /></label><label style='color:red' id='val_add_real_account'></label></li>"+
    "<li><label><font color='#ff0000'>* </font>姓名：<input type='text' name='username' required='required' value='' id='add_real_name' class='ipt' /></label><label style='color:red' id='val_add_real_name'></label></li>"+
    "<li><label><font color='#ff0000'>* </font>密码：<input type='password' name='password' required='required' value='' id='add_password' class='ipt' /></label><label style='color:red' id='val_add_password'></label></li>"+
    "<li><label><font color='#ff0000'>* </font>确认密码：<input type='password' name='chenckPassword' required='required' value='' id='check_password' class='ipt' /></label><label style='color:red' id='val_add_password'></label></li>"+
//    "<li><label><font color='#ff0000'>* </font>邮箱：<input type='text' name='email' required='required' value='shunzi@aic.cn' id='add_email' class='ipt' /></label><label style='color:red' id='val_add_email'></label></li>"+
//    "<li><label><font color='#ff0000'>* </font>手机：<input type='text' name='contact' required='required' value='1888888888'  id='add_phone' class='ipt' /></label><label style='color:red' id='val_add_phone'></label></li>"+
    "<li><label><font color='#ff0000'>&nbsp;&nbsp;</font><span id='span_x'>角色</span>：" +
	    "<select-div.css name='userType' style='width:158px' required class='ipt' required='required' onchange='selectOrg(this.options[this.options.selectedIndex].value);'>" +
		"<option selected='selected'>请选择用户类型</option>" +
		"<option value ='1' >接入商</option>" +
		"<option value ='2' >核查机构</option>" +
		"<option value ='3' >省管局</option>" +
		"<option value ='4' >系统用户</option>" +
	"</select-div.css></label></li>"+
	"<li><label><font color='#ff0000'>&nbsp;</font><span id='span_x'>单位</span>：" +
    "<select-div.css name='orgid' style='width:158px' id='loadAddOrgInfo' required class='ipt'>" +
    	"<option value ='-1' selected='selected'>请选择单位</option>" +
  	"</select-div.css></label></li>"+
    "<li hidden='hidden'><label><font color='#ff0000'>* </font>当前用户名：<input type='text' name='sessionName' required='required' value=" + sessionName + "  id='add_phone' class='ipt' /></label><label style='color:red' id='val_add_phone'></label></li>"+
    "<li><input type='button' value='确认提交' onclick='ajaxButton_set(1)' class='submitBtn' /></li></ul>"

function to_detail_func(data,type,orgType){
    	var uid = data.userid
    	$.ajax({
            url:getOrganizationInfoUrl,
            type:'GET',
            tradition:true,
            data:{uid:uid},
            success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
			                    console.log(arg);
			                    var orgName = "";
			                    var strs = JSON.stringify(arg)
			                    var obj_data = JSON.parse(arg);
			                    if(obj_data.orgType == 1){
			                    	var orgAccessProvider = obj_data.OrgObject
			                    	orgName = orgAccessProvider.dwmc;
			                    }else if(obj_data.orgType == 2){
			                    	var orgProvincialAdministration = obj_data.OrgObject
			                    	orgName = orgProvincialAdministration.mc;
			                    }else if(obj_data.orgType == 3){
			                    	var orgProvincialAdministration = obj_data.OrgObject
			                    	orgName = orgProvincialAdministration.name;
			                    }else{
			                    	orgName = "暂无单位信息";
			                    }
										    $('#editForm').append("<ul class='editInfos'><li hidden='hidden'><label><font color='#ff0000'>* </font>ID：<input type='text' name='userid' required value="+data.userid+" class='ipt' /></label></li>"+
										    "<li><label><font color='#ff0000'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* </font><span id='span_x'>账户</span>：<input type='text' name='account' id='edit_account' required value="+data.account+" class='ipt' readonly='readonly'></label></li>"+
										    "<li><label><font color='#ff0000'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* </font><span id='span_x'>姓名</span>：<input type='text' name='username' id='edit_real_name' required value="+data.username+" class='ipt' ></label></li>"+
//										    "<li><label><font color='#ff0000'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* </font><span id='span_x'>昵称</span>：<input type='text' name='status' id='edit_nickname' required class='ipt' value="+data.status+" ></label></li>"+
										//    "<li><label><font color='#ff0000'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* </font><span id='span_x'>邮箱</span>：<input type='text' name='email' id='edit_email' required class='ipt' value="+data.email+" ></label></li>"+
										//    "<li><label><font color='#ff0000'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* </font><span id='span_x'>手机</span>：<input type='text' name='contact' id='edit_phone' required class='ipt' value="+data.contact+" ></label></li>"+
										//    "<li><label><font color='#ff0000'>* </font><span id='span_x'>证件类型</span>：<input type='text' name='cardType' id='edit_level' required class='ipt' value="+checkUndefined(data.cardType)+" ></label></li>"+
										//    "<li><label><font color='#ff0000'>* </font><span id='span_x'>证件号码</span>：<input type='text' name='cardNumber' id='edit_level' required class='ipt' value="+checkUndefined(data.cardNumber)+" ></label></li>"+
										//    "<li><label><font color='#ff0000'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* </font><span id='span_x'>角色</span>：<input type='text' name='roleId' id='edit_level' required class='ipt' value="+data.roleId+" ></label></li>"+
										    "<li><label><font color='#ff0000'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* </font><span id='span_x'>角色</span>：" +
										    "<select-div.css name='roleid' style='width:158px' id='loadRoleInfo' required class='ipt'>" +
										    	"<option value ='-1' selected='selected'>请选择角色</option>" +
										  	"</select-div.css></label></li>"+
										  	"<li><label><font color='#ff0000'>&nbsp;* </font><span id='span_x'>所属单位</span>：" +
										    "<select-div.css name='orgid' style='width:158px' id='loadOrgInfo' required class='ipt'>" +
										    	"<option value ='-1' selected='selected'>请选择单位</option>" +
										  	"</select-div.css></label></li>"+
										  	
//										    "<li><label><font color='#ff0000'>* </font><span id='span_x'>所属单位</span>：<input type='text' name='orgid' id='edit_level' required class='ipt' value="+orgid+" ></label></li>"+
										    "<li><label><font color='#ff0000'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* </font><span id='span_x'>备注</span>：" +
										//    "<input type='text' name='description' id='edit_level' required class='ipt' value="+data.description+" >" +
										    "<textarea style='width:158px' rows='3' cols='20' name='description' id='edit_level' required class='ipt' >" +
										    checkUndefined(data.remark) +
										    "</textarea>" +
										    "</label></li>"+
										    "<li><input id='ajaxButton' type='button' value='确认提交' onclick='ajaxButton_set(2)' class='submitBtn' /></li></ul>");
										    
										    loadRoleInfo(data.roleid); 
										    loadOrgInfo(data.orgid,orgType); 
										    if (type == 1){
			                                    $('#editForm').find('input,textarea').attr('readonly',"readonly");
			                                    $('#loadRoleInfo').attr({onfocus:"this.defaultIndex=this.selectedIndex;",onchange:"this.selectedIndex=this.defaultIndex;"});
			                                    $('#ajaxButton').remove();
			                                }
            }
    	});
    }
    
    function selectOrg(obj){
    	var orgType = parseInt(obj);
    	if(orgType == 1){
    		$("#loadAddOrgInfo").empty("");
    		$("#loadAddOrgInfo").append("<option selected>请选择单位</option>");
    		$.ajax({
                url:accessProviderlist,
                type:'GET',
                tradition:true,
                data:{},
                success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
                	var strs = JSON.stringify(arg)
    			                    var obj_data = JSON.parse(arg);
    			                    if(obj_data instanceof Array){
    			                        $.each(obj_data,function(i,n){
    			                        	$("#loadAddOrgInfo").append("<option value="+n.id+">"+n.dwmc+"</option>");
    			                        });
//    			                         $("#select_item").attr("onfocus","javascript:void(0)");
    			                    }else{
    			                        alert(); //把错误的信息从后台提出展示出来
    			                    }
                 			}
        			});
    	}else if(orgType == 2){
    		$("#loadAddOrgInfo").empty("");
    		$("#loadAddOrgInfo").append("<option selected>请选择单位</option>");
    		$.ajax({
                url:verificationInstitutionlist,
                type:'GET',
                tradition:true,
                data:{},
                success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
    			                    var strs = JSON.stringify(arg)
    			                    var obj_data = JSON.parse(arg);
    			                    if(obj_data instanceof Array){
    			                        $.each(obj_data,function(i,n){
    			                        	$("#loadAddOrgInfo").append("<option value="+n.id+">"+n.name+"</option>");
    			                        });
//    			                         $("#select_item").attr("onfocus","javascript:void(0)");
    			                    }else{
    			                        alert(); //把错误的信息从后台提出展示出来
    			                    }
                 			}
        			});
    	}else if(orgType == 3){
    		$("#loadAddOrgInfo").empty("");
    		$("#loadAddOrgInfo").append("<option selected>请选择单位</option>");
    		$.ajax({
                url:provincialAdministrationlist,
                type:'GET',
                tradition:true,
                data:{},
                success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
    			                    var strs = JSON.stringify(arg)
    			                    var obj_data = JSON.parse(arg);
    			                    if(obj_data instanceof Array){
    			                        $.each(obj_data,function(i,n){
    			                        		$("#loadAddOrgInfo").append("<option value="+n.id+">"+n.mc+"</option>");
    			                        });
    			                    }else{
    			                        alert(); //把错误的信息从后台提出展示出来
    			                    }
                 			}
        			});
    	}else{
    		$("#loadAddOrgInfo").empty("");
    		$("#loadAddOrgInfo").append("<option selected>请选择单位</option>");
    		$("#loadAddOrgInfo").append("<option value='40001' selected='selected'>天津国瑞数码</option>");
    	}
    	
    }
//    <!-- 		  orgType 1 接入商 2 核查单位 3 管局用户 4系统用户-->
    function loadOrgInfo(orgid,orgType){
    	if(orgType == 1){
    		$("#loadOrgInfo").empty("");
    		$.ajax({
                url:accessProviderlist,
                type:'GET',
                tradition:true,
                data:{},
                success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
    			                    var strs = JSON.stringify(arg)
    			                    var obj_data = JSON.parse(arg);
    			                    if(obj_data instanceof Array){
    			                        $.each(obj_data,function(i,n){
    			                        	if(n.id == orgid){
    			                        		$("#loadOrgInfo").append("<option value="+n.id+" selected='selected'>"+n.dwmc+"</option>");
    			                        	}else{
    			                        		$("#loadOrgInfo").append("<option value="+n.id+">"+n.dwmc+"</option>");
    			                        	}
    			                        });
//    			                         $("#select_item").attr("onfocus","javascript:void(0)");
    			                    }else{
    			                        alert(); //把错误的信息从后台提出展示出来
    			                    }
                 			}
        			});
    	}else if(orgType == 2){
    		$("#loadOrgInfo").empty("");
    		$.ajax({
                url:verificationInstitutionlist,
                type:'GET',
                tradition:true,
                data:{},
                success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
    			                    var strs = JSON.stringify(arg)
    			                    var obj_data = JSON.parse(arg);
    			                    if(obj_data instanceof Array){
    			                        $.each(obj_data,function(i,n){
    			                        	if(n.id == orgid){
    			                        		$("#loadOrgInfo").append("<option value="+n.id+" selected='selected'>"+n.name+"</option>");
    			                        	}else{
    			                        		$("#loadOrgInfo").append("<option value="+n.id+">"+n.name+"</option>");
    			                        	}
    			                        });
//    			                         $("#select_item").attr("onfocus","javascript:void(0)");
    			                    }else{
    			                        alert(); //把错误的信息从后台提出展示出来
    			                    }
                 			}
        			});
    	}else if(orgType == 3){
    		$("#loadOrgInfo").empty("");
    		$.ajax({
                url:provincialAdministrationlist,
                type:'GET',
                tradition:true,
                data:{},
                success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
    			                    var strs = JSON.stringify(arg)
    			                    var obj_data = JSON.parse(arg);
    			                    if(obj_data instanceof Array){
    			                        $.each(obj_data,function(i,n){
    			                        	if(n.id == orgid){
    			                        		$("#loadOrgInfo").append("<option value="+n.id+" selected='selected'>"+n.mc+"</option>");
    			                        	}else{
    			                        		$("#loadOrgInfo").append("<option value="+n.id+">"+n.mc+"</option>");
    			                        	}
    			                        });
//    			                         $("#select_item").attr("onfocus","javascript:void(0)");
    			                    }else{
    			                        alert(); //把错误的信息从后台提出展示出来
    			                    }
                 			}
        			});
    		
    	
    	}else{
    		$("#loadOrgInfo").empty("");
    		$("#loadOrgInfo").append("<option value='40001' selected='selected'>天津国瑞数码</option>");
    	}
    }
    
    
    function loadRoleInfo(roleid){
    	$.ajax({
            url:data_list_role,
            type:'GET',
            tradition:true,
            data:{},
            success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
			                    console.log(arg);
			                    var strs = JSON.stringify(arg)
			                    var obj_data = JSON.parse(arg);
			                    console.log("role"+obj_data);
			                    if(obj_data instanceof Array){
			                        $.each(obj_data,function(i,n){
			                        	if(n.id == roleid){
			                        		$("#loadRoleInfo").append("<option value="+n.id+" selected='selected'>"+n.name+"</option>");
			                        	}else{
			                        		$("#loadRoleInfo").append("<option value="+n.id+">"+n.name+"</option>");
			                        	}
			                        });
//			                         $("#select_item").attr("onfocus","javascript:void(0)");
			                    }else{
			                        alert(); //把错误的信息从后台提出展示出来
			                    }
             			}
    			});
    }
    
    $("#loadExchange").change(function(){
    	var exchange_code = $(this).val();
    	 $.ajax({
             url:data_list_role,
             type:'GET',
             tradition:true,
             data:{},
             success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
                     console.log(arg);
                     var strs = JSON.stringify(arg)
                     var obj_data = JSON.parse(arg);
                     console.log(obj_data);
                     if(obj_data instanceof Array){
                         $.each(obj_data,function(i,n){
                             $("#loadRoleInfo").append("<option value="+n.fields.code+">"+n.fields.name+"</option>");
                         });
                          $("#select_item").attr("onfocus","javascript:void(0)");
                     }else{
                         alert(); //把错误的信息从后台提出展示出来
                     }
              }
    });
    	
    });
    
    
    $("#chooseExchange").change(function(){
        $("#chooseTransactionPair").empty();
        var exchange_code = $(this).val();
        var data_list_url = '/get_exchange_pair_list';
               $.ajax({
                        url:data_list_url,
                        type:'GET',
                        tradition:true,
                        data:{"exchange_code":exchange_code},
                        success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
                                console.log(arg);
                                var strs = JSON.stringify(arg)
                                var obj_data = JSON.parse(arg);
                                console.log(obj_data);
                                if(obj_data instanceof Array){
                                    $.each(obj_data,function(i,n){
                                        $("#chooseTransactionPair").append("<option value="+n.fields.code+">"+n.fields.name+"</option>");
                                    });
                                     $("#select_item").attr("onfocus","javascript:void(0)");
                                }else{
                                    alert(); //把错误的信息从后台提出展示出来
                                }
                         }
               });
    });
    
$(document).ready(function(){
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
            $("#editForm").empty("");
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
	            $("#editForm").empty("");
	            $("#operationTitle").text("");
        });

    	var username = getSessionName();
    	if(username){
    		$("#welcome_user").text("欢迎:  "+username);
//    		console.log(username);
    	}else{
    		$("#username").attr("href","../main/to_login")
    		$("#welcome_user").text("请登录");
    	}
    	$("#tbody_id").empty("");
    	datalist(1);
	});

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

 /*   function delete_obj(obj){
    	var confirm_result = confirm("确定对该记录进行操作?");
    	if (confirm_result){
    		 $.ajax({
           	  url:deleteUrl,
                   type:'POST',
                   tradition:true,
                   data:{"id":obj},
                   success: function (arg) {    //如果程序执行成功就会执行这里的函数
                       var callback_dic = $.parseJSON(arg);
                       var strs = JSON.stringify(arg)
                       var obj = JSON.parse(arg)
                       console.info(obj)
                       if(obj.status){
                           alert('该记录操作成功');
                           window.location.reload();
                       }else{
                           alert('该记录操作失败');
                           alert(obj.error); //把错误的信息从后台提出展示出来
                       }
                   }
                });
    	}
    }*/
    
    function cancel_obj(obj){
    	var confirm_result = confirm("确定对该记录进行操作?");
    	if (confirm_result){
    		 $.ajax({
           	  url:cancelUser,
                   type:'POST',
                   tradition:true,
                   data:{"uid":obj},
                   success: function (arg) {    //如果程序执行成功就会执行这里的函数
                       /*var callback_dic = $.parseJSON(arg);*/
                       /*var strs = JSON.stringify(arg)*/
                       var obj = JSON.parse(arg)
//                       console.info(obj)
                       if(obj == 1){
                           alert('该记录操作成功');
                           window.location.reload();
                       }else{
                           alert('该记录操作失败');
                           alert(obj.error); //把错误的信息从后台提出展示出来
                       }
                   }
                });
    	}
    }

    function ajaxButton_set(submitType){
        if(submitType == 1){
            /*var fd = new FormData(document.querySelector("form"));*/
            /*var form = document.getElementById("editForm");*/
            /*var formData = new FormData(form);*/
            /*var form = new FormData($("#editForm"));*/
            /*fd.append("CustomField", "This is some extra data");*/
//            console.info($('#editForm').serialize());
        	var data = $('#editForm').serialize();
            $.ajax({
                url:addUrl,
                type:'POST',
                tradition:true,
                data:data,
                //processData: false,  // 不处理数据
                //contentType: false   // 不设置内容类型
                success: function (arg) {    //如果程序执行成功就会执行这里的函数
                    /*var callback_dic = $.parseJSON(arg);*/
                    /*var strs = JSON.stringify(arg)*/
                    var obj = JSON.parse(arg)
                    console.info(obj)
                    if(obj == 1){
                        alert('成功');
                        window.location.reload();
                    }else{
                        alert('失败');
                        alert(obj.error); //把错误的信息从后台提出展示出来
                    }
                    /*if(obj.status){
                        alert('成功');
                        window.location.reload();
                    }else{
                        alert('失败');
                        alert(obj.error); //把错误的信息从后台提出展示出来
                    }*/
                }
            });
        }else if(submitType == 2){
            /*var fd = new FormData(document.querySelector("form"));*/
            /*var form = new FormData($("#editForm")[0]);*/
            /*fd.append("CustomField", "This is some extra data");*/
            if(confirm("确定修改该记录?")){
                $.ajax({
                    url:updateUrl,
                    type:'POST',
                    tradition:true,
                    data:$('#editForm').serialize(),
                    //processData: false,  // 不处理数据
                    //contentType: false   // 不设置内容类型
                    success: function (arg) {    //如果程序执行成功就会执行这里的函数
                        /*var callback_dic = $.parseJSON(arg);*/
                        /*var strs = JSON.stringify(arg)*/
                        var obj = JSON.parse(arg)
                        console.info(obj)
                        if(obj == 1){
                            console.log('-----------------------',obj)
                            /*if(obj.process_id != ''){
                                $('#skip_html').click();
                            }*/
                            window.location.reload();
//                            var set_id = 'set_'+ obj.website_identification_code
//                            $('#'+set_id).text('进行中...')
//                            $('#'+set_id).attr('disabled','disabled')
                        }else{
                            alert('失败');
                            alert(obj); //把错误的信息从后台提出展示出来
                        }
                    }
                });
            }
        }else{
            return "xxxxxx"
        }
    }

    function edit_obj(obj,type,orgType){
         var className= "bounceInDown";
              $.ajax({
                        url:detailUrl,
                        type:'GET',
                        tradition:true,
                        data:{"uid":obj},
                        success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
                            /*var callback_dic = $.parseJSON(arg);*/
                            var strs = JSON.stringify(arg)
                            var obj_data = JSON.parse(arg);
                            console.log(obj_data);
                            /*console.info(obj_data[0].fields);
                            console.info(obj_data);*/
                            if(obj_data){
                                $('#dialogBg').fadeIn(100);
                                $('#dialog').removeAttr('class').addClass('animated '+className+'').fadeIn();
                                $("#editForm").attr('action',updateUrl);
                                var textStr = $("#operationTitle").text();
                                if (textStr !== null || textStr !== undefined || textStr !== '' || textStr != '修改'+manage_theme) {
                                    if (type == 1){
                                            $("#operationTitle").text("查看详情");
                                        }else{
                                            $("#operationTitle").text("修改"+manage_theme);
                                        }
                                }
                                $("#editForm").empty("");
                                to_detail_func(obj_data,type,orgType);
                                
                            }else{
                                alert(); //把错误的信息从后台提出展示出来
                            }

                        }
              });
       if(type == 3){
    	   url = "../page/user/resetpasswd.html?uid="+obj;//此处拼接内容
//    	   url = "../page/user/resetpasswd.html"; //此处拼接内容
    	   window.location.href = url;
       }
    }

    /*function AjaxSubmit_set(){
        var data_list = [
            {'name':'chenchao','age':18},
            {'name':'lisi','age':19},
            {'name':'wangwu','age':13}
        ];

        $.ajax({
            url:"/app01/ajax_submit_set/",
            type:'POST',
            tradition:true,
            data:{data:JSON.stringify(data_list)},
            success: function (arg) {    //如果程序执行成功就会执行这里的函数
                var callback_dic = $.parseJSON(arg);
                if(callback_dic.status){
                    alert('成功');
                }else{
                    alert(callback_dic.error); //把错误的信息从后台提出展示出来
                }
            }
        });
    }*/


    function get(obj,type){
         var className= "bounceInDown";
              $.ajax({
                        url:detailUrl,
                        type:'POST',
                        tradition:true,
                        data:{"uid":obj},
                        success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
                            /*var callback_dic = $.parseJSON(arg);*/
                            var strs = JSON.stringify(arg)
                            var obj_data = JSON.parse(arg);
                            /*console.info(obj_data[0].fields);
                            console.info(obj_data);*/
                            if(obj_data[0].fields){
                                var data_pk = obj_data[0].pk;
                                var data_fields = obj_data[0].fields;
                                $('#dialogBg').fadeIn(100);
                                $('#dialog').removeAttr('class').addClass('animated '+className+'').fadeIn();
                                $("#editForm").attr('action',editUrl);
                                var textStr = $("#operationTitle").text();
                                if (textStr !== null || textStr !== undefined || textStr !== '' || textStr != '修改'+manage_theme) {
                                    if (type == 1){
                                            $("#operationTitle").text("查看详情");
                                        }else{
                                            $("#operationTitle").text("修改"+manage_theme);
                                        }
                                }
                                $("#editForm").empty();
                                to_detail_func(data_pk,data_fields);
                                if (type == 1){
                                    $('#editForm').find('input,textarea').attr('readonly',"readonly");
                                    $('#ajaxButton').remove();
                                }
                            }else{
                                alert(); //把错误的信息从后台提出展示出来
                            }

                        }
              });
    }

    function reload_spider_data(){
        if(confirm("确定爬刷新记录?")){
                $.ajax({
                    url:reloadUrl,
                    type:'POST',
                    tradition:true,
//                    data:$('#editForm').serialize(),
                    //processData: false,  // 不处理数据
                    //contentType: false   // 不设置内容类型
                    success: function (arg) {    //如果程序执行成功就会执行这里的函数
                        /*var callback_dic = $.parseJSON(arg);*/
                        /*var strs = JSON.stringify(arg)*/
                        var obj = JSON.parse(arg)
                        console.info(obj)
                        if(obj.status){
                            alert('ok ', obj.msg);
                            console.log('-----------------------',obj)
                            window.location.reload();
//                            var set_id = 'set_'+ obj.website_identification_code
//                            $('#'+set_id).text('进行中...')
//                            $('#'+set_id).attr('disabled','disabled')
                        }else{
                            alert('失败');
                            alert(obj.error); //把错误的信息从后台提出展示出来
                        }
                    }
                });
         }
     }

function datalist(orgType){
	response_time = $.cookie("response_time"); //保存两天
	_grwitness = $.cookie("_grwitness");
	_grsole = $.cookie("_grsole");
	account = $.session.get("accountId");
//	loginUrl = "../api/user/loginUser";
	c_url = base_url+"listByAuth";
//	$("#id").val = 
	$.ajax({
        url:c_url,
        type:'GET',
        tradition:true,
//        data:$('#loginForm').serialize(),
        data:{account:account,orgType:orgType},
        beforeSend:function(XHR){
        	XHR.setRequestHeader("response_time", response_time);
        	XHR.setRequestHeader("_grwitness", _grwitness);
        	XHR.setRequestHeader("_grsole", _grsole);
        },
        //processData: false,  // 不处理数据
        //contentType: false   // 不设置内容类型
        success: function (arg) {    //如果程序执行成功就会执行这里的函数
            /*var callback_dic = $.parseJSON(arg);*/
            /*var strs = JSON.stringify(arg)*/
        	console.info(arg);
            var result = JSON.parse(arg);
            if(result){
                var obj = result.list;
                for(i in obj){
                	var obj_i = obj[i];
                	var accountStr = checkUndefined(obj_i.ACCOUNT);
                	if (accountStr.length > 7){
                		accountStr = accountStr.substring(0,8) + "...";
                	}
                	var addTimeStr = checkUndefined(obj_i.CREATETIME);
                	if(addTimeStr != ""){
                		addTimeStr = TimeObjectUtil.longMsTimeConvertToDateTime(checkUndefined(obj_i.CREATETIME))
                	}
                	var this_username = obj_i.USERNAME
//                	ORGID=1, ORGANIZATIONCITY=-1, PARENTUSERNAME=系统测试角色, ROLESTATUS=0, HOLDERSNTXT=实打实大, ORGANIZATIONPROVINCE=340000, ROLECODE=222, ROLENAME=默认角色, ORGANIZATIONID=1, ROLEDESCRIPTION=系统默认测试角色, ROW_ID=1, ACCOUNT=111, STATUS=0, PARENTID=1
                	var tr_str =
                	"<tr>" + 
                		"<td>" + i +"</td>" +
                		"<td>" + checkUndefined(accountStr) +"</td>" +
	                    "<td>" + checkUndefined(this_username) +"</td>" +
	                    "<td>" + checkUndefined(obj_i.STATUS) +"</td>" +
	                    "<td>" + checkUndefined(obj_i.ROLENAME) +"</td>" +
	                    "<td>" + checkUndefined(obj_i.ORGANIZATIONNAME) + "</td>" +
	                    "<td>" + checkUndefined(obj_i.PARENTUSERNAME) + "</td>" +
	                    "<td>" + addTimeStr + "</td>" +
	                    "<td style='text-align:center' >" +
	                        "<a href='javascript:void(0)' onclick='edit_obj("+obj_i.USERID+",1,"+orgType+")'><button style='background-color:#FFCCCC;border-radius: 5px;'>详情</button></a>" +
	                        "<a href='javascript:void(0)' onclick='edit_obj("+obj_i.USERID+",2,"+orgType+")'><button style='background-color:#FFCCCC;border-radius: 5px;'>修改</button></a>" +
	                        "<a href='javascript:void(0)' onclick='edit_obj("+obj_i.USERID+",3)'><button style='background-color:#FFCCCC;border-radius: 5px;'>重置密码</button></a>" +
	                        "<a href='javascript:void(0)' onclick='cancel_obj("+obj_i.USERID+")'><button style='background-color:#FFCCCC;border-radius: 5px;'>注销</button></a>" +
	                    "</td>" +
                	"</tr>";
                    $("#tbody_id").append(tr_str);
                }
                /*window.location.reload();*/
            }else{
                alert('失败');
                alert(obj.error); //把错误的信息从后台提出展示出来
            }
        }
    });
}

function searchByOrgType(){
	var orgType = $("#orgType").val();
	$("#tbody_id").empty("");
	datalist(orgType);
}
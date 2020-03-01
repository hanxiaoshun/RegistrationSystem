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

    	var username = $.session.get("username");
    	if(username){
    		$("#welcome_user").text("欢迎:  "+username);
    		console.log(username);
    	}else{
    		$("#username").attr("href","../main/to_login")
    		$("#welcome_user").text("请登录");
    	}
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

    function delete_obj(obj){
    	var confirm_result = confirm("确定对该记录进行操作?");
    	if (confirm_result){
    		 $.ajax({
           	  url:deleteUrl,
                   type:'POST',
                   tradition:true,
                   data:{"id":obj},
                   success: function (arg) {    //如果程序执行成功就会执行这里的函数
                       /*var callback_dic = $.parseJSON(arg);*/
                       /*var strs = JSON.stringify(arg)*/
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
    }

    function ajaxButton_set(submitType){
        if(submitType == 1){
            /*var fd = new FormData(document.querySelector("form"));*/
            /*var form = document.getElementById("editForm");*/
            /*var formData = new FormData(form);*/
            /*var form = new FormData($("#editForm"));*/
            /*fd.append("CustomField", "This is some extra data");*/
            console.info($('#editForm').serialize());
            $.ajax({
                url:addUrl,
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
                    if(obj.status){
                        alert('成功');
                        window.location.reload();
                    }else{
                        alert('失败');
                        alert(obj.error); //把错误的信息从后台提出展示出来
                    }
                }
            });
        }else if(submitType == 2){
            /*var fd = new FormData(document.querySelector("form"));*/
            /*var form = new FormData($("#editForm")[0]);*/
            /*fd.append("CustomField", "This is some extra data");*/
            if(confirm("确定爬取该记录?")){
                $.ajax({
                    url:editUrl,
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
                        if(obj.status){
                            alert('ok ', obj.msg);
                            console.log('-----------------------',obj)
                            if(obj.process_id != ''){
                                $('#skip_html').click();
                            }
//                            window.location.reload();
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
        }else{
            return "xxxxxx"
        }
    }

    function edit_obj(obj,type){
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


    function re_spider_edit_obj(obj,type){
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




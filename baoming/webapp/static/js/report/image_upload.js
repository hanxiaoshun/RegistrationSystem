function image_upload(type) {
    //关闭弹窗
    // csrfmiddlewaretoken: '{{ csrf_token }}'
    let form_data = new FormData();
    let photo_type = $('#photo_type').val();
    // let file_info = $('#imageUpload-form')[0].files[0];
    // form_data.append("picture_name", document.getElementById('picture_name').value);
    let file_before = document.getElementById('file');
    let file_info = document.getElementById('file').files[0];
    if (file_before.files.length === 0) {
        alert("未选择任何文件，请重新选择！");
    } else if (file_info.size > 10240000) {
        // if (type === 1) {
        //     if (file_info.size > 102400){
        //         alert("二寸大小不能超过100KB");
        //     }else{
        //         console.log("图片大小符合要求");
        //     }
        // }else{
        //     alert("图片大小不能超过700KB");
        // }
        alert("图片大小不能超过100KB");
    } else if (file_info.type !== 'image/jpeg') {
        alert("请上传后缀为 .jpg 格式的图片！");
    } else {
        form_data.append("csrfmiddlewaretoken", document.getElementsByName('csrfmiddlewaretoken')[0].value);
        form_data.append("file", document.getElementById('file').files[0]);
        if (type === 1) {
            form_data.append("file_type", "1");
        }
        let url = '/report/image_upload/';
        if (photo_type === 'val4') {
            url = '/report/image_upload_id_card/';

        } else if (photo_type === 'val5') {
            url = '/report/image_upload_id_card/';
        }
        $.ajax({
            url: url,
            type: 'POST',
            data: form_data,
            processData: false, // tell jquery not to process the data
            contentType: false, // tell jquery not to set contentType
            success: function(data) {
                if (data.status) {
                    if (photo_type === 'val1') {
                        let two_inch_photo = $("#two-inch-photo");
                        let two_inch_photo_value = $("#two_inch_photo");
                        two_inch_photo.attr('src', data.data);
                        two_inch_photo_value.val(data.picture);
                        // let imgo = document.getElementById('two-inch-photo');
                        // let height = imgo.naturalHeight;
                        // let width = imgo.naturalWidth;
                        //
                        // let img = null;
                        // img = document.createElement("img");
                        // document.body.insertAdjacentElement("beforeend", img);
                        // img.style.visibility = "hidden";
                        // img.src = data.data;
                        // let imgwidth = img.offsetWidth;
                        // let imgheight = img.offsetHeight;
                        // console.log("imgwidth::" + imgwidth);
                        // console.log("imgheight::" + imgheight);
                        //
                        // console.log("height::" + height);
                        // console.log("width::" + width);
                        //
                        // if (width < 420 && width > 380) {
                        //     if (height < 650 && height < 590) {
                        //         alert("照片尺寸判断正常，请继续提交");
                        //         //关闭模态框
                        //         let left = ($(window).width() * (1 - 0.35)) / 2;
                        //         let top = ($(window).height() * (1 - 0.5)) / 2;
                        //         $(".image-box").show().animate({
                        //             width: "-$(window).width()*0.35",
                        //             height: "-$(window).height()*0.5",
                        //             left: "-" + left + "px",
                        //             top: "-" + top + "px"
                        //         }, 1000, function () {
                        //             let width1 = $(window).width() * 0.35;
                        //             let height1 = $(window).height() * 0.5;
                        //             console.log(width1);
                        //             $(this).css({width: width1, height: height1}).hide();
                        //         });
                        //     } else {
                        //         alert("照片尺寸判断异常！请重新上传尺寸为：413*626像素 的二寸头像图片");
                        //         two_inch_photo.attr('src', "");
                        //         two_inch_photo.attr('alt', "请重新上传尺寸为：413*626像素 的图片");
                        //         two_inch_photo_value.val("");
                        //     }
                        // } else {
                        //     alert("照片尺寸判断异常！请重新上传尺寸为：413*626像素 的二寸头像图片");
                        //     two_inch_photo.attr('src', "");
                        //     two_inch_photo.attr('alt', "请重新上传尺寸为：413*626像素 的图片");
                        //     two_inch_photo_value.val("");
                        // }

                        // let start = (new Date()).getTime();
                        // while ((new Date()).getTime() - start < 500) {
                        // }
                        // let img = document.getElementById('two-inch-photo');
                        // w = img.naturalWidth;
                        // h = img.naturalHeight;
                        // console.log(w, h);
                        // if (h > 380 && h < 420) {
                        //     if (w > 590 && w < 650) {
                        //         alert("二寸照片上传成功");
                        //     } else {
                        //         alert("照片尺寸判断异常！请重新尝试");
                        //         $("#two-inch-photo").attr('src', "");
                        //         $("#two-inch-photo").attr('alt', "请重新上传尺寸为：413*626像素 的图片");
                        //         $("#two_inch_photo").val();
                        //     }
                        // } else {
                        //     alert("照片尺寸判断异常！请重新尝试");
                        //     $("#two-inch-photo").attr('src', "");
                        //     $("#two-inch-photo").attr('alt', "请重新上传尺寸为：413*626像素 的图片");
                        //     $("#two_inch_photo").val();
                        // }
                    } else if (photo_type === 'val2') {
                        alert("图片上传成功");
                        $("#certificate-photos").attr('src', data.data);
                        $("#certificate_photos").val(data.picture);
                        // $(".more_info").show();
                        $("#val2").val("更换资格证件照");
                    } else if (photo_type === 'val3') {
                        alert("图片上传成功");
                        $("#diploma-certificate-photos").attr('src', data.data);
                        $("#diploma_certificate_photos").val(data.picture);
                        // $(".more_info").show();
                        $("#val3").val("更换毕业证件照");
                        //关闭模态框
                    } else if (photo_type === 'val4') {
                        alert("图片上传成功");
                        $("#id-card-heads-photo").attr('src', data.data);
                        $("#id_card_heads_photo").val(data.picture);
                        // $(".more_info").show();
                        $("#val4").val("更换身份证正面照");
                        //关闭模态框
                    } else if (photo_type === 'val5') {
                        alert("图片上传成功");
                        $("#id-card-tails-photo").attr('src', data.data);
                        $("#id_card_tails_photo").val(data.picture);
                        // $(".more_info").show();
                        $("#val5").val("更换身份证反面照");
                        //关闭模态框
                    }
                    let left = ($(window).width() * (1 - 0.35)) / 2;
                    let top = ($(window).height() * (1 - 0.5)) / 2;
                    $(".image-box").show().animate({
                        width: "-$(window).width()*0.35",
                        height: "-$(window).height()*0.5",
                        left: "-" + left + "px",
                        top: "-" + top + "px"
                    }, 1000, function() {
                        let width1 = $(window).width() * 0.35;
                        let height1 = $(window).height() * 0.5;
                        console.log(width1);
                        $(this).css({ width: width1, height: height1 }).hide();
                    });
                } else {
                    alert(data.message);
                }
            }
        });
    }
}
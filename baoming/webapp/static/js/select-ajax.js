//一些常用的js Ajax 请求信息集合地
//---------------------------------
function getEducationDegree(type, obj) {
    /**
     * type  0 表示添加  1 表示修改
     * 异步获取教育程度，根据数据库记录生成下拉菜单
     * @type {string}
     */
    let url = '/report/education_degree/';
    $.ajax({
        url: url,
        type: 'GET',
        tradition: true,
        data: {},
        success: function(data) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            // var strs = JSON.stringify(arg);
            console.log(data);
            if (data.status) {
                let data_list = JSON.parse(data.data);

                if (type === 0) {
                    $(".education-degree").empty("").append("<option value='0'>---请选择---</option>");
                    $.each(data_list, function(i, n) {
                        $('.education-degree').append('<option value=' + n.id + '>' + n.education_name + '</option>');
                    });
                } else {
                    $("#education_degree_update").empty("").append("<option value='0'>---请选择---</option>");
                    $.each(data_list, function(i, n) {
                        if (n.id === obj) {
                            $('#education_degree_update').append('<option value=' + n.id + ' selected>' + n.education_name + '</option>');
                        } else {
                            $('#education_degree_update').append('<option value=' + n.id + '>' + n.education_name + '</option>');
                        }
                    });
                }
            } else {
                console.log();
            }
        }
    });
}

function getUnitNature(type, obj) {
    /**
     * type  0 表示添加  1 表示修改
     * 异步获取教育程度，根据数据库记录生成下拉菜单
     * @type {string}
     */
    let url = '/report/unit_nature/';
    $.ajax({
        url: url,
        type: 'GET',
        tradition: true,
        data: {},
        success: function(data) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            // var strs = JSON.stringify(arg);
            console.log(data);
            if (data.status) {
                let data_list = JSON.parse(data.data);
                $(".unit-nature").empty("").append("<option>---请选择---</option>");
                if (type === 0) {
                    $.each(data_list, function(i, n) {
                        $('.unit-nature').append('<option value=' + n.id + '>' + n.unit_nature + '</option>');
                    });
                } else {
                    let unit_nature_update = $('#unit_nature_update');
                    unit_nature_update.empty("").append("<option>---请选择---</option>");
                    $.each(data_list, function(i, n) {
                        if (n.id === obj) {
                            unit_nature_update.append('<option value=' + n.id + ' selected>' + n.unit_nature + '</option>');
                        } else {
                            unit_nature_update.append('<option value=' + n.id + '>' + n.unit_nature + '</option>');
                        }
                    });
                }

            } else {
                console.log();
            }
        }
    });
}

function getNationInfo(type, obj) {
    /**
     * type  0 表示添加  1 表示修改
     * 异步获取教育程度，根据数据库记录生成下拉菜单
     * @type {string}
     */
    let url = '/report/nation_info/';
    $.ajax({
        url: url,
        type: 'GET',
        tradition: true,
        data: {},
        success: function(data) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            // var strs = JSON.stringify(arg);
            console.log(data);
            if (data.status) {
                let data_list = JSON.parse(data.data);
                $(".nation-info").empty("").append("<option>---请选择---</option>");
                if (type === 0) {
                    $.each(data_list, function(i, n) {
                        $('.nation-info').append('<option value=' + n.id + '>' + n.nation_name + '</option>');
                    });
                } else {
                    $.each(data_list, function(i, n) {
                        if (n.id === obj) {
                            $('.nation-info').append('<option value=' + n.id + ' selected>' + n.nation_name + '</option>');
                        } else {
                            $('.nation-info').append('<option value=' + n.id + '>' + n.nation_name + '</option>');
                        }
                    });
                }

            } else {
                console.log();
            }
        }
    });
}


// function getTeacherInfo(type, obj) {
//     /**
//      * type  0 表示添加  1 表示修改
//      * 异步获取教师的信息，根据数据库记录生成下拉菜单
//      * @type {string}
//      */
//     let url = '/report/teacher_info/';
//     $.ajax({
//         url: url,
//         type: 'GET',
//         tradition: true,
//         data: {},
//         success: function (data) {
//             /*var callback_dic = $.parseJSON(arg);*/
//             /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
//             // var strs = JSON.stringify(arg);
//             if (data.status) {
//                 let data_list = JSON.parse(data.data);
//                 $(".teacher-info").empty("").append("<option>---请选择---</option>");
//                 if (type === 0) {
//                     $.each(data_list, function (i, n) {
//                         $('.teacher-info').append('<option value=' + n.id + '>' + n.teacher_name + '</option>');
//                     });
//                 } else {
//                     $.each(data_list, function (i, n) {
//                         if (n.id === obj) {
//                             $('.nation-info').append('<option value=' + n.id + ' selected>' + n.teacher_name + '</option>');
//                         } else {
//                             $('.nation-info').append('<option value=' + n.id + '>' + n.teacher_name + '</option>');
//                         }
//                     });
//                 }
//
//             } else {
//                 console.log();
//             }
//         }
//     });
// }
//


function province(type, obj) {
    /**
     * 异步获取教育程度，根据数据库记录生成下拉菜单
     * @type {string}
     */
    let url = '/report/province/';

    if  (typeof(obj)  === 'number' && isNaN(obj))  {
        console.log("Number NaN")
    } else {
        $.ajax({
            url: url,
            type: 'GET',
            tradition: true,
            data: {},
            success: function(data) {
                /*var callback_dic = $.parseJSON(arg);*/
                /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
                // var strs = JSON.stringify(arg);
                console.log(data);
                if (data.status) {
                    let data_list = JSON.parse(data.data);
                    if (type === 0) {
                        $(".province").empty("").append("<option>---省---</option>");
                        $(".city").empty("").append("<option>---市---</option>");
                        $(".county").empty("").append("<option value='-1'>---县---</option>");
                        $.each(data_list, function(i, n) {
                            $('.province').append('<option value=' + n.id + '>' + n.region_name + '</option>');
                        });
                    } else {
                        $(".province_update").empty("").append("<option>---省---</option>");
                        $(".city_update").empty("").append("<option>---市---</option>");
                        $(".county_update").empty("").append("<option value='-1'>---县---</option>");
                        let province_id = 0;
                        $.each(data_list, function(i, n) {
                            if (n.id === obj) {
                                province_id = n.id;
                                $('#hukou_province_update').append('<option value=' + n.id + ' selected>' + n.region_name + '</option>');
                            } else {
                                $('#hukou_province_update').append('<option value=' + n.id + '>' + n.region_name + '</option>');
                            }
                        });
                        let city_id = parseInt($("#update_hukou_city").val());
                        city(province_id, 1, city_id);
                    }

                } else {
                    console.log();
                }
            }
        });
    }
}


function city(obj, type, current_value) {
    /**
     * 异步获取教育程度，根据数据库记录生成下拉菜单
     * @type {string}
     */
    // IE浏览器不支持
    // if (Number.isNaN(obj)) {
    //     console.log("Number NaN';")
    // }
    if  (typeof(obj)  === 'number' && isNaN(obj))  {
        console.log("Number NaN")
    } else {
        let url = '/report/city/';
        $.ajax({
            url: url,
            type: 'GET',
            tradition: true,
            data: { province: obj },
            success: function(data) {
                /*var callback_dic = $.parseJSON(arg);*/
                /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
                // var strs = JSON.stringify(arg);
                if (data.status) {
                    let data_list = JSON.parse(data.data);
                    if (type === 0) {
                        $(".city").empty("").append("<option>---市---</option>");
                        $(".county").empty("").append("<option value='-1'>---县---</option>");
                        $.each(data_list, function(i, n) {
                            $('.city').append('<option value=' + n.id + '>' + n.region_name + '</option>');
                        });
                    } else {
                        $(".city_update").empty("").append("<option>---市---</option>");
                        $(".county_update").empty("").append("<option value='-1'>---县---</option>");
                        let city_id = 0;
                        $.each(data_list, function(i, n) {
                            if (n.id === current_value) {
                                city_id = n.id;
                                $('#hukou_city_update').append('<option value=' + n.id + ' selected>' + n.region_name + '</option>');
                            } else {
                                $('#hukou_city_update').append('<option value=' + n.id + '>' + n.region_name + '</option>');
                            }
                        });
                        let county_id = parseInt($("#update_hukou_county").val());
                        county(city_id, 1, county_id);
                    }

                } else {
                    console.log();
                }
            }
        });
    }
}

function county(obj, type, current_value) {
    /**
     * 异步获取教育程度，根据数据库记录生成下拉菜单
     * @type {string}
     */
    if  (typeof(obj)  === 'number' && isNaN(obj))  {
        console.log("Number NaN")
    } else {
        let url = '/report/county/';
        $.ajax({
            url: url,
            type: 'GET',
            tradition: true,
            data: { city: obj },
            success: function(data) {
                /*var callback_dic = $.parseJSON(arg);*/
                /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
                // var strs = JSON.stringify(arg);
                console.log(data);
                if (data.status) {
                    let data_list = JSON.parse(data.data);

                    if (type === 0) {
                        $(".county").empty("").append("<option value='-1'>---县---</option>");
                        $.each(data_list, function(i, n) {
                            $('.county').append('<option value=' + n.id + '>' + n.region_name + '</option>');
                        });
                    } else {
                        $(".county_update").empty("").append("<option value='-1'>---县---</option>");
                        $.each(data_list, function(i, n) {
                            if (n.id === current_value) {
                                $('.county_update').append('<option value=' + n.id + ' selected>' + n.region_name + '</option>');
                            } else {
                                $('.county_update').append('<option value=' + n.id + '>' + n.region_name + '</option>');
                            }
                        });
                    }
                } else {
                    console.log();
                }
            }
        });
    }
}
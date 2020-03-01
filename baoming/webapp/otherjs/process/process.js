/*省*/
var provincialBase = "../../api/OrgProvincialAdministration/";
var provincelist = provincialBase + "list";
/*接入商*/
var ispBase = "../../api/OrgAccessProvider/";
var isplistByProvince = ispBase + "findByShengid";

var batchidBase = "../../api/batchInfo/";
var batchlistByDwid = batchidBase + "list";

var cybatchidBase = "../../api/samplingBatchInfo/";
var cybatchidlist = cybatchidBase + "selectAllByDesc";
/*增加抽样信息*/
var addCybatchInfo = cybatchidBase + "addCybatchInfo";

var processBase = "../../api/process/";
var startSampled = processBase + "startSampled";
var startSampledSingle = processBase + "startSampledSingle";
var deleteSampleds = processBase + "deleteSampleds";
var checkSampled = processBase + "checkSampled";
var balanceSampledadd = processBase + "balanceSampledadd";
var balanceSampleddel = processBase + "balanceSampleddel";
var checkSampleResult = processBase + "checkSampleResult";
var checkSampledStatus = processBase + "checkSampledStatus";
var saveSampledData = processBase + "saveSampledData";

var selectAllBatchInfo = batchidBase + "selectAllBatchInfo";
var findByBatchid = batchidBase + "findByBatchid";

var getZtidCountOfISPBYbatcid = batchidBase + "getZtidCountOfISPBYbatcid";
var updateUrl = batchidBase + "updateCybatchInfoUrl";

var provinceBase = "../../api/provincial/";
var selectProvinceInfo = provinceBase + "selectProvinceInfo";

var manage_theme = '抽样批次';
$('#manage_title').text(manage_theme + '管理');

/**
 * 选择抽样的范围
 * @param obj
 * @returns
 */
function selectSampleType(obj) {
    /*得到省列表*/
    var orgType = parseInt(obj);
    if (obj > 0) {
        $("#province").empty("");
        $("#province").append("<option selected='selected'>请选择省份</option>");
        $.ajax({
            url: provincelist,
            type: 'GET',
            tradition: true,
            data: {},
            success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
                var strs = JSON.stringify(arg)
                var obj_data = JSON.parse(arg);
                if (obj_data instanceof Array) {
                    $.each(obj_data, function (i, n) {
                        $("#province").append("<option value=" + n.shengid + ">" + n.mc + "</option>");
                    });
//			                         $("#select_item").attr("onfocus","javascript:void(0)");
                } else {
                    alert(); //把错误的信息从后台提出展示出来
                }
            }
        });

        if (obj == 2) {
            $("#li_isp").removeAttr("hidden");
        } else if (obj == 1) {
            $("#li_isp").attr("hidden", "hidden");
        }
    } else {
        $("#li_isp").removeAttr("hidden");
    }
}

/**
 * 选择省份单位
 * @param shengid
 * @returns
 */
function selectProvinceType(shengid) {
    if (shengid > 0) {
        $("#isp").empty("");
        $("#isp").append("<option selected='selected'>请选择接入商</option>");
        $.ajax({
            url: isplistByProvince,
            type: 'GET',
            tradition: true,
            data: {shengid: shengid},
            success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
                var strs = JSON.stringify(arg)
                var obj_data = JSON.parse(arg);
                if (obj_data instanceof Array) {
                    $.each(obj_data, function (i, n) {
                        $("#isp").append("<option value=" + n.id + ">" + n.dwmc + "</option>");
                    });
//			                         $("#select_item").attr("onfocus","javascript:void(0)");
                } else {
                    alert(); //把错误的信息从后台提出展示出来
                }
            }
        });
    } else {
        alert("未选择任何省份!");
    }
}

/**
 * 选择接入商
 * @param dwid
 * @returns
 */
function selectIspType(dwid) {
    if (dwid > 0) {
        $("#dataBatch").empty("");
        $("#dataBatch").append("<option selected='selected'>请选择数据批次</option>");
        $.ajax({
            url: batchlistByDwid,
            type: 'GET',
            tradition: true,
            data: {dwid: dwid},
            success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
                var strs = JSON.stringify(arg)
                var obj_data = JSON.parse(arg);
                if (obj_data instanceof Array) {
                    $.each(obj_data, function (i, n) {
                        $("#dataBatch").append("<option value=" + n.batchid + ">" + n.remark + "</option>");
                    });
//			                         $("#select_item").attr("onfocus","javascript:void(0)");
                } else {
                    alert(); //把错误的信息从后台提出展示出来
                }
            }
        });
    } else {
        alert("未选择任何接入商!");
    }
}

/**
 * 选择批次列表
 * @param dwid
 * @returns
 */
function selectAllBatch() {
    $("#dataBatch").empty("");
//		$("#dataBatch").append("<option selected='selected'>请选择数据批次</option>");
    $.ajax({
        url: selectAllBatchInfo,
        type: 'GET',
        tradition: true,
        data: {},
        success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
            var strs = JSON.stringify(arg)
            var obj_data = JSON.parse(arg);
            console.log("obj_data::::" + obj_data);
            if (obj_data instanceof Array) {
                $.each(obj_data, function (i, n) {
                    $("#dataBatch").append("<option value=" + n.batchid + ">" + n.name + "</option>");
                });
//			                         $("#select_item").attr("onfocus","javascript:void(0)");
            } else {
                alert(); //把错误的信息从后台提出展示出来
            }
        }
    });
}

var cybatchs = new Array();

function selectCybatchid() {
    $("#cybatchid").empty("");
//	$("#cybatchid").append("<option selected='selected'>请选择抽样批次</option>");
    $.ajax({
        url: cybatchidlist,
        type: 'GET',
        tradition: true,
        data: {},
        success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
            var strs = JSON.stringify(arg)
            var obj_data = JSON.parse(arg);
            if (obj_data instanceof Array) {
                cybatchs = obj_data;
                var len = obj_data.length;
                $.each(obj_data, function (i, n) {
                    if (i == 0) {
                        selectbatchInfoType(n.cybatchid);
                    }
                    $("#cybatchid").append("<option value=" + n.cybatchid + ">" + n.name + "</option>");
                });
//		                         $("#select_item").attr("onfocus","javascript:void(0)");
            } else {
                alert(); //把错误的信息从后台提出展示出来
            }
        }
    });
}

/**
 * 暂时不用
 * @param batchid
 * @returns
 */
function selectOrgInfoByBatchid(batchid) {
    $.ajax({
        url: dwByBatchid,
        type: 'GET',
        tradition: true,
        data: {batchid: batchid},
        success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
            var strs = JSON.stringify(arg)
            var obj_data = JSON.parse(arg);
            if (obj_data instanceof Array) {
                var len = obj_data.length;
                $.each(obj_data, function (i, n) {
                    if (i == 1) {
                        selectbatchInfoType(n.batchid);
                    }
                    $("#cybatchid").append("<option value=" + n.cybatchid + ">" + n.name + "</option>");
                });
//		                         $("#select_item").attr("onfocus","javascript:void(0)");
            } else {
                alert(); //把错误的信息从后台提出展示出来
            }
        }
    });

}

function selectbatchInfoType(cybatchid) {
    $.each(cybatchs, function (i, n) {
        if (cybatchid == n.cybatchid) {
            $.ajax({
                url: findByBatchid,
                type: 'GET',
                tradition: true,
                data: {batchid: n.batchid},
                success: function (arg) {    //如果程序执行成功就会执行这里的函数-->
                    console.log("arg:::::" + arg);
//    	        	var strs = JSON.stringify(arg)
                    var obj_data = JSON.parse(arg);
                    if (obj_data instanceof Object) {
                        $("#batchid").val(n.batchid);
                        $("#batchidName").val(obj_data.name);
                    } else {
                        alert(); //把错误的信息从后台提出展示出来
                    }
                }
            });
        }
    });
}


function ajaxButton_set(submitType) {
    if (submitType == 1) {
        /*var fd = new FormData(document.querySelector("form"));*/
        /*var form = document.getElementById("editForm");*/
        /*var formData = new FormData(form);*/
        /*var form = new FormData($("#editForm"));*/
        /*fd.append("CustomField", "This is some extra data");*/
//        console.info($('#editForm').serialize());
        var data = $('#editForm').serialize();
        $.ajax({
            url: addCybatchInfo,
            type: 'POST',
            tradition: true,
            data: data,
            //processData: false,  // 不处理数据
            //contentType: false   // 不设置内容类型
            success: function (arg) {    //如果程序执行成功就会执行这里的函数
                /*var callback_dic = $.parseJSON(arg);*/
                /*var strs = JSON.stringify(arg)*/
                var obj = JSON.parse(arg)
                console.info(obj)
                if (obj == 1) {
                    alert('成功');
                    window.location.reload();
                } else {
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
    } else if (submitType == 2) {
        /*var fd = new FormData(document.querySelector("form"));*/
        /*var form = new FormData($("#editForm")[0]);*/
        /*fd.append("CustomField", "This is some extra data");*/
        if (confirm("确定修改该记录?")) {
            $.ajax({
                url: updateUrl,
                type: 'POST',
                tradition: true,
                data: $('#editForm').serialize(),
                //processData: false,  // 不处理数据
                //contentType: false   // 不设置内容类型
                success: function (arg) {    //如果程序执行成功就会执行这里的函数
                    /*var callback_dic = $.parseJSON(arg);*/
                    /*var strs = JSON.stringify(arg)*/
                    var obj = JSON.parse(arg)
                    console.info(obj)
                    if (obj == 1) {
                        console.log('-----------------------', obj)
                        /*if(obj.process_id != ''){
                            $('#skip_html').click();
                        }*/
                        window.location.reload();
//                        var set_id = 'set_'+ obj.website_identification_code
//                        $('#'+set_id).text('进行中...')
//                        $('#'+set_id).attr('disabled','disabled')
                    } else {
                        alert('失败');
                        alert(obj); //把错误的信息从后台提出展示出来
                    }
                }
            });
        }
    } else {
        return "xxxxxx"
    }
}

function changeRatio(ratio) {
    var float_ratio = parseFloat(ratio);
    if (float_ratio === 0) {
        console.log(ratio);
        console.log(float_ratio);
    } else if (float_ratio > 100) {
        alert("请输入小于 0.001 至 100 的数字");
        console.log(float_ratio);
    } else if (float_ratio <= 0.000001) {
        alert("请输入小于 0.001 至 100 的数字");
        console.log(float_ratio);
    } else {
        console.log(ratio);
        console.log(float_ratio);
    }
}

var ids = [];
var idsCopy = [];
var sampledArray = [];
// id: ispid,
var sampledStandard = $("#smallestLimit").val();
var sampledStandardCount = parseFloat(sampledStandard);
var tmpCount = 0;

/**
 * 进行批量选择操作
 * @type {Array}
 */
var checkIds = [];
var checkIdsCopy = [];

var selectType = 1;

function createOrder() {
    var values = [];
    var ratio_str = "";
    var index_str = "";               //序号
    var id_str = "";                  //接入商ID
    var dwmc_str = "";                //单位名称
    var count_str = "";               //总数数量
    var float_ratio = 0;              //获得百分数
    var ratio_count = 0;

    var i_str_ratio = "";
    var i_str_ratio_count = "";
    var newid = "";
    var sampled = {};
    var check_val = "";
    var i;
    var index_i = 0;

    for (i = 0; i < checkIds.length; i++) {
        sampled = {index: "", id: "", ratio: "", init_count: "", count: "", dwmc: ""};
        console.log("checkIds[i]:::" + checkIds[i]);
        check_val = $("#" + checkIds[i]).val();
        values = check_val.split("_");
        ratio_str = $("#ratio_str").val();
        ratio_str = ratio_str.replace(/(^\s*)|(\s*$)/g, "");
        index_str = values[0];               //序号
        id_str = values[1];                  //接入商ID
        dwmc_str = values[2];                //单位名称
        count_str = values[3];               //总数数量
        if (ratio_str == "0") {
            float_ratio = 0;
        } else {
            float_ratio = parseFloat(ratio_str); //获得百分数
        }
        float_ratio = float_ratio / 100;         //获得系数
        ratio_count = parseInt((float_ratio * parseFloat(count_str)));
        if (ratio_count <= 1) {
            /*如果主体数量小于50，则全部抽取*/
            ratio_count = parseInt(count_str);
        } else {
            ratio_count = parseInt((float_ratio * parseFloat(count_str))); //获得抽取数量
        }
        // var pNode = $("#"+checkIds[i]).parentNode;
        // nextNode = pNode.nextSibling;
        if (ratio_str == "0") {
            i_str_ratio = "n_ratio_" + index_str;
            $("#" + i_str_ratio).text(0);
            i_str_ratio_count = "c_ratio_" + index_str;
            $("#" + i_str_ratio_count).text(0);
        } else {
            i_str_ratio = "n_ratio_" + index_str;
            $("#" + i_str_ratio).text(float_ratio);
            i_str_ratio_count = "c_ratio_" + index_str;
            $("#" + i_str_ratio_count).text(ratio_count);
        }
        var check_str = index_str + "_" + id_str + "_" + dwmc_str + "_" + count_str;
        $("#" + check_str).attr("onclick", "selectBatchSingleAdd(this.id)");
        index_i = ids.indexOf(id_str);
        if (ratio_str == "0") {
            if (index_i >= 0) {
                sampledArray.splice(index_i, 1);
                ids.splice(index_i, 1);
                sampled.index = index_str;
                sampled.id = id_str;
                sampled.init_count = count_str;
                sampled.ratio = float_ratio.toString();
                sampled.count = "0";
                sampled.dwmc = dwmc_str;
                ids.push(id_str);
            } else {
                sampled.index = index_str;
                sampled.id = id_str;
                sampled.init_count = count_str;
                sampled.ratio = float_ratio.toString();
                sampled.count = "0";
                sampled.dwmc = dwmc_str;
                ids.push(id_str);
            }
            //查看是否在之前抽选过
            sampledArray.push(sampled);
            // coffee[i].checked = false;
            $("#" + checkIds[i]).attr("checked", false);
            var sampledLength = sampledArray.length;
            if (sampledLength > sampledStandardCount) {
                /*如果抽样数量已经超过了设定的标准数量，即要提醒用户进行重新设置，或者通过补抽或减抽的机制使其平衡*/
                alert("当前抽样数量已经超出抽样数量设置的标准，请重新设置比例，或者设置补抽和减抽标准数");
            } else {
            }
        } else {
            if (index_i >= 0) {
                sampledArray.splice(index_i, 1);
                ids.splice(index_i, 1);
                sampled.index = index_str;
                sampled.id = id_str;
                sampled.init_count = count_str;
                sampled.ratio = float_ratio.toString();
                sampled.count = ratio_count.toString();
                sampled.dwmc = dwmc_str;
                ids.push(id_str);
            } else {
                sampled.index = index_str;
                sampled.id = id_str;
                sampled.init_count = count_str;
                sampled.ratio = float_ratio.toString();
                sampled.count = ratio_count.toString();
                sampled.dwmc = dwmc_str;
                ids.push(id_str);
            }
            //查看是否在之前抽选过
            sampledArray.push(sampled);
            // coffee[i].checked = false;
            $("#" + checkIds[i]).attr("checked", false);
            var sampledLength = sampledArray.length;
            if (sampledLength > sampledStandardCount) {
                /*如果抽样数量已经超过了设定的标准数量，即要提醒用户进行重新设置，或者通过补抽或减抽的机制使其平衡*/
                alert("当前抽样数量已经超出抽样数量设置的标准，请重新设置比例，或者设置补抽和减抽标准数");
            } else {
            }
        }

    }

    /*清空已经抽样结束的临时抽样结果*/
    // checkIdsCopy.concat(checkIds);
    // idsCopy.concat(ids);
    // ids.length = 0;
    checkIds.length = 0;
    var tex = 0;
    console.log("sampledArray:::" + JSON.stringify(sampledArray));
    $.each(sampledArray, function (i, n) {
        tex = tex + parseInt(n.count);
    });
    $("#sampledSum").text(tex);
}

function stopOrder() {
    var sampledStandard = $("#smallestLimit").val();
    var sampledStandardCount = parseInt(sampledStandard);
    var sampledLength = sampledArray.length;
    if (sampledLength === sampledStandardCount) {
        console.log();
        /*如果抽样数量已经超过了设定的标准数量，即要提醒用户进行重新设置，或者通过补抽或减抽的机制使其平衡*/
    } else if (sampledLength > sampledStandardCount) {
        alert("当前抽样数量已经 超出 抽样数量设置的标准，请重新设置比例，或者设置补抽和减抽标准数");
    } else {
        alert("当前抽样数量为 0 或者尚未达到 抽样数量设置的标准，请继续抽取或者重新设置比例，或者设置补抽和减抽标准数");
    }
}

function selectBatchSingleAdd(obj) {
    console.log("obj:::" + obj);
    checkIds.push(obj);
    console.log(checkIds);
    $("#" + obj).attr("onclick", "selectBatchSingleDel(this.id)");
}

function selectBatchSingleDel(obj) {
    var index = checkIds.indexOf(obj);
    checkIds.splice(index, 1);
    console.log(checkIds);
    $("#" + obj).attr("onclick", "selectBatchSingleAdd(this.id)");
}

function selectBatch() {
    /*清空上一次存储的内容*/
    checkIds.length = 0;
    var ltid = parseFloat($("#ltid").val());
    var gtid = parseFloat($("#gtid").val());
    var ztcounts = document.getElementsByClassName("ztcount");
    var checkId = "";
    for (var i = 0; i < ztcounts.length; i++) {
        var countStr = ztcounts[i].textContent;
        var countInt = parseFloat(countStr);
        if (countInt >= ltid && countInt < gtid) {
            var nextNode = ztcounts[i].nextSibling;
            nextNode = nextNode.nextSibling;
            var cs = nextNode.childNodes;
            var nodeCs = cs[0];
            nodeCs.setAttribute("checked", "checked");
            checkId = nodeCs.getAttribute("id");
            checkIds.push(checkId);
        }
    }
    selectType = 0;
}


function selectBatchClear() {
    var ltid = parseFloat($("#ltid").val());
    var gtid = parseFloat($("#gtid").val());
    var ztcounts = document.getElementsByClassName("ztcount");
    var num = 0;
    for (var i = 0; i < ztcounts.length; i++) {
        var countStr = ztcounts[i].textContent;
        var countInt = parseFloat(countStr);
        if (countInt >= ltid && countInt < gtid) {
            num = num + 1;
            var nextNode = ztcounts[i].nextSibling;
            nextNode = nextNode.nextSibling;
            var cs = nextNode.childNodes;
            var nodeCs = cs[0];
            var checkboxId = nodeCs.getAttribute("id");
            var vs = checkboxId.split("_");
            var id_str = vs[1];                  //接入商ID
            /*从已生成抽样数据列表中删除*/
            var index_i = ids.indexOf(id_str);
            if (index_i > 0) {
                sampledArray.splice(index_i, 1);
                ids.splice(index_i, 1);
            }
            // nodeCs.removeAttribute("checked");
            // nodeCs.setAttribute("checked","");
            // nodeCs.setAttribute("checked","checked");
            // nodeCs.checked = true; //数据清空没必要固定选择
            nextNode = nextNode.nextSibling;
            cs = nextNode.childNodes;
            nodeCs = cs[0];
            var nid = nodeCs.getAttribute("id");
            console.log("nid:::" + nid);
            $("#" + nid).text("");
            nextNode = nextNode.nextSibling;
            cs = nextNode.childNodes;
            nodeCs = cs[0];
            var nid2 = nodeCs.getAttribute("id");
            console.log("nid2:::" + nid2);
            $("#" + nid2).text("");
        }
    }
}

/**
 * 随机数时间抽样
 * sum(1,100)；
 * @param m
 * @param n
 */
function ramdom(m, n) {
    return Math.floor(Math.random() * (m - n) + n);
}

/**
 * 抽取的主要方法
 * @param i
 * @param len
 * @param n
 */
function parse(i, len, n, pint) {
    var cybatchid = $("#cybatchid").val();
    var batchid = $("#batchid").val();
    var i_str_ratio_real_progress = "";
    var i_str_ratio_real_progress_int = "";
    var i_str_ratio_real_zhuan = "";
    var ramdomNum = 0;
    var progress = "";
    var processAll = 0;
    i_str_ratio_real_progress = "c_real_progress_" + n.index2;
    i_str_ratio_real_progress_int = "c_real_progress_int_" + n.index2;
    i_str_ratio_real_zhuan = "c_real_progress_zhuan_" + n.index2;
    ramdomNum = ramdom(1, 100);
    ramdomNum = ramdomNum - 20;
    if (ramdomNum < 0) {
        ramdomNum = ramdomNum * -1;
    }
    progress = ramdomNum.toString();
    $("#" + i_str_ratio_real_zhuan).attr("src", "./zhuan.gif");
    $("#" + i_str_ratio_real_progress).css("width", progress + "px");
    $("#" + i_str_ratio_real_progress_int).text(progress + "%");
    var jsonStr = JSON.stringify(n);

    // increase(i_str_ratio_real_progress,i_str_ratio_real_progress_int,ramdomNum);
    $.ajax({
        url: startSampledSingle,
        type: 'POST',
        tradition: true,
        // async:false,
        data: {cybatchid: cybatchid, batchid: batchid, jsonStr: jsonStr},
        success: function (arg) {
            if (arg == 1) {
                $("#" + i_str_ratio_real_progress).css("width", "100px");
                $("#" + i_str_ratio_real_progress_int).text("100%");
                $("#" + i_str_ratio_real_zhuan).attr("src", "");
                processAll = processAll + 1;
                if (pint === 1) {
                    $("#processAll").css("width", "100px");
                    $("#processAllInt").text("100%");
                    $("#zhuan").attr("src", "");
                } else {
                    var widthpx = $("#processAll").css("width");
                    if (widthpx === "100px") {
                        console.log("");
                    } else {
                        // sleep(1500);
                        widthpx = widthpx.replace("px", "");
                        var curret = parseInt(widthpx) + 1;
                        if (curret > 100) {
                            curret = curret - 40;
                        } else if (curret < 20) {
                            curret = curret + 30;
                        } else {
                            console.log();
                        }
                        $("#processAll").css("width", curret.toString() + "px");
                        // $("#processAllInt").text(curret.toString() + "%");
                        $("#processAllInt").text("抽取中...");
                    }
                }
                return 1;
            }
        }
    });
}

function sleep(delay) {
    var start = (new Date()).getTime();
    while ((new Date()).getTime() - start < delay) {
        continue;
    }
}

/**
 * 开始抽样
 */
function start_sample() {
    /*检测数量*/
    // stopOrder();
    var jsonStr = "";
    var cybatchid = $("#cybatchid").val();
    var batchid = $("#batchid").val();
    var widthpx = $("#processAll").css("width");
    $.ajax({
        url: checkSampled,
        type: 'GET',
        tradition: true,
        data: {cybatchid: cybatchid},
        success: function (arg) {
            if (arg == 1) {
                var confirmRes = confirm("当前抽样批次已经有数据，是否删除重新抽样？")
                if (confirmRes) {
                    $.ajax({
                        url: deleteSampleds,
                        type: 'POST',
                        tradition: true,
                        data: {cybatchid: cybatchid},
                        success: function (arg) {
                            /* == 转义成同一个类型之后在比较*/
                            if (arg == 1) {
                                var len = parseFloat(sampledArray.length);
                                var sleepx = 0;
                                for (let i = 0; i < sampledArray.length; i++) {
                                    $("#zhuan").attr("src", "./zhuan.gif");
                                    var ram = ramdom(3, 10) * 2 * i;
                                    var curret = parseInt(widthpx) + ram;
                                    if (curret > 100) {
                                        curret = curret - 50;
                                    } else if (curret < 20) {
                                        curret = curret + 30;
                                    } else {
                                        console.log();
                                    }
                                    $("#processAll").css("width", curret.toString() + "px");
                                    $("#processAllInt").text(curret.toString() + "%");
                                    sleepx = sleep + 500;
                                    sleep(sleepx);
                                    if (i === sampledArray.length - 1) {
                                        parse(i, len, sampledArray[i], 1);
                                    } else {
                                        parse(i, len, sampledArray[i], 0);
                                        $("#processAll").css("width", "100px");
                                        $("#processAllInt").text("100%");
                                        $("#zhuan").attr("src", "");
                                    }
                                }
                            } else {
                                console.log("");
                            }
                        }
                    });

                }
            } else if (arg == 0) {
                /*如果不存在此抽样数据批次，则直接进行相关的抽样操作*/
                var len = parseFloat(sampledArray.length);
                var sleepx = 0;
                for (let i = 0; i < sampledArray.length; i++) {
                    $("#zhuan").attr("src", "./zhuan.gif");
                    var ram = ramdom(3, 10) * 2 * i;
                    var curret = parseInt(widthpx) + ram;
                    if (curret > 100) {
                        curret = curret - 10;
                    }
                    // $("#processAll").css("width", curret.toString() + "px");
                    $("#processAllInt").text("抽取中...");
                    sleepx = sleep + 500;
                    sleep(sleepx);
                    if (i === sampledArray.length - 1) {
                        parse(i, len, sampledArray[i], 1);
                    } else {
                        parse(i, len, sampledArray[i], 0);
                        $("#processAll").css("width", "100px");
                        $("#processAllInt").text("100%");
                        $("#zhuan").attr("src", "");
                    }
                }
            }
        }
    });
}

function loading(percent) {
    $('.progress span').animate({width: percent}, 1000, function () {
        $(this).children().html(percent);
        if (percent === '100%') {
            $(this).children().html('抽样数量匹配完成...&nbsp;&nbsp;&nbsp;&nbsp;');
            // setTimeout(function(){
            //     $('.container').fadeOut();
            //     location.href="http://sc.chinaz.com/";
            // },1000);
        }
    })
}

var tmpArray = [];
var tmpArraySearch = [];

function dwlbSwitch(dwlbCheckArray, ndwlb, tr_index){
    for (let j = 0; j < dwlbCheckArray.length; j++) {
        if((ndwlb == dwlbCheckArray[j])){
            console.log((ndwlb == dwlbCheckArray[j]));
            $("#" + tr_index).show();
        }else{
            $("#" + tr_index).hide();
        }
    }
}
function searchZtInfo() {
    tmpArraySearch.length = 0;
    var shengid = $("#selectProvince").val();
    var keyword = $("#keyword").val();

    var dwlbChecks =document.getElementsByName("dwlb");
    var dwlbCheckArray = [];
    dwlbCheckArray.length = 0;
    for (let i = 0; i < dwlbChecks.length; i++) {
       let ischecked = dwlbChecks[i].checked;
       if(ischecked){
           let dwlbval = dwlbChecks[i].value;
           console.log(typeof dwlbval);
           dwlbCheckArray.push(dwlbval.toString());
       }else{
           console.log("未选择");
       }
    }
    var len = dwlbCheckArray.length;
    if(len > 0) {
        $.each(tmpArray, function (i, n) {
            var dwmc = n.DWMC;
            var nshengid = n.SHENGID.toString();
            var ndwlb = n.DWLB;
            var shengidBool = isEmpty(shengid);
            var tr_index = "tr_" + i.toString();
            if (shengidBool) {
                if (shengid === "-10000000" || shengid === "null") {
                    if (keyword) {
                        if (dwmc.indexOf(keyword) > -1) {
                            console.log("匹配到相关信息01-", dwmc + "-", keyword);
                            // tmpArraySearch.push(n);
                            dwlbSwitch(dwlbCheckArray, ndwlb, tr_index)
                        } else {
                            $("#" + tr_index).hide();
                            console.log("未匹配到相关信息02");
                        }
                    } else {
                        console.log("匹配到相关信息01-", dwmc + "-", keyword);
                        // tmpArraySearch.push(n);
                        // $("#" + tr_index).show();
                        dwlbSwitch(dwlbCheckArray, ndwlb, tr_index)
                        // tmpArraySearch.push(n);
                    }
                } else if (nshengid === shengid) {
                    console.log(nshengid + "000" + shengid + "666666666666666666666666666666666666666666666666666");
                    /*得到此省份的信息*/
                    if (keyword) {
                        if (dwmc.indexOf(keyword) > -1) {
                            console.log("匹配到相关信息01-", +nshengid + "000" + dwmc + "-", keyword);
                            // tmpArraySearch.push(n);
                            dwlbSwitch(dwlbCheckArray, ndwlb, tr_index)
                        } else {
                            $("#" + tr_index).hide();
                            console.log("未匹配到相关信息02");
                        }
                    } else {
                        console.log("匹配到相关信息01-", dwmc + "-", keyword);
                        // tmpArraySearch.push(n);
                        dwlbSwitch(dwlbCheckArray, ndwlb, tr_index)
                        // tmpArraySearch.push(n);
                    }
                } else {
                    $("#" + tr_index).hide();
                    console.log("未匹配到相关信息04");
                }
            } else {
                if (keyword) {
                    if (dwmc.indexOf(keyword) > -1) {
                        console.log("匹配到相关信息01-", dwmc + "-", keyword);
                        // tmpArraySearch.push(n);
                        dwlbSwitch(dwlbCheckArray, ndwlb, tr_index)
                    } else {
                        $("#" + tr_index).hide();
                        console.log("未匹配到相关信息02");
                    }
                } else {
                    console.log("匹配到相关信息01-", dwmc + "-", keyword);
                    // tmpArraySearch.push(n);
                    dwlbSwitch(dwlbCheckArray, ndwlb, tr_index)
                    // tmpArraySearch.push(n);
                }
            }
        });
    }else{
        $.each(tmpArray, function (i, n) {
            var dwmc = n.DWMC;
            var nshengid = n.SHENGID.toString();
            var ndwlb = n.DWLB;
            var shengidBool = isEmpty(shengid);
            var tr_index = "tr_" + i.toString();
            if (shengidBool) {
                if (shengid === "-10000000" || shengid === "null") {
                    if (keyword) {
                        if (dwmc.indexOf(keyword) > -1) {
                            console.log("匹配到相关信息01-", dwmc + "-", keyword);
                            // tmpArraySearch.push(n);
                            $("#" + tr_index).show();
                        } else {
                            $("#" + tr_index).hide();
                            console.log("未匹配到相关信息02");
                        }
                    } else {
                        console.log("匹配到相关信息01-", dwmc + "-", keyword);
                        // tmpArraySearch.push(n);
                        $("#" + tr_index).show();
                        // tmpArraySearch.push(n);
                    }
                } else if (nshengid === shengid) {
                    console.log(nshengid + "000" + shengid + "666666666666666666666666666666666666666666666666666");
                    /*得到此省份的信息*/
                    if (keyword) {
                        if (dwmc.indexOf(keyword) > -1) {
                            console.log("匹配到相关信息01-", +nshengid + "000" + dwmc + "-", keyword);
                            // tmpArraySearch.push(n);
                            $("#" + tr_index).show();
                        } else {
                            $("#" + tr_index).hide();
                            console.log("未匹配到相关信息02");
                        }
                    } else {
                        console.log("匹配到相关信息01-", dwmc + "-", keyword);
                        // tmpArraySearch.push(n);
                        $("#" + tr_index).show();
                        // tmpArraySearch.push(n);
                    }
                } else {
                    $("#" + tr_index).hide();
                    console.log("未匹配到相关信息04");
                }
            } else {
                if (keyword) {
                    if (dwmc.indexOf(keyword) > -1) {
                        console.log("匹配到相关信息01-", dwmc + "-", keyword);
                        // tmpArraySearch.push(n);
                        $("#" + tr_index).show();
                    } else {
                        $("#" + tr_index).hide();
                        console.log("未匹配到相关信息02");
                    }
                } else {
                    console.log("匹配到相关信息01-", dwmc + "-", keyword);
                    // tmpArraySearch.push(n);
                    $("#" + tr_index).show();
                    // tmpArraySearch.push(n);
                }
            }
        });
    }
    console.log("tmpArraySearch::" + tmpArraySearch.length);

    $("#selectProvince").val(shengid);
    $("#keyword").val(keyword);
}

//判断字符是否为空的方法
function isEmpty(obj) {
    if (typeof obj == "undefined" || obj == null || obj === "") {
        return false;
    } else {
        return true;
    }
}

//判断字符是否为空的方法
function isEmpty2(obj) {
    if (typeof obj == "undefined" || obj == null || obj === "") {
        return 0;
    } else {
        return obj;
    }
}

/**
 * 补抽增加
 */
function balanceSampledAdds() {
    var smallestLimit = $("#smallestLimit").val();
    var supplement = $("#supplement").val();
    var sampledSum = $("#sampledSum").text();
    var jsonStr = JSON.stringify(sampledArray);
    $.ajax({
        url: balanceSampledadd,
        type: 'GET',
        tradition: true,
        data: {smallestLimit: smallestLimit, supplement: supplement, sampledSum: sampledSum, jsonStr: jsonStr},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            var strs = JSON.stringify(arg);
            console.log("strs:::" + strs);
            var obj_data = JSON.parse(arg);
            console.log("obj_data:::" + obj_data);
            var texxx = 0;
            sampledArray = obj_data;
            $.each(sampledArray, function (i, n) {
                var new_ratio = parseFloat(n.count) / parseFloat(n.init_count);
                new_ratio = new_ratio.toFixed(4);
                var i_str_ratio = "n_ratio_" + n.index2;
                var ratio_text = $("#" + i_str_ratio).text();
                if (parseFloat(ratio_text).toFixed(4) === new_ratio) {
                    console.log();
                } else {
                    // ratio_text = ratio_text + "->" + new_ratio.toString();
                    $("#" + i_str_ratio).text(new_ratio.toString());
                }
                var i_str_ratio_count = "c_ratio_" + n.index2;
                $("#" + i_str_ratio_count).text(n.count);
                texxx = texxx + parseInt(n.count);
                var check_str = n.index2 + "_" + n.id + "_" + n.dwmc + "_" + n.count.toString();
                $("#" + check_str).attr("onclick", "selectBatchSingleAdd(this.id)");
            });
            $("#sampledSum").text(texxx);
            $("#zhuanSum").attr("src", "zhuan.gif");
            $("#zhuanadd").attr("src", "zhuan.gif");
            $("#zhuandel").attr("src", "");
        }
    });
}

function balanceSampleddels() {
    var smallestLimit = $("#smallestLimit").val();
    var supplement = $("#supplement").val();
    var sampledSum = $("#sampledSum").text();
    var jsonStr = JSON.stringify(sampledArray);
    $.ajax({
        url: balanceSampleddel,
        type: 'GET',
        tradition: true,
        data: {smallestLimit: smallestLimit, supplement: supplement, sampledSum: sampledSum, jsonStr: jsonStr},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            var strs = JSON.stringify(arg);
            console.log("strs:::" + strs);
            var obj_data = JSON.parse(arg);
            console.log("obj_data:::" + obj_data);
            var texxx = 0;
            sampledArray = obj_data;
            $.each(sampledArray, function (i, n) {
                var new_ratio = parseFloat(n.count) / parseFloat(n.init_count);
                new_ratio = new_ratio.toFixed(4);
                var i_str_ratio = "n_ratio_" + n.index2;
                var ratio_text = $("#" + i_str_ratio).text();
                if (parseFloat(ratio_text).toFixed(4) === new_ratio) {
                    console.log();
                } else {
                    // ratio_text = ratio_text + "->" + new_ratio.toString();
                    $("#" + i_str_ratio).text(new_ratio.toString());
                }
                var i_str_ratio_count = "c_ratio_" + n.index2;
                $("#" + i_str_ratio_count).text(n.count);
                texxx = texxx + parseInt(n.count);
                var check_str = n.index2 + "_" + n.id + "_" + n.dwmc + "_" + n.count.toString();
                $("#" + check_str).attr("onclick", "selectBatchSingleAdd(this.id)");
            });
            $("#sampledSum").text(texxx);
            $("#zhuanSum").attr("src", "zhuan.gif");
            $("#zhuanadd").attr("src", "");
            $("#zhuandel").attr("src", "zhuan.gif");
        }
    });
}

/**
 * 检查抽样的结果
 */

var cybatchid = $("#cybatchid").val();
var batchid = $("#batchid").val();
function check_sample() {
	var cybatchid = $("#cybatchid").val();
	var batchid = $("#batchid").val();
    $.ajax({
        url: checkSampleResult,
        type: 'GET',
        tradition: true,
        data: {batchid: batchid, cybatchid: cybatchid},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            // var strs = JSON.stringify(arg);
            var obj_data = JSON.parse(arg);
            console.log("obj_data::" + obj_data);
            var actualSampled = 0; //实际抽取数量反馈
            var actualRatio = 0; //实际抽取比例
            $.each(obj_data, function (i, n) {
                $.each(sampledArray, function (i, m) {
                    if (n.ID == m.id) {
                        if (isEmpty2(m.count) == 0) {
                            console.log(m.count);
                        } else {
                            var i_str_ratio = "n_real_ratio_" + m.index2;
                            var real_ratio = parseFloat(n.KCOUNT) / parseFloat(n.COUNT);
                            $("#" + i_str_ratio).text(real_ratio.toFixed(4));
                            var i_str_ratio_count = "c_real_ratio_" + m.index2;
                            $("#" + i_str_ratio_count).text(n.KCOUNT);
                            actualSampled = actualSampled + n.KCOUNT;
                        }
                    }
                });
            });
            $("#actualSampledCount").text(actualSampled);
        }
    });
}

function saveSampledDatas(){
	var cybatchid = $("#cybatchid").val();
    if(confirm("确定保存本次抽样记录?")){
        $.ajax({
            url: saveSampledData,
            type: 'GET',
            tradition: true,
            data: {cybatchid: cybatchid},
            success: function (arg) {
                /*var callback_dic = $.parseJSON(arg);*/
                /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
                var strs = JSON.stringify(arg)
                // var obj_data = JSON.parse(arg);
                    if (arg == 1) {
                        alert("保存成功！！");
                    }else{
                        alert("保存失败！！");
                    }
                }
            });
    }
}

function to_detail_func(obj_data) {

    $('#contents_div').html("");
    var div_controller = "<div style=''><table><title>配置抽取百分比</title><tbody>" +
        // "<tr style='width: 700px'>" +
        //     "<td width='300px' style='text-align: right'>前置条件:</td>"+
        // "</tr>" +
        "<tr style='width: 700px'>" +
        "<td width='300px' style='text-align: right'>前置条件:</td>" +
        "<td>" +
        "&nbsp;&nbsp;<select-div.css id='selectProvince' class='ipt' style='width:145px'>" +
        "</select-div.css>" +
        "&nbsp;&nbsp;<input style='-webkit-appearance: checkbox' type='checkbox'>主体省份&nbsp;&nbsp;" +
        "<input type='text' value='' id='keyword' class='ipt' title='关键词' placeholder='关键词'>&nbsp;&nbsp;" +
        "&nbsp;&nbsp;<input type='button'  class='btop' value='查询' id='' onclick='searchZtInfo()'>" +
        "</td>" +
        // "<th><input id='smallestLimit' class='ipt' style='width:140px' placeholder='抽样标准总数量' title='请填写抽样标准总数量'/></th>" +
        "<td>&nbsp;&nbsp;<input id='smallestLimit' class='ipt' style='width:145px' placeholder='抽样标准总数量' title='请填写抽样标准总数量'/>" +
        "&nbsp;&nbsp;<input id='supplement' class='ipt' style='width:145px' placeholder='补抽或减抽主体数量临界' title='如抽样完毕后总量未达到抽样标准总数量，" +
        "在接入网站数量为主体临界值以上的范围中继续补抽，直到达到抽样标准总数量条。如超过抽样总数量下限，在接入网站数量为主体临界值以上的范围中减去，直到达到抽样标准总数量'/>" +
        "&nbsp;<a href='javascript:void(0)' onclick='balanceSampledAdds();'>" +
        "&nbsp;&nbsp;<button class='btop' title='开始按照补减主体数量标准进行抽样数量平衡'>平衡抽样数量(补抽)</button><img style='height:10px' id='zhuanadd' src='' alt=''/></a>&nbsp;" +
        "&nbsp;<a href='javascript:void(0)' onclick='balanceSampleddels();'>" +
        "&nbsp;&nbsp;<button class='btop' title='开始按照补减主体数量标准进行抽样数量平衡'>平衡抽样数量(减抽)</button><img style='height:10px' id='zhuandel' src='' alt=''/></a>&nbsp;" +
        "</td>" +
        "</tr>" +
        "<tr style='width: 700px'>" +
        "<td width='300px' height='30px' style='text-align: right'></td>" +
        "<td>" +
        "&nbsp;&nbsp;&nbsp;&nbsp;<input type='checkbox' style='-webkit-appearance: checkbox' name='dwlb' value='0'>APPNIC" +
        "&nbsp;&nbsp;<input type='checkbox' style='-webkit-appearance: checkbox' name='dwlb' value='1'>CNNIC" +
        "&nbsp;&nbsp;<input type='checkbox' style='-webkit-appearance: checkbox' name='dwlb' value='2'>公益性单位" +
        "&nbsp;&nbsp;<input type='checkbox' style='-webkit-appearance: checkbox' name='dwlb' value='3'>运行商总部" +
        "&nbsp;&nbsp;<input type='checkbox' style='-webkit-appearance: checkbox' name='dwlb' value='4'>运行商省级分公司" +
        "&nbsp;&nbsp;<input type='checkbox' style='-webkit-appearance: checkbox' name='dwlb' value='5'>报备单位" +
        "&nbsp;&nbsp;<input type='checkbox' style='-webkit-appearance: checkbox' name='dwlb' value='6'>从CNNIC申请IP的单位" +
        "&nbsp;&nbsp;<input type='checkbox' style='-webkit-appearance: checkbox' name='dwlb' value='7'>从APNIC直接申请IP的单位"+
        "</tr>"+
        "<tr style='width: 700px'>" +
        "<td width='300px' style='text-align: right'>参数设置:</td>" +
        // "<th><input id='ltid' class='ipt' style='width:85px' placeholder='主体数量(小)'/>~<input id='gtid' style='width:85px' class='ipt' placeholder='主体数量(大)'/></th>" +
        "<td>&nbsp;&nbsp;<input id='ltid' class='ipt' style='width:145px' placeholder='主体数量(小)'/>~<input id='gtid' style='width:145px' class='ipt' placeholder='主体数量(大)'/>" +
        "&nbsp;&nbsp;<a href='javascript:void(0)' onclick='selectBatch();'><button class='btop' title='开始核查选中抽样批次的数据'>批量选择</button></a>" +
        "&nbsp;&nbsp;<a href='javascript:void(0)' onclick='selectBatchClear();'><button class='btop' title='开始核查选中抽样批次的数据'>清空选择</button></a>" +
        "</td>" +
        // "<th><a href='javascript:void(0)' onclick='selectBatchClear();'><button class='btop' title='开始核查选中抽样批次的数据'>清空选择</button></a></th>"+
        /*"<th>参数配置</th>" +*/
        "<td>&nbsp;&nbsp;<input onchange='changeRatio(this.value);' id='ratio_str' type='text' placeholder='抽样比率' style='width:145px' required class='ipt'>" +
        "<span class='ipt' style='color:red' title='以百分比计算比例'>%</span>" +
        "&nbsp;&nbsp;<a href='javascript:void(0)' onclick='createOrder();'><button class='btop' title='开始核查选中抽样批次的数据'>生成抽样数据</button></a>" +
        "&nbsp;&nbsp;<span id='sampledSum'></span><img style='height:10px' id='zhuanSum' src='' alt=''/>&nbsp;&nbsp;" +
        "&nbsp;&nbsp;<a href='javascript:void(0)' onclick='stopOrder();'><button class='btop' title='开始核查选中抽样批次的数据'>终止抽样</button></a></td>" +
        // "<th><a href='javascript:void(0)' onclick='createOrder();'><button class='btop' title='开始核查选中抽样批次的数据'>生成抽样数据</button></a></th>"+
        // "<th><a href='javascript:void(0)' onclick='stopOrder();'><button class='btop' title='开始核查选中抽样批次的数据'>终止抽样</button></a></th>"+
        "</tr>" +
        "<tr style='width: 700px'>" +
        "<td width='300px' style='text-align: right'></td>" +
        "<td id='progrBar' style='text-align: left'>" +
        "&nbsp;&nbsp;<a href='javascript:void(0)' onclick='start_sample();'><button class='btop' title='开始核查选中抽样批次的数据'>开始抽取</button></a>" +
        "&nbsp;&nbsp;<span class='ipt' title='开始核查选中抽样批次的数据'>抽样进度&nbsp;&nbsp; <img style='height:10px' id='zhuan' src='' alt=''/><img id='processAll' src='./jindu2.gif' style='height:10px;width:0px' alt='进度进度为0%' />" +
        "<a href='javascript:void(0)' id='processAllInt'></a></span>" +
        "&nbsp;&nbsp;<a href='javascript:void(0)' onclick='check_sample();'><button class='btop' title='检查抽样抽样批次的数据'>检查抽样结果</button></a>" +
        "&nbsp;&nbsp;<span id='actualSampledCount'></span>" +
        "&nbsp;&nbsp;<a href='javascript:void(0)' onclick='saveSampledDatas();'><button class='btop' title='保存抽样结果'>保存抽样结果</button></a>" +
        "</td>" +
        "</tr></tbody></table></div>";

    // display:table;
    // width:100%;
    // table-layout:fixed;
    // width: calc( 100% - 1em )
    var table_head = "<table id='tab_opt' class=\"zebra\">" +
        "<thead>" +
        "<tr style='display: table;width: 100%;table-layout: fixed'>" +
        "<th style=\"width:70px\">接入商ID</th>" +
        "<th style=\"width:150px\">接入商名称</th>" +
        "<th style=\"width:50px\">抽样源数</th>" +
        "<th style=\"width:50px\">已抽样数</th>" +
        "<th style=\"width:50px\">选择</th>" +
        "<th style=\"width:50px\">应抽取比率系数</th>" +
        "<th style=\"width:50px\">应抽取数量</th>" +
        "<th style=\"width:50px\">实际抽取比率系数</th>" +
        "<th style=\"width:50px\">实际抽取数量</th>" +
        "<th style=\"width:50px\">抽取进度</th>" +
        "<th style=\"width:0.236%\"></th>" +
        // "<th style=\"width:0.01px\">&nbsp;</th>" +
        // "        <th style=\"width:15%\">已选接入商</th>\n" +
        "        </tr>" +
        "        </thead>" +
        "        <tbody id='infos' style='display: block;height: 100%;overflow-y: scroll;-webkit-overflow-scrolling: touch;'>"

    // display:block;
    // height:195px;
    // overflow-y:scroll;
    var table_tbody_end = "</tbody></table>";
    $.each(obj_data, function (i, n) {
        var i_str = "samplingRatio_" + i.toString();
        var i_str_ratio = "n_ratio_" + i.toString();
        var i_str_ratio_count = "c_ratio_" + i.toString();
        var i_str_real_ratio = "n_real_ratio_" + i.toString();
        var i_str_ratio_real_count = "c_real_ratio_" + i.toString();
        var i_str_ratio_real_progress = "c_real_progress_" + i.toString();
        var i_str_ratio_real_progress_int = "c_real_progress_int_" + i.toString();
        var i_str_ratio_real_zhuan = "c_real_progress_zhuan_" + i.toString();
        var check_str = i.toString() + "_" + n.ID.toString() + "_" + n.DWMC + "_" + n.COUNT.toString();
        var tr_index = "tr_" + i.toString();
        var table_tr = "<tr style='display: table;width: 100%;table-layout: fixed' id="+tr_index+">" +
            "<td style='width:70px'>" +
            n.ID +
            "</td>" +
            "<td style='width:150px'>" +
            n.DWMC +
            "</td>" +
            "<td style='width:50px' class='ztcount'>" +
            n.COUNT +
            "</td>" +
            "<td style='width:50px' class='cyztcount'>" +
            isEmpty2(n.KCOUNT) +
            "</td>" +
            "<td style='width:50px'>" +
            "<input style='-webkit-appearance: checkbox' type='checkbox' name='coffee' id=" + check_str + " value=" + check_str +
            " onclick='selectBatchSingleAdd(this.id);'>选择" +
            "</td>" +
            "<td style=\"width:50px\">" +
            "<span id=" + i_str_ratio + "  style='color:red' title='应抽样系数'></span>" +
            "</td>" +
            "<td style=\"width:50px\">" +
            "<span id=" + i_str_ratio_count + "  style='color:red' title='应抽样数量'></span>" +
            "</td>" +
            "<td style=\"width:50px\">" +
            "<span id=" + i_str_real_ratio + "  style='color:red' title='实际抽样系数'></span>" +
            "</td>" +
            "<td style=\"width:50px\">" +
            "<span id=" + i_str_ratio_real_count + "  style='color:red' title='实际抽样数量'></span>" +
            "</td>" +
            "<td style='width:50px;text-align: left'>" +
            "<img style='height:10px' id=" + i_str_ratio_real_zhuan + " src='' alt=''/>" +
            "<img id=" + i_str_ratio_real_progress + " src='./jindu2.gif' style='height:10px;width:0px' alt='进度进度为0%' />" +
            "<span id=" + i_str_ratio_real_progress_int + "></span>" +
            "</td>" +
            "</tr>"
        table_head = table_head + table_tr;
    });
    table = table_head + table_tbody_end;
    $('#contents_div').removeAttr("hidden");
    $('#editForm').attr("hidden", "hidden");
    $('#dialog').css("width", "90%");
    $('#dialog').css("height", "80%");
    $('#dialog').css("top", "20%");
    $('#dialog').css("left", "13%");
    $('#contents_div').append(div_controller);
    $('#contents_div').append("<hr>");
    $('#contents_div').append(table);
    $('#contents_div').css("height", "100%");
    $('#tab_opt').css("width", "auto");
    $('#tab_opt').css("height", "80%");
    $(".claseDialogBtn").css("font", "100px");
    // $('#tab_tbody').css("overflow-y","scroll");
    // $('#editForm').css("width","40%");
    // $('#editForm').css("height","50%");
    // $('#sub_div').css("overflow-y","scroll");
    // $('#editForm').append(table);
    $.ajax({
        url: selectProvinceInfo,
        type: 'GET',
        tradition: true,
        data: {},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            var strs = JSON.stringify(arg)
            var obj_data = JSON.parse(arg);
            if (obj_data instanceof Array) {
                $("#selectProvince").append("<option value='-10000000'>选择省份</option>");
                $.each(obj_data, function (i, n) {
                    $("#selectProvince").append("<option value=" + n.shengid + ">" + n.mc + "</option>")
                });
            }
        }
    });
}

/**
 * 生成抽样数据
 */
function edit_obj_sample() {
    var className = "bounceInDown";
    var batchid = $("#batchid").val();
    var cybatchid = $("#cybatchid").val();
    $.ajax({
        url: checkSampledStatus,
        type: 'GET',
        tradition: true,
        data: {cybatchid: cybatchid},
        success: function (arg) {
            /*var callback_dic = $.parseJSON(arg);*/
            /*检测抽样批次的处理状态，如果为 1 则处于保护状态将无法进行数据抽取*/
            var strs = JSON.stringify(arg)
            // var obj_data = JSON.parse(arg);
            if(arg == 1){
                alert("此批抽样数据已保存无法进行进一步操作");
            }else{
                $.ajax({
                    url: getZtidCountOfISPBYbatcid,
                    type: 'GET',
                    tradition: true,
                    data: {batchid: batchid},
                    success: function (arg) {
                        /*var callback_dic = $.parseJSON(arg);*/
                        var strs = JSON.stringify(arg)
                        var obj_data = JSON.parse(arg);
                        tmpArray = obj_data;
                        console.log(obj_data);
                        /*console.info(obj_data[0].fields);
                        console.info(obj_data);*/
                        if (obj_data) {
                            $('#dialogBg').fadeIn(100);
                            $('#dialog').removeAttr('class').addClass('animated ' + className + '').fadeIn();
                            $("#editForm").attr('action', updateUrl);
                            var textStr = $("#operationTitle").text();
                            if (textStr !== null || textStr !== undefined || textStr !== '' || textStr != '修改' + manage_theme) {
                                var type = 1;
                                if (type == 1) {
                                    $("#operationTitle").text("抽样配置");
                                } else {
                                    $("#operationTitle").text("修改" + manage_theme);
                                }
                            }
                            $("#editForm").empty("");
                            to_detail_func(obj_data);
                        } else {
                            alert(); //把错误的信息从后台提出展示出来
                        }
                    }
                });
            }
        }
    });

}

/**/
var addContent = "<ul class='editInfos' style='text-align:center'>"
    //		+ "<li><label><font color='#ff0000'>&nbsp;&nbsp;* </font><span id='span_x'>选择抽样类型</span>："
    //		+ "<select-div.css id='selectSample' name='sampleType' style='width:158px;float:right;' required class='ipt' onchange='selectSampleType(this.options[this.options.selectedIndex].value);'>"
    //		+ "<option value ='0' >请选择抽样类型</option>"
    //		+ "<option value ='1' >省份</option>"
    //		+ "<option value ='2' >运营商</option>"
    //		+ "</select-div.css></label></li><br>"
    //		+ "<li id='li_province'><label><font color='#ff0000'>&nbsp;&nbsp;* </font><span id='span_p'>省份</span>："
    //		+ "<select-div.css id='province' name='selectProvince' style='width:158px;float:right;' required class='ipt'  onchange='selectProvinceType(this.options[this.options.selectedIndex].value);'>"
    //		+ "<option selected='selected'>请选择省份</option>"
    //		+ "</select-div.css></label></li><br>"
    //		+ "<li id='li_isp' hidden='hidden'><label><font color='#ff0000'>&nbsp;&nbsp;* </font><span id='span_y'>运营商</span>："
    //		+ "<select-div.css id='isp' name='selectIsp' style='width:158px;float:right;' required class='ipt'  onchange='selectIspType(this.options[this.options.selectedIndex].value);'>"
    //		+ "<option selected='selected'>请选择运营商</option>"
    //		+ "</select-div.css></label></li><br>"
    + "<li><label><font color='#ff0000'>&nbsp;&nbsp;* </font><span id='span_x'>选择核查批次</span>："
    + "<select-div.css id='dataBatch' name='batchid' style='width:158px;float:right;' required class='ipt'>"
    + "<option value ='0xx' >请选择核查批次</option>"
    + "</select-div.css></label></li><br>"
    + "<li><label><font color='#ff0000'>* </font>设置抽样名称：<input type='text' style='width:158px;float:right;' name='name'  value='' id='add_real_account' class='ipt' /></label><label style='color:red' id='val_add_real_account'></label></li>"
    + "<li><input  style='width:20%' /><input type='button' value='确认提交'  onclick='ajaxButton_set(1)' class='submitBtn' /></li></ul>"

function getSessionName() {
    return $.session.get("username");
}

function checkUndefined(obj) {
    if (obj == undefined) {
        return "";
    } else if (obj == "undefined") {
        return "";
    } else if (obj == "null") {
        return "";
    } else {
        return obj;
    }
}

var sessionName = getSessionName();

$(document).ready(
    function () {
        $('#sideMenu').sideToggle({
            moving: '#sideMenuContainer',
            direction: 'right'
        });
        getSrceenWH();
        // 显示弹框
        $('.box a').click(
            function () {
                className = $(this).attr('class');
                $('#dialogBg').fadeIn(100);
                $('#dialog').removeAttr('class').addClass(
                    'animated ' + className + '').fadeIn();
                /* $("#editForm").attr('action',addUrl); */
                var textStr = $("#operationTitle").text();
                if (textStr !== null || textStr !== undefined
                    || textStr !== ''
                    || textStr != "添加" + manage_theme) {
                    $("#operationTitle").text('添加' + manage_theme);
                }
                $('#contents_div').attr("hidden", "hidden");
                $('#contents_div').html("");
                $("#editForm").removeAttr("hidden");
                $('#dialog').css("display", "block");
                $('#dialog').css("top", "45%");
                $('#dialog').css("left", "45%");
                $('#dialog').css("width", "25%");
                $('#dialog').css("height", "30%");
                // display: block; top: 45%; left: 45%; width: 25%; height: 30%;
                $("#editForm").empty("");
                $('#editForm').append(addContent);
                // $('#dialog').css("width","25%");
                // $('#dialog').css("height","30%");
                // $('#dialog').css("overflow-y","");
                selectAllBatch();
            });

        // 关闭弹窗
        $('.claseDialogBtn').click(function () {
            $('#dialog').addClass('bounceOutUp').fadeOut();
            $('#dialogBg').fadeOut();
            /*
             * $('#dialogBg').fadeOut(50,function(){
             * $('#dialog').addClass('bounceOutUp').fadeOut(); });
             */
            $("#editForm").empty("");
            // $("#editForm").hide();
            // $("#editForm").attr("hidden","hidden");
            $("#contents_div").empty("");
            // $("#contents_div").hide();
            // $("#contents_div").attr("hidden","hidden");
            $("#operationTitle").text("");
        });

        var username = getSessionName();
        if (username) {
            $("#welcome_user").text("欢迎:  " + username);
            // console.log(username);
        } else {
            $("#username").attr("href", "../main/to_login")
            $("#welcome_user").text("请登录");
        }
        $("#tbody_id").empty("");
        // datalist(1);
        selectSampleType(1);
        selectCybatchid();
    });

var w, h, className;

function getSrceenWH() {
    w = $(window).width();
    h = $(window).height();
    $('#dialogBg').width(w).height(h);
}

window.onresize = function () {
    getSrceenWH();
}
$(window).resize();

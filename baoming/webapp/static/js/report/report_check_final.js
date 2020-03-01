//获取当前时间，格式YYYY-MM-DD
function getNowFormatDate() {
    let date = new Date();
    let seperator1 = "-";
    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    return year + seperator1 + month + seperator1 + strDate;
}

/**
 * 判断学徒期开始时间
 * @param obj
 */
function change_apprentice_time_start(obj) {
    if (obj.length === 10) {
        let dates_start = obj.split("-");
        let year = parseInt(dates_start[0]);
        let month = parseInt(dates_start[1]);
        let day = parseInt(dates_start[2]);
        let date = new Date();
        let flag = false;
        if (year > date.getFullYear()) {
            alert("不应大于：" + date.getFullYear() + ":年");
            this.value = "";
            $('#continue').attr('disabled', 'disabled');
        } else if (year === date.getFullYear()) {
            if (month > date.getMonth() + 1) {
                alert("不应大于：" + date.getFullYear() + ":年，" + (date.getMonth() + 1) + ":月");
                this.value = "";
                $('#continue').attr('disabled', 'disabled');
                this.focus();
            } else if (month === date.getMonth() + 1) {
                // alert(date.getDate());
                if (day >= date.getDate() + 1) {
                    alert("不应大于：" + date.getFullYear() + ":年，" + (date.getMonth() + 1) + ":月, " + date.getDate() + ":日");
                    this.value = "";
                    $('#continue').attr('disabled', 'disabled');
                } else {
                    flag = true;
                }
            } else {
                flag = true;
            }
        } else {
            flag = true;
        }

        if (flag) {
            computer();
            // let end = $("#apprentice_end");
            // if (end.length === 10) {
            //     //  如果有数据直接计算，没有数据只是聚焦
            //     computer();
            // } else {
            //     end.focus();
            // }
        } else {
            this.focus();
        }
    } else {
        alert("开始时间未输入，或输入格式错误，请查证后重置！");
    }
}

/**
 * 判断学徒期结束时间
 * @param obj
 */
function change_apprentice_time_end(obj) {
    if (obj.length === 10) {
        let dates_end = obj.split("-");
        let year = parseInt(dates_end[0]);
        let month = parseInt(dates_end[1]);
        let day = parseInt(dates_end[2]);
        let date = new Date();
        let flag = false;
        if (year > date.getFullYear()) {
            alert("不应大于：" + date.getFullYear() + ":年");
            this.value = "";
            $('#continue').attr('disabled', 'disabled');
        } else if (year === date.getFullYear()) {
            if (month > date.getMonth() + 1) {
                alert("不应大于：" + date.getFullYear() + ":年，" + (date.getMonth() + 1) + ":月");
                this.value = "";
                $('#continue').attr('disabled', 'disabled');
            } else if (month === date.getMonth() + 1) {
                if (day >= date.getDate() + 1) {
                    alert("不应大于：" + date.getFullYear() + ":年，" + (date.getMonth() + 1) + ":月, " + date.getDate() + ":日");
                    this.value = "";
                    $('#continue').attr('disabled', 'disabled');
                } else {
                    flag = true;
                }
            } else {
                flag = true;
            }
        } else {
            flag = true;
        }

        if (flag) {
            computer();
            // let start = $("#apprentice_start");
            // alert(start.length);
            // if (start.length === 10) {
            //     //  如果有数据直接计算，没有数据只是聚焦
            //
            // } else {
            //     start.focus();
            // }
        }else{
            this.focus();
        }
        // } else {
        //     $('#apprentice_year').val(0);
        //     $('#apprentice_month').val(0);
        // }
    } else {
        alert("结束时间未输入，或输入格式错误，请查证后重置！");
    }
}

function computer() {
    
    let end = $("#apprentice_end").val();
    let start = $("#apprentice_start").val();
    if (typeof end === "undefined" && end.length === 0 || end === '') {
        $('#continue').attr('disabled', 'disabled');
        $("#apprentice_end").focus();
    } else {
        if (typeof start === "undefined" && start.length === 0 || start === '') {
            $('#continue').attr('disabled', 'disabled');
            $("#apprentice_start").focus();
        } else {
            if (start.length === 10) {
                if (end.length === 10) {
                    let dates_end = end.split("-");
                    let year = parseInt(dates_end[0]);
                    let month = parseInt(dates_end[1]);
                    let day = parseInt(dates_end[2]);


                    let dates_start = start.split('-');
                    let year_start = parseInt(dates_start[0]);
                    let month_start = parseInt(dates_start[1]);
                    let day_start = parseInt(dates_start[2]);
                    let years = year - year_start;
                    let full_days = years * 365;
                    let full_month_days_start_day = month_to_days(month) + day;
                    let full_month_days_old_day = month_to_days(month_start) + day_start;
                    let days = (full_month_days_start_day - full_month_days_old_day) + full_days;
                    if (years < 0) {
                        alert("结束年份应大于或等于开始年份，请重置开始时间，或者结束时间！");
                        this.value = "";
                        $('#continue').attr('disabled', 'disabled');
                    } else {
                        if (days <= 0) {
                            alert("结束日期应大于开始日期，请重置开始时间，或者结束时间！");
                            this.value = "";
                            $('#continue').attr('disabled', 'disabled');
                        } else {
                            let f_year = Math.floor(days / 365);
                            if (f_year === 0) {
                                $('#apprentice_year').val(0);
                                $('#apprentice_year_label').text(" :年  ");
                                let l_day = days - (f_year * 365);
                                let f_month = Math.floor(l_day / 30);
                                if (f_month > 0) {
                                    if (f_month === 12) {
                                        f_year = f_year + 1;
                                        $('#apprentice_year').val(f_year);
                                        $('#apprentice_year_label').text(f_year.toString() + " :年  ");
                                        $('#apprentice_month').val(0);
                                        $('#apprentice_month_label').text(" :月");
                                    } else {
                                        $('#apprentice_year').val(0);
                                        $('#apprentice_year_label').text(" :年  ");
                                        $('#apprentice_month').val(f_month);
                                        $('#apprentice_month_label').text(f_month.toString() + " :月");
                                    }
                                } else {
                                    $('#apprentice_month').val(0);
                                }
                                $('#continue').removeAttr('disabled');
                            } else if (f_year >= 1) {
                                $('#apprentice_year').val(f_year);
                                $('#apprentice_year_label').text(f_year.toString() + " :年  ");
                                let l_day = days - (f_year * 365);
                                let f_month = Math.floor(l_day / 30);
                                if (f_month > 0) {
                                    if (f_month === 12) {
                                        f_year = f_year + 1;
                                        $('#apprentice_year').val(f_year);
                                        $('#apprentice_year_label').text(f_year.toString() + " :年  ");
                                        $('#apprentice_month').val(0);
                                        $('#apprentice_month_label').text(" :月");
                                    } else {
                                        $('#apprentice_year').val(f_year);
                                        $('#apprentice_year_label').text(f_year.toString() + " :年  ");
                                        $('#apprentice_month').val(f_month);
                                        $('#apprentice_month_label').text(f_month.toString() + " :月");
                                    }
                                } else {
                                    $('#apprentice_month').val(0);
                                }
                                $('#continue').removeAttr('disabled');
                            } else {
                                $('#apprentice_year').val(0);
                                let f_month = Math.floor(days / 30);
                                if (f_month > 0) {
                                    if (f_month === 12) {
                                        f_year = f_year + 1;
                                        $('#apprentice_year').val(1);
                                        $('#apprentice_year_label').text("1 :年  ");
                                        $('#apprentice_month').val(0);
                                        $('#apprentice_month_label').text(" :月");
                                    } else {
                                        $('#apprentice_year').val(f_year);
                                        $('#apprentice_year_label').text(f_year.toString() + " :年  ");
                                        $('#apprentice_month').val(f_month);
                                        $('#apprentice_month_label').text(f_month.toString() + " :月");
                                    }
                                    $('#continue').removeAttr('disabled');
                                } else {
                                    alert("学徒期不满一月，请重置开始和结束时间，或者联系管理员！");
                                    this.value = "";
                                    $('#continue').attr('disabled', 'disabled');
                                    $('#apprentice_month').val(0);
                                    start.focus();
                                }
                            }
                        }
                    }
                } else {
                    alert("时间输入不正确！");
                }
            } else {
                alert("时间输入不正确！");
            }
        }
    }
    // } else {
    //     console.log('时间验证未通过！');
    //     $('#apprentice_year').val(0);
    //     $('#apprentice_month').val(0);
    // }
    //
}


function change_start_the_work_of_this_occupation(obj) {

    let dates = obj.split("-");
    let year = parseInt(dates[0]);
    let month = parseInt(dates[1]);
    let day = parseInt(dates[2]);
    let date = new Date();
    let flag = false;
    if (year > date.getFullYear()) {
        alert("不应大于：" + date.getFullYear() + ":年");
        this.value = "";
        $('#continue').attr('disabled', 'disabled');
    } else if (year === date.getFullYear()) {
        if (month > date.getMonth() + 1) {
            alert("不应大于：" + date.getFullYear() + ":年，" + (date.getMonth() + 1) + ":月");
            this.value = "";
            $('#continue').attr('disabled', 'disabled');
        } else if (month === date.getMonth() + 1) {
            if (day >= date.getDate() + 1) {
                alert("不应大于：" + date.getFullYear() + ":年，" + (date.getMonth() + 1) + ":月, " + date.getDate() + ":日");
                this.value = "";
                $('#continue').attr('disabled', 'disabled');
            } else {
                flag = true;
            }
        } else {
            flag = true;
        }
    } else {
        flag = true;
    }

    if (flag) {

    }

    let final_years = 0;
    if (parseInt(year) > date.getFullYear()) {
        alert("您的输入有误，请重置时间或不再继续填写！");
        $('#continue').attr('disabled', 'disabled');
    } else if (parseInt(year) === date.getFullYear()) {
        alert("您的工作年限未满一年，请重置时间或不再继续填写！");
        $('#continue').attr('disabled', 'disabled');
    } else {

        let years = date.getFullYear() - year;
        let full_days = years * 365;
        let full_month_days_old = month_to_days(month) + parseInt(day);
        let full_month_days_new = month_to_days(date.getMonth() + 1) + date.getDate();
        if (full_month_days_new === full_month_days_old) {
            final_years = years;
        } else if (full_month_days_new > full_month_days_old) {
            //天数多，但是不足一年
            final_years = years;
        } else if (full_month_days_new < full_month_days_old) {
            //天数多，但是不足一年
            final_years = years - 1;
        }
    }

    let need_years = $('#career_life_time').val();
    let career_life = $('#career_life');
    let career_life_label_value = $("#career_life_label_value");
    if (final_years < need_years) {
        career_life.val(final_years);
        career_life_label_value.text(final_years.toString() + " :年   ");
        career_life.attr('readonly', 'readonly');
        career_life.css('color', 'red');
        $('#career_life_label').text('从事本职业年限不足');
        $('#continue').attr('disabled', 'disabled');
    } else {
        career_life.val(final_years);
        career_life_label_value.text(final_years.toString() + " :年   ");
        career_life.attr('readonly', 'readonly');
        career_life.css('color', 'black');
        $('#career_life_label').text("");
        $('#continue').removeAttr('disabled');
    }
}


function change_original_certificate_worker_time(obj) {
    let final_years = 0;

    let date = new Date();
    let dates = obj.split("-");
    let year = dates[0];
    let month = dates[1];
    let day_string = dates[2];

    if (parseInt(year) > date.getFullYear()) {
        alert("您的输入有误，请重置时间或不再继续填写！");
        $('#continue').attr('disabled', 'disabled');
    } else if (parseInt(year) === date.getFullYear()) {
        let from_certificate_need_year = $('#from_certificate_need_year').val();
        if (from_certificate_need_year === "0") {
            console.log("获得证书后，没有工作时间年限要求！");
        } else {
            alert("您的工作年限未满一年，请重置时间或不再继续填写！");
            $('#continue').attr('disabled', 'disabled');
        }
    } else {

        let years = date.getFullYear() - parseInt(year);
        let full_days = years * 365;
        let full_month_days_old = month_to_days(parseInt(month)) + parseInt(day_string);
        let full_month_days_new = month_to_days(date.getMonth() + 1) + date.getDate();
        if (full_month_days_new === full_month_days_old) {
            final_years = years;
        } else if (full_month_days_new > full_month_days_old) {
            //天数多，但是不足一年
            final_years = years;
        } else if (full_month_days_new < full_month_days_old) {
            //天数多，但是不足一年
            final_years = years - 1;
        }
    }

    let need_years = $('#from_certificate_need_year');
    let original_certificate_worker_year = $('#original_certificate_worker_year');
    let original_certificate_worker_year_value = $('#original_certificate_worker_year_value');

    if (final_years < need_years.val()) {
        original_certificate_worker_year.val(final_years);
        original_certificate_worker_year_value.text(final_years.toString() + " ：年  ");
        original_certificate_worker_year.attr('readonly', 'readonly');
        original_certificate_worker_year.css('color', 'red');
        need_years.css('color', 'red');
        $('#original_certificate_worker_year_label').text('从事本职业年限不足');
        $('#continue').attr('disabled', 'disabled');
    } else {
        original_certificate_worker_year.val(final_years);
        original_certificate_worker_year_value.text(final_years.toString() + " ：年  ");
        original_certificate_worker_year.attr('readonly', 'readonly');
        original_certificate_worker_year.css('color', 'black');
        $('#original_certificate_worker_year_label').text("");
        $('#continue').removeAttr('disabled');
    }

    // if (need_years == 0) {
    //         //如果本职业工作年限要求为0 则不显示
    //         $('.original_certificate_worker_time').hide();
    // } else {
    //
    // }
}

function month_to_days(month) {
    let months = {
        '1': 31,
        '2': 28,
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31
    };
    let day = 0;
    for (let i = 1; i <= month; i++) {
        day = day + months[i];
    }
    return day;
}

function change_graduation_result(graduation_time) {
    $("#condition-b").val("");
    $("#condition-b-update").val("");
    $('.strict_status').hide();
    $('.graduation_result_1').show();
    let strict_status = $("#graduation_status").attr('data-strict');
    let dates = graduation_time.split("-");
    let year = parseInt(dates[0]);
    let month = parseInt(dates[1]);
    let day = parseInt(dates[2]);

    let date = new Date();
    let full_month_days_old = month_to_days(month) + parseInt(day);
    let full_month_days_new = month_to_days(date.getMonth() + 1) + date.getDate();
    let diploma_certificate_photos_class = $('.diploma_certificate_photos');
    let diploma_certificate_photos_id = $('#diploma_certificate_photos');
    if (date.getFullYear() > year) {
        $("#graduation_result_0").prop("checked", "checked");
        diploma_certificate_photos_class.show();
        diploma_certificate_photos_id.attr('required', 'required');
        $("#condition-b").val("condition-b");
        $('#continue').removeAttr('disabled');
    } else if (date.getFullYear() === year) {
        if (full_month_days_new > full_month_days_old) {
            $("#graduation_result_0").prop("checked", "checked");
            diploma_certificate_photos_class.show();
            diploma_certificate_photos_id.attr('required', 'required');
            $('#continue').removeAttr('disabled');
            $("#condition-b").val("condition-b");
        } else {
            if (strict_status === "true") {
                $("#graduation_result_0").prop("checked", "checked");
                diploma_certificate_photos_class.show();
                diploma_certificate_photos_id.attr('required', 'required');
                $('.strict_status').show();
                $('.graduation_result_1').hide();
                $('#continue').attr('disabled', 'disabled');
                $("#condition-b").val("condition-b");
                $("#condition-b-update").val("condition-b-update");
            } else {
                $("#graduation_result_1").prop("checked", "checked");
                diploma_certificate_photos_class.hide();
                diploma_certificate_photos_id.removeAttr('required');
                $('#continue').removeAttr('disabled');
            }
        }
    } else {
        if (strict_status === "true") {
            $("#graduation_result_0").prop("checked", "checked");
            diploma_certificate_photos_class.show();
            diploma_certificate_photos_id.attr('required', 'required');
            $('.strict_status').show();
            $('.graduation_result_1').hide();
            $('#continue').attr('disabled', 'disabled');
            $("#condition-b").val("condition-b");
            $("#condition-b-update").val("condition-b-update");
        } else {
            $("#graduation_result_1").prop("checked", "checked");
            diploma_certificate_photos_class.hide();
            diploma_certificate_photos_id.removeAttr('required');
            $('#continue').removeAttr('disabled');
        }
    }

}

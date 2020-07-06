/**
 * 按照条件显示输入框
 * @param condition_string 填报选项
 * @param status 条件生成状态
 */
function condition_controller(condition_string, status) {
    if (status === "add") {
        clear_input_label();
    } else {
        console.log("修改不需要清空数据");
    }

    let form_inputs = $("#add-student-info-id input");
    for (let i = 0; i < form_inputs.length; i++) {
        form_inputs[i].required = false;
        // form_inputs[i].value = "";
    }


    $("#condition_selected_value").val(condition_string);
    let apprentice_class = $('.apprentice');

    let apprentice_start_class = $(".apprentice_start").hide();
    $(".apprentice_end").hide();
    //========================================================================================
    //是否需要
    let qualification_class = $('.has_qualification');
    let graduation_status_class = $('.graduation_status');
    let condition_selected_class = $('.condition_selected');
    //职业年限
    let career_life_class = $(".career_life");
    //从事本职业工作开始时间
    let start_the_work_of_this_occupation_class = $(".start_the_work_of_this_occupation");
    //术等级（原级别）
    let primary_level_class = $(".primary_level");
    // 现持有职业资格证书编号(原证书编号)
    let original_certificate_number_class = $(".original_certificate_number");
    // 现有证件发证单位
    let issue_unit_class = $(".issue_unit");
    //现有职业资格证发证时间
    let issuance_time_class = $(".issuance_time");

    // 职业资格证图片上传
    let certificate_photos_class = $('.certificate_photos');
    //=========================================================================================

    // // 学历程度
    //     let education_degree_class = $(".education_degree");
    //毕业（应届）院校名称
    let school_name_class = $(".school_name");
    // 毕业时间(或即将毕业时间)
    let graduation_time_class = $(".graduation_time");
    //专业工种(或相关专业工种)
    let profession_class = $(".profession");

    //被授予毕业资格证书名称
    let diploma_granted_class = $(".diploma_granted");
    // 毕业证图片上传
    let diploma_certificate_photos_class = $('.diploma_certificate_photos');

    apprentice_class.hide();
    career_life_class.hide();
    start_the_work_of_this_occupation_class.hide();

    graduation_status_class.hide();
    // 职业年限情况
    career_life_class.hide();
    profession_class.hide();
    start_the_work_of_this_occupation_class.hide();
    $('.career_life_time').hide();
    $(".course_hours").hide();
    //有关证书情况
    primary_level_class.hide();
    original_certificate_number_class.hide();
    issue_unit_class.hide();
    issuance_time_class.hide();
    $('.from_certificate_need_year').hide();
    $('.original_certificate_worker_time').hide();

    certificate_photos_class.hide();
    // 院校毕业证书情况
    $('.education_degree_form').hide();
    school_name_class.hide();
    graduation_time_class.hide();
    $('.graduation_worker_time').hide();
    $('.strict_status').hide();
    $('.major').hide();

    diploma_certificate_photos_class.hide();


    let title_level = {
        '3': "高级工",
        '4': "中级工",
        '5': "初级工"
    };

    if (condition_string.indexOf('dhg') > -1) {
        // 电焊工
        // dhg05 = ['(1) 累计从事本职业工作１年( 含)以上。', '(2) 本职业学徒期满。'];
        if (condition_string.indexOf("dhg05") > -1) {
            //五级（初级）
            if (condition_string.indexOf("dhg05_1") > -1) {
                //第1个条件
                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);
            } else if (condition_string.indexOf("dhg05_2") > -1) {
                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }
        } else if (condition_string.indexOf("dhg04") > -1) {
            //四级（中级）
            // dhg04 = ['(1) 取得本职业五级/ 初级工职业资格证书( 技能等级证书)后，累计从事本职业工作４年(含)以上。',
            // '(2) 累计从事本职业工作６年(含)以上。',
            // '(3__1) 取得技工学校本专业或相关专业毕业证书(含尚未取得毕业证书的在校应届毕业生)；',
            // '(3__2) 或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ' +
            // '( 含尚未取得毕业证书的在校应届毕业生)。', '注：相关专业：焊接加工、焊接技术应用、金属热加工（焊接）、焊接技术与自动化、焊接技术与工程。'];
            if (condition_string.indexOf("dhg04_1") > -1) {
                //第1个条件
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);
            } else if (condition_string.indexOf("dhg04_2") > -1) {
                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dhg04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //===============================

            } else if (condition_string.indexOf("dhg04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //===============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }

        } else if (condition_string.indexOf("dhg03") > -1) {
            //高级（三级）

            //          dhg03 = ['(1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作５ 年( 含) 以上。',
            // '(2__1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；' ,
            // '(2__2)或取得本职业四级/ 中级工职业资格证书，并具有经评估论证、 以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 (含尚未取得毕业证书的在校应届毕业生)。',
            // '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业工作２年( 含) 以上。', '注：相关专业：焊接加工、焊接技术应用、金属热加工（焊接）、焊接技术与自动化、焊接技术与工程。'];

            if (condition_string.indexOf("dhg03_1") > -1) {
                //第1个条件
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dhg03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false, 4); //======================================

            } else if (condition_string.indexOf("dhg03_3__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false, 5); //======================================

            } else if (condition_string.indexOf("dhg03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('dg') > -1) {
        // 电工
        if (condition_string.indexOf("dg05") > -1) {
            //五级（初级）
            // dg05 = ['(1) 累计从事本职业工作１年( 含)以上。', '(2) 本职业学徒期满。'];
            if (condition_string.indexOf("dg05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dg05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("dg04") > -1) {

            //dg04 = ['(1) 取得本职业五级/ 初级工职业资格证书( 技能等级证书)后，累计从事本职业工作４年(含)以上。',
            // '(2) 累计从事本职业工作６年(含)以上。',
            // '(3__1) 取得技工学校本专业或相关专业毕业证书( 含尚未取得毕业证书的在校应届毕业生)；' ,
            // '(3__2)或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。', '注：本专业或相关专业: 数控机床装配与维修、机械设备装配与自动控制、制冷设备运用与维修、机电设备安装与维修、机电一体化、电气自动化设备安装与维修 、电梯工程技术、城市轨道交通车辆运用与检修 、煤矿电气设备维修、' +
            // ' 工业机器人应用与维护、工业网络技术、机电技术应用、电气运行与控制、电气技术应用、纺织机电技术、铁道供电技术、农业电气化技术等专业。'];
            if (condition_string.indexOf("dg04_1") > -1) {
                //第1个条件
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dg04_2") > -1) {
                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dg04_3__1") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false);

            } else if (condition_string.indexOf("dg04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }

        } else if (condition_string.indexOf("dg03") > -1) {
            //高级（三级）

            //         dg03 = ['(1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作５ 年( 含) 以上',
            // '(2__1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；',
            // '(2__2)或取得本职业四级/ 中级工职业资格证书，并具有经评估论证、 以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 (含尚未取得毕业证书的在校应届毕业生)。',
            // '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业工作２年( 含) 以上。',
            if (condition_string.indexOf("dg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dg03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false, 4); //=============================

            } else if (condition_string.indexOf("dg03_3__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, true, false); //=============================

            } else if (condition_string.indexOf("dg03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('qg') > -1) {
        // 钳工
        if (condition_string.indexOf("qg05") > -1) {
            //五级（初级）
            if (condition_string.indexOf("qg05_1") > -1) {
                //第1个条件
                //qg05 = ['(1) 经本职业初级正规培训达规定标准学时数，并取得结业证书。',
                // '(2) 在本职业连续见习工作 2 年以上。',
                // '(3) 本职业学徒期满。'];

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 9, false);
            } else if (condition_string.indexOf("qg05_2") > -1) {
                career_life_time(2);
                check_graduation_status(2);
                apprentice_check(false);
                check_has_qualification(2);
            } else if (condition_string.indexOf("qg05_3") > -1) {
                career_life_time();
                check_graduation_status(2);
                apprentice_check(true);
                check_has_qualification(2);
            } else {
                console.log("获取失败！");
            }
        } else if (condition_string.indexOf("qg04") > -1) {
            //四级（中级）
            // let qg04 = ['(1) 取得本职业初级职业资格证书后，连续从事本职业工作 3 年以上，经本职业中级正规培训达规定标准学时数，并取得结业证书。',
            //      '(2) 取得本职业初级职业资格证书后，连续从事本职业工作 5 年以上。',
            //     '(3) 连续从事本职业工作 7 年以上。',
            //     '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。'];

            if (condition_string.indexOf("qg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 3);
                check_graduation_status(1, 10, false, true);

            } else if (condition_string.indexOf("qg04_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("qg04_3") > -1) {

                career_life_time(7);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("qg04_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("qg03") > -1) {
            //高级（三级）

            //         qg03 = ['(1) 取得本职业中级职业资格证书后，连续从事本职业工作 4 年以上，经本职业高级正规培训达规定标准学时数，并取得结业证书。',
            // '(2) 取得本职业中级职业资格证书后，连续从事本职业工作 7 年以上。',
            // '(3__1）取得高级技工学校结业证书。',
            // '(3__2)或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校毕业证书。',
            // '(3__3)或高级技工学校本职业 ( 专业 ) 毕业证书。',
            // '(4) 大专以上本专业或相关专业毕业生取得本职业中级职业资格证书后, 连续从事本职业工作 2 年以上。'];

            //             ——高级 ( 具备下列条件之一者〉
            // (1) 取得本职业中级职业资格证书后，连续从事本职业工作 4 年以上，经本职业高级正规培训达规定标准学时数，并取得结业证书。
            // (2) 取得本职业中级职业资格证书后，连续从事本职业工作 7 年以上。
            // (3) 取得高级技工学校或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校或高级技工学校本职业 ( 专业 ) 毕业证书。
            // (4) 大专以上本专业或相关专业毕业生取得本职业中级职业资格证书后, 连续从事本职业工作 2 年以上。

            if (condition_string.indexOf("qg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 4);
                check_graduation_status(1, 11, false, true);

            } else if (condition_string.indexOf("qg03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 7);
                check_graduation_status(2);

            } else if (condition_string.indexOf("qg03_3") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 4, false, true);

            } else if (condition_string.indexOf("qg03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, false, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('yyy') > -1) {
        // 育婴员
        if (condition_string.indexOf("yyy05") > -1) {
            //五级（初级）
            // yyy05 = ['(1)经本职业初级正规培训达规定标准学时数，并取得结业证书。', '（2）在本职业连续见习工作2年以上。', '（3）本职业学徒期满。'];
            if (condition_string.indexOf("yyy05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_graduation_status(2);
                check_has_qualification(2);

            } else if (condition_string.indexOf("yyy05_2") > -1) {
                career_life_time();
                apprentice_check(true);
                check_graduation_status(2);
                check_has_qualification(2);
            } else {
                console.log("获取失败！");
            }
            // } else if (condition_string.indexOf("yyy05_3") > -1) {
            //     career_life_time();
            //     apprentice_check(true);
            //     check_graduation_status(2);
            //     check_has_qualification(2);
            // } else {
            //     console.log("获取失败！");
            // }
        } else if (condition_string.indexOf("yyy04") > -1) {
            //四级（中级）
            //2019-0903 修订
            //——四级/中级工（具备以下条件之一者）
            // （1）取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作 4 年（含）以上。
            // （2）累计从事本职业或相关职业工作 6 年（含）以上。
            // （3-1）取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；
            // （3-2）或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。
            if (condition_string.indexOf("yyy04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check();
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("yyy04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("yyy04_3") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, true);

            } else if (condition_string.indexOf("yyy04_4") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("yyy03") > -1) {
            //高级（三级）

            //——三级/高级工（具备以下条件之一者）
            // （1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作５年（含）以上。
            // （2-1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；
            // （2-2）或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。
            // （3）具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作２年（含）以上。
            // 注：
            // 1、相关职业：婴幼儿发展引导员、幼儿教育教师、儿科医师、儿科护士、孤残儿童护理员、母婴保健技术服务人员、保健调理师、健康管理师、保育员、家政服务员。
            // 2、本专业：学前教育、早期教育。
            // 3、相关专业:中职：护理、中医护理、家政服务与管理、营养与保健；高职高专：护理、预防医学、公共卫生管理、人口与家庭发展服务、临床医学、中医学、食品营养与卫生、健康管理、医学营养、心理咨询、营养配餐、特殊教育、心理健康教育、幼儿发展与健康管理、中医康复技术；普通高校：护理学、基础医学、预防医学、中医学、妇幼保健医学、针灸推拿、教育学、小学教育。

            if (condition_string.indexOf("yyy03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("yyy03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 3, false, true);

            } else if (condition_string.indexOf("yyy03_3") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 3, false, true);

                // } else if (condition_string.indexOf("yyy03_4__2") > -1) {
                //
                //     career_life_time();
                //     apprentice_check(false);
                //     check_has_qualification(2);
                //     check_graduation_status(1, 5, false);

            } else if (condition_string.indexOf("yyy03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 3, false, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('byy') > -1) {
        // 保育员
        if (condition_string.indexOf("byy05") > -1) {
            //五级（初级）
            //              ——五级/初级工（具备以下条件之一者 ）
            // （1）累计从事本职业或相关职业工作１年（含）以上。
            // （2）本职业或相关职业学徒期满。
            if (condition_string.indexOf("byy05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("byy05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);
            } else {
                console.log("获取失败！");
            }
        } else if (condition_string.indexOf("byy04") > -1) {
            //——四级/中级工（具备以下条件之一者）
            // （1）取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作 4 年（含）以上。
            // （2）累计从事本职业或相关职业工作 6 年（含）以上。
            // （3-1）取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；
            // （3-2）或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（ 含尚未取得毕业证书的在校应届毕业生）。
            if (condition_string.indexOf("byy04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("byy04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("byy04_3") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, true);

            } else if (condition_string.indexOf("byy04_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("byy03") > -1) {
            //高级（三级）
            //——三级/高级工（具备以下条件之一者 ）
            // （1）取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作５年（含）以上。
            // （2-1）取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书），并具有高级技工学校、 技师学院毕业证书 （含尚未取得毕业证书的在校应届毕业生）；
            // （2-2）或取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 （ 含尚未取得毕业证书的在校应届毕业生）。
            // （3） 具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/ 中级工职业资格证书 （ 技能等级证书）后，累计从事本职业或相关职业工作２年（ 含） 以上。
            // 注：
            // 1、相关职业：婴幼儿发展引导员、幼儿教师、儿科医师、儿科护士、孤残儿童护理员、母婴保健技术服务人员、保健护理师、健康管理师、育婴员、家政服务员等。
            // 2、本专业：学前教育、早期教育。
            // 3、相关专业:中职：护理、中医护理、家政服务与管理、营养与保健、助产；高职高专：护理、预防医学、公共卫生管理、人口与家庭发展服务、临床医学、中医学、食品营养与卫生、健康管理、医学营养、心理咨询、特殊教育、心理健康教育、幼儿发展与健康管理；普通高校：护理学、基础医学、预防医学、中医学、妇幼保健医学、教育学。
            if (condition_string.indexOf("byy03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("byy03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 4, false, true);

            } else if (condition_string.indexOf("byy03_3") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 4, false, true);
                //
                // } else if (condition_string.indexOf("byy03_4__2") > -1) {
                //
                //     career_life_time();
                //     apprentice_check(false);
                //     check_has_qualification(2);
                //     check_graduation_status(1, 5, false, true);

            } else if (condition_string.indexOf("byy03_4") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('hg') > -1) {
        // 化工
        if (condition_string.indexOf("hg05") > -1) {
            //五级（初级）
            //         （1）累计从事本职业或相关职业工作1年（含）以上。',
            // '（2）本职业或相关职业学徒期满。'
            if (condition_string.indexOf("hg05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("hg05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("hg04") > -1) {

            //四级（中级）

            //         hg04 = ['（1）取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
            // '（2）累计从事本职业或相关职业工作6年（含）以上。',
            // '（3__1）取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（3__2）或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。'
            if (condition_string.indexOf("hg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("hg04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);
            } else if (condition_string.indexOf("hg04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("hg04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("hg03") > -1) {
            //高级（三级）

            //         hg03 = ['（1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作5年（含）以上。',
            // '（2__1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（2__2）或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
            // '（3）具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作2年（含）以上。',
            if (condition_string.indexOf("hg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("hg03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false, 4);

            } else if (condition_string.indexOf("hg03_3__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("hg03_4") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('hxjyy') > -1) {
        // 化工
        if (condition_string.indexOf("hxjyy05") > -1) {
            //五级（初级）
            //         （1）累计从事本职业或相关职业工作1年（含）以上。',
            // '（2）本职业或相关职业学徒期满。'
            if (condition_string.indexOf("hxjyy05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("hxjyy05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("hxjyy04") > -1) {

            //四级（中级）

            //         hg04 = ['（1）取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
            // '（2）累计从事本职业或相关职业工作6年（含）以上。',
            // '（3__1）取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（3__2）或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。'
            if (condition_string.indexOf("hxjyy04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("hxjyy04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);
            } else if (condition_string.indexOf("hxjyy04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("hxjyy04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("hxjyy03") > -1) {
            //高级（三级）

            //         hg03 = ['（1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作5年（含）以上。',
            // '（2__1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（2__2）或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
            // '（3）具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作2年（含）以上。',
            if (condition_string.indexOf("hxjyy03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("hxjyy03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false, 4);

            } else if (condition_string.indexOf("hxjyy03_3") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("hxjyy03_4") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('ffsg') > -1) {
        // 化工
        if (condition_string.indexOf("ffsg05") > -1) {
            //五级（初级）
            //         （1）累计从事本职业或相关职业工作1年（含）以上。',
            // '（2）本职业或相关职业学徒期满。'
            if (condition_string.indexOf("ffsg05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("ffsg05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("ffsg04") > -1) {

            //四级（中级）
            //         hg04 = ['（1）取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
            // '（2）累计从事本职业或相关职业工作6年（含）以上。',
            // '（3__1）取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（3__2）或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。'
            if (condition_string.indexOf("ffsg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("ffsg04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("ffsg04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("ffsg04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("ffsg03") > -1) {
            //高级（三级）

            //         hg03 = ['（1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作5年（含）以上。',
            // '（2__1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（2__2）或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
            // '（3）具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作2年（含）以上。',
            if (condition_string.indexOf("ffsg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("ffsg03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false, 4);

            } else if (condition_string.indexOf("ffsg03_3__2") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("ffsg03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('wjhxfyscg') > -1) {
        // 化工
        if (condition_string.indexOf("wjhxfyscg05") > -1) {
            //五级（初级）
            //         （1）累计从事本职业或相关职业工作1年（含）以上。',
            // '（2）本职业或相关职业学徒期满。'
            if (condition_string.indexOf("wjhxfyscg05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("wjhxfyscg05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("wjhxfyscg04") > -1) {

            //四级（中级）

            //         hg04 = ['（1）取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
            // '（2）累计从事本职业或相关职业工作6年（含）以上。',
            // '（3__1）取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（3__2）或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。'
            if (condition_string.indexOf("wjhxfyscg04_1") > -1) {
                //第1个条件
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);
            } else if (condition_string.indexOf("wjhxfyscg04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);
            } else if (condition_string.indexOf("wjhxfyscg04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================
            } else if (condition_string.indexOf("wjhxfyscg04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================
            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("wjhxfyscg03") > -1) {
            //高级（三级）

            //         hg03 = ['（1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作5年（含）以上。',
            // '（2__1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（2__2）或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
            // '（3）具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作2年（含）以上。',
            if (condition_string.indexOf("wjhxfyscg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);
            } else if (condition_string.indexOf("wjhxfyscg03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false, 4);
            } else if (condition_string.indexOf("wjhxfyscg03_3__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);
            } else if (condition_string.indexOf("wjhxfyscg03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);
            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('ld') > -1) {
        // 化工
        if (condition_string.indexOf("ld04") > -1) {

            //四级（中级）
            //         ld04 = ['（1） 累计从事本职业或相关职业工作 4 年（含）以上。 ',
            // '（2__1） 取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（2__2）或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
            // '（3）高等院校本专业或相关专业在校生。 ', '注：\n' +
            // '1、相关职业：人力资源管理、劳动保障事务处理、社会工作等职业。 \n' +
            // '2、相关专业：劳动与社会保障、劳动经济学、人力资源管理、工商企业管理、法学、社会学等专业。 \n' +
            // '3、相关职业资格证书（技能等级证书）:企业人力资源管理师、劳动保障协理员、劳动保障专理员、社会工作者等与劳动关系协调员职业功能具有关联性的职业资格证书。'];
            if (condition_string.indexOf("04_1") > -1) {
                //第1个条件

                career_life_time(4);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);
            } else if (condition_string.indexOf("04_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //-------------------------------------------
            } else if (condition_string.indexOf("04_3__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //-------------------------------------------
            } else if (condition_string.indexOf("04_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, true, false);
            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("ld03") > -1) {
            //高级（三级）
            //         ld03 = ['（1）取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作５年（含）以上。 ',
            // '（2__1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（2__2）或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
            // '（3）具有大学专科本专业或相关专业毕业证书，并取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书） 后，累计从事本职业或相关职业工作２年（含）以上。',
            // '（4）具有大学本科本专业或相关专业学历证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作 1 年（含）以上。 ',
            // '（5）具有硕士研究生及以上本专业或相关专业学历证书（含尚未取得毕业证书的在校应届研究生毕业生）。', '注：\n' +
            // '1、相关职业：人力资源管理、劳动保障事务处理、社会工作等职业。 \n' +
            // '2、相关专业：劳动与社会保障、劳动经济学、人力资源管理、工商企业管理、法学、社会学等专业。 \n' +
            // '3、相关职业资格证书（技能等级证书）:企业人力资源管理师、劳动保障协理员、劳动保障专理员、社会工作者等与劳动关系协调员职业功能具有关联性的职业资格证书。'];
            if (condition_string.indexOf("03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);
            } else if (condition_string.indexOf("03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false, 4); //===================================
            } else if (condition_string.indexOf("03_3__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false); //====================================================
            } else if (condition_string.indexOf("03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 7, false, true);
            } else if (condition_string.indexOf("03_5") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 1); //==========================================
                check_graduation_status(1, 7, false, true);
            } else if (condition_string.indexOf("03_6") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2); //==========================================
                check_graduation_status(1, 8, true, false);
            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
        //    后加 2019 07 29 ----
    } else {
        new_add_worker(condition_string);
        // alert(condition_string);
    }
}

function clear_input_label() {
    $("#apprentice_start").val("");
    $("#apprentice_end").val("");
    $("#apprentice_year").val("");
    $("#start_the_work_of_this_occupation").val("");
    $("#career_life").val("");
    $("#career_life_time").val("");
    $("#original_certificate_number").val("");
    $("#issue_unit").val("");
    $("#issuance_time").val("");
    $("#original_certificate_worker_year").val("");
    $("#from_certificate_need_year").val("");
    $("#school_name").val("");
    $("#major").val("");
    $("#course_hours").val("");
    $("#graduation_time").val("");
    $("#certificate_photos").val("");
    $("#diploma_certificate_photos").val("");

    $("#career_life_label_value").text("");
    $("#apprentice_year_label").text("");
    $("#apprentice_month_label").text("");
    $("#original_certificate_worker_year_value").text("");
    $("#career_life_label").text("");
    $("#original_certificate_worker_year_label").text("");
}
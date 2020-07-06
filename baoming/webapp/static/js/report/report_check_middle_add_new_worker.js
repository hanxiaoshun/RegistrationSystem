/**
 * 新增的工种类型中间件
 * @param condition_string
 */
function new_add_worker(condition_string) {
    if (condition_string.indexOf('cg') > -1) {
        // 车工
        if (condition_string.indexOf("cg05") > -1) {
            //五级（初级）
            //         cg05 = ['(1) 累计从事本职业工作１年( 含)以上。',
            // '(2) 本职业学徒期满。'];
            if (condition_string.indexOf("cg05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("cg05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("cg04") > -1) {

            //四级（中级）
            //        cg04 = ['(1) 取得本职业五级/ 初级工职业资格证书( 技能等级证书)后，累计从事本职业工作４年(含)以上。',
            // '(2) 累计从事本职业工作６年(含)以上。',
            // '(3__1) 取得技工学校本专业或相关专业毕业证书( 含尚未取得毕业证书的在校应届毕业生)；',
            // '(3__2) 或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。'];
            if (condition_string.indexOf("cg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("cg04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("cg04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("cg04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("cg03") > -1) {
            //高级（三级）

            //         cg03 = ['(1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作５ 年( 含) 以上。',
            // '(2__1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；',
            // '(2__2)或取得本职业四级/ 中级工职业资格证书，并具有经评估论证、 以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 (含尚未取得毕业证书的在校应届毕业生)。 ',
            // '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业四级/ 中级工职业资格证书  ( 技能等级证书) 后，累计从事本职业工作２年( 含) 以上。'];
            career_life_time();
            apprentice_check(false);
            check_has_qualification(1, 4, 5);
            check_graduation_status(2);

        } else if (condition_string.indexOf("cg03_2__1") > -1) {

            career_life_time();
            apprentice_check(false);
            check_has_qualification(1, 4);
            check_graduation_status(1, 4, false, false);

        } else if (condition_string.indexOf("cg03_3__2") > -1) {
            career_life_time();
            apprentice_check(false);
            check_has_qualification(1, 4);
            check_graduation_status(1, 5, false, false);

        } else if (condition_string.indexOf("cg03_4") > -1) {

            career_life_time();
            apprentice_check(false);
            check_has_qualification(1, 4, 2);
            check_graduation_status(1, 6, true, true);

        } else {
            alert("没有相关的信息填报条件！，请查证后重新选择。");
        }
    } else if (condition_string.indexOf('jcztwxg') > -1) {
        // 机床装调维修工
        if (condition_string.indexOf("jcztwxg04") > -1) {

            //四级（中级）
            //        jcztwxg04 = ['(1) 取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
            // '(2) 累计从事本职业或相关职业工作6年（含）以上。',
            // '(3__1) 取得技工学校本专业或相关专业毕业证书(含尚未取得毕业证书的在校应届毕业生)；',
            // '(3__2) 取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。'];
            if (condition_string.indexOf("jcztwxg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("jcztwxg04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("jcztwxg04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("jcztwxg04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("jcztwxg03") > -1) {
            //高级（三级）

            //         jcztwxg03 = ['(1) 取得本职业或相关职业四级/ 中级工职业资格证书(技能等级证书)后，累计从事本职业或相关职业工作５年(含)以上。',
            // '(2__1) 取得本职业或相关职业四级/ 中级工职业资格证书 ( 技能等级证书) ，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；',
            // '(2__2)或取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。',
            // '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业或相关职业工作２年( 含) 以上。'];
            if (condition_string.indexOf("jcztwxg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("jcztwxg03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 4, false, false);

            } else if (condition_string.indexOf("jcztwxg03_3__2") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("jcztwxg03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('dtanwxg') > -1) {
        // 电梯安装维修工
        if (condition_string.indexOf("dtanwxg05") > -1) {
            //五级（初级）
            //         let cg05 = ['(1) 累计从事本职业工作１年( 含)以上。',
            // '(2) 本职业学徒期满。'];
            if (condition_string.indexOf("dtanwxg05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dtanwxg05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("dtanwxg04") > -1) {

            //四级（中级）
            //         hg04 = ['（1）取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
            // '（2）累计从事本职业或相关职业工作6年（含）以上。',
            // '（3__1）取得技工学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（3__2）或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。'
            if (condition_string.indexOf("dtanwxg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dtanwxg04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dtanwxg04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("dtanwxg04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("dtanwxg03") > -1) {
            //高级（三级）

            //         hg03 = ['（1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作5年（含）以上。',
            // '（2__1）取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有高级技工学校、技师学院毕业证书（含尚未取得毕业证书的在校应届毕业生）；',
            // '（2__2）或取得本职业或相关职业四级/中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书（含尚未取得毕业证书的在校应届毕业生）。',
            // '（3）具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/中级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作2年（含）以上。',
            if (condition_string.indexOf("dtanwxg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("dtanwxg03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false, 4);

            } else if (condition_string.indexOf("dtanwxg03_3__2") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("dtanwxg03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('qzzxjxczg') > -1) {
        // 起重装卸机械操作工
        if (condition_string.indexOf("qzzxjxczg05") > -1) {
            //五级（初级）
            //         qzzxjxczg05 = ['(1) 累计从事本职业或相关职业工作１年( 含)以上。',
            // '(2) 本职业或相关职业学徒期满。'];
            if (condition_string.indexOf("qzzxjxczg05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("qzzxjxczg05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("qzzxjxczg04") > -1) {

            //四级（中级）
            //          qzzxjxczg04 = ['(1) 取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
            // '(2) 累计从事本职业或相关职业工作6年（含）以上。',
            // '(3__1) 取得技工学校本专业或相关专业毕业证书(含尚未取得毕业证书的在校应届毕业生)；',
            // '(3__2)或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。'];
            if (condition_string.indexOf("qzzxjxczg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("qzzxjxczg04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("qzzxjxczg04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("qzzxjxczg04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("qzzxjxczg03") > -1) {
            //高级（三级）
            // qzzxjxczg03 = ['(1) 取得本职业或相关职业四级/ 中级工职业资格证书(技能等级证书)后，累计从事本职业或相关职业工作５年(含)以上。',
            //     '(2__1) 取得本职业或相关职业四级/ 中级工职业资格证书 ( 技能等级证书) ，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；',
            //     '(2__2)或取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。 ',
            //     '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业或相关职业工作２年( 含) 以上。', '注：电梯安装维修工 1、相关职业：电梯装配调试工、特种设备检验检测工程技术人员（电梯）。2、本专业：电梯工程技术专业。\n' +
            //     '3、相关专业: 理工科专业。起重装卸机械操作工 本专业或相关专业: 机械、电气类专业 。'];
            if (condition_string.indexOf("qzzxjxczg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("qzzxjxczg03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 4, false, false);

            } else if (condition_string.indexOf("qzzxjxczg03_3__2") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("qzzxjxczg03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('jzg') > -1) {
        // 架子工
        if (condition_string.indexOf("jzg05") > -1) {
            //五级（初级）
            //         jzg05 = ['（1）经本职业初级正规培训达规定标准学时数 , 并取得毕 ( 结)业证书。',
            // '(2) 在本职业连续见习工作 2 年以上。',
            // '(3) 本职业学徒期满。'];
            if (condition_string.indexOf("jzg05_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 9, false, true);

            } else if (condition_string.indexOf("jzg05_2") > -1) {

                career_life_time(2);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("jzg05_3") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("jzg04") > -1) {

            //四级（中级）
            //         jzg04 = ['(1) 取得本职业初级职业资格证书后 , 连续从事本职业工作 3 年以上 , 经本职业中级正规培训达规定标准学时数 ,并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业初级职业资格证书后 , 连续从事本职业工作 5 年以上。',
            // '(3) 连续从事本职业工作7年以上。',
            // '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。'];
            if (condition_string.indexOf("jzg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 3);
                check_graduation_status(1, 10, false, true);

            } else if (condition_string.indexOf("jzg04_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("jzg04_3") > -1) {

                career_life_time(7);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2); //==============================

            } else if (condition_string.indexOf("jzg04_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("jzg03") > -1) {
            //高级（三级）

            //         jzg03 = ['(1) 取得本职业中级职业资格证书后 , 连续从事本职业工作 4 年以上 ,经本职业高级正规培训达规定标准学时数 , 并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业中级职业资格证书后 , 连续从事本职业工作6年以上。',
            // '(3__1) 取得高级技工学校审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
            // '(3__2)或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
            // '(4) 取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生 , 连续从事本职业工作2年以上。'];
            if (condition_string.indexOf("jzg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 4);
                check_graduation_status(1, 11, false, true);

            } else if (condition_string.indexOf("jzg03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 6);
                check_graduation_status(2);

            } else if (condition_string.indexOf("jzg03_3__1") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("jzg03_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, true, true);

            } else if (condition_string.indexOf("jzg03_5") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, false);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('fsg') > -1) {
        // 防水工
        if (condition_string.indexOf("fsg05") > -1) {
            //五级（初级）
            //         fsg05 = ['（1）经本职业初级正规培训达规定标准学时数 , 并取得毕 ( 结)业证书。',
            // '(2) 在本职业连续见习工作 2 年以上。',
            // '(3) 本职业学徒期满。'];
            if (condition_string.indexOf("fsg05_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 9, false, true);

            } else if (condition_string.indexOf("fsg05_2") > -1) {

                career_life_time(2);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("fsg05_3") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("fsg04") > -1) {

            //四级（中级）
            //         fsg04 = ['(1) 取得本职业初级职业资格证书后 , 连续从事本职业工作 3 年以上 , 经本职业中级正规培训达规定标准学时数 ,并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业初级职业资格证书后 , 连续从事本职业工作 5 年以上。',
            // '(3) 连续从事本职业工作7年以上。',
            // '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。'];
            if (condition_string.indexOf("fsg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 3);
                check_graduation_status(1, 10, false, true);

            } else if (condition_string.indexOf("fsg04_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("fsg04_3") > -1) {

                career_life_time(7);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2); //==============================

            } else if (condition_string.indexOf("fsg04_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("fsg03") > -1) {
            //高级（三级）

            //         fsg03 = ['(1) 取得本职业中级职业资格证书后 , 连续从事本职业工作 4 年以上 ,经本职业高级正规培训达规定标准学时数 , 并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业中级职业资格证书后 , 连续从事本职业工作6年以上。',
            // '(3__1) 取得高级技工学校审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
            // '(3__2)或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
            // '(4) 取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生 , 连续从事本职业工作2年以上。'];
            if (condition_string.indexOf("fsg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 4);
                check_graduation_status(1, 11, false, true);

            } else if (condition_string.indexOf("fsg03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 6);
                check_graduation_status(2);

            } else if (condition_string.indexOf("fsg03_3__1") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("fsg03_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, true, true);

            } else if (condition_string.indexOf("fsg03_5") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, false);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('sgmg') > -1) {
        // 手工木工
        if (condition_string.indexOf("sgmg05") > -1) {
            //五级（初级）
            //         sgmg05 = ['（1）经本职业初级正规培训达规定标准学时数 , 并取得毕 ( 结)业证书。',
            // '(2) 在本职业连续见习工作 2 年以上。',
            // '(3) 本职业学徒期满。'];
            if (condition_string.indexOf("sgmg05_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 9, false, true);

            } else if (condition_string.indexOf("sgmg05_2") > -1) {

                career_life_time(2);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("sgmg05_3") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("sgmg04") > -1) {

            //四级（中级）
            //         sgmg04 = ['(1) 取得本职业初级职业资格证书后 , 连续从事本职业工作 3 年以上 , 经本职业中级正规培训达规定标准学时数 ,并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业初级职业资格证书后 , 连续从事本职业工作 5 年以上。',
            // '(3) 连续从事本职业工作7年以上。',
            // '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。'];
            if (condition_string.indexOf("sgmg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 3);
                check_graduation_status(1, 10, false, true);

            } else if (condition_string.indexOf("sgmg04_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("sgmg04_3") > -1) {

                career_life_time(7);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2); //==============================

            } else if (condition_string.indexOf("sgmg04_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("sgmg03") > -1) {
            //高级（三级）

            //         sgmg03 = ['(1) 取得本职业中级职业资格证书后 , 连续从事本职业工作 4 年以上 ,经本职业高级正规培训达规定标准学时数 , 并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业中级职业资格证书后 , 连续从事本职业工作6年以上。',
            // '(3__1) 取得高级技工学校审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
            // '(3__2)或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
            // '(4) 取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生 , 连续从事本职业工作2年以上。'];
            if (condition_string.indexOf("sgmg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 4);
                check_graduation_status(1, 11, false, true);

            } else if (condition_string.indexOf("sgmg03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 6);
                check_graduation_status(2);

            } else if (condition_string.indexOf("sgmg03_3__1") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("sgmg03_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, true, true);

            } else if (condition_string.indexOf("sgmg03_5") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, false);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
        // -----------------------------------------------------------------------------------------------
    } else if (condition_string.indexOf('qzg') > -1) {
        // 砌筑工
        if (condition_string.indexOf("qzg05") > -1) {
            //五级（初级）
            //         qzg05 = ['（1）经本职业初级正规培训达规定标准学时数 , 并取得毕 ( 结)业证书。',
            // '(2) 在本职业连续见习工作 2 年以上。'];
            if (condition_string.indexOf("qzg05_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 9, false, true);

            } else if (condition_string.indexOf("qzg05_2") > -1) {

                career_life_time(2);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("qzg04") > -1) {

            //四级（中级）
            //        qzg04 = ['(1) 取得本职业初级职业资格证书后 , 连续从事本职业工作 3 年以上 , 经本职业中级正规培训达规定标准学时数 ,并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业初级职业资格证书后 , 连续从事本职业工作 5 年以上。',
            // '(3) 连续从事本职业工作8年以上。',
            // '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。'];
            if (condition_string.indexOf("qzg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 3);
                check_graduation_status(1, 10, false, true);

            } else if (condition_string.indexOf("qzg04_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("qzg04_3") > -1) {

                career_life_time(8);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2); //==============================

            } else if (condition_string.indexOf("qzg04_4") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, true); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("qzg03") > -1) {
            //高级（三级）

            //        qzg03 = ['(1) 取得本职业中级职业资格证书后 , 连续从事本职业工作 4 年以上 , 经本职业高级正规培训达规定标准学时数 , 并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业中级职业资格证书后 , 连续从事本职业工作6年以上。',
            // '(3__1) 取得高级技工学校本职业 ( 专业 ) 毕业证书。',
            // '(3__2)或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
            // '(4) 取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生，连续从事本职业工作2年以上。'];
            if (condition_string.indexOf("qzg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 4);
                check_graduation_status(1, 11, false, true);

            } else if (condition_string.indexOf("qzg03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 6);
                check_graduation_status(2);

            } else if (condition_string.indexOf("qzg03_3__1") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 4, false, true);

            } else if (condition_string.indexOf("qzg03_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, false, true);

            } else if (condition_string.indexOf("qzg03_5") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, false, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('gjg') > -1) {
        // 钢筋工
        if (condition_string.indexOf("gjg05") > -1) {
            //五级（初级）
            //        gjg05 = ['（1）经本职业初级正规培训达规定标准学时数 , 并取得毕 ( 结)业证书。',
            // '(2) 在本职业连续见习工作 2 年以上。'];
            if (condition_string.indexOf("gjg05_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 9, false, true);

            } else if (condition_string.indexOf("gjg05_2") > -1) {

                career_life_time(2);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("gjg04") > -1) {

            //四级（中级）
            //  gjg04 = ['(1) 取得本职业初级职业资格证书后 , 连续从事本职业工作 3 年以上 , 经本职业中级正规培训达规定标准学时数 ,并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业初级职业资格证书后 , 连续从事本职业工作 5 年以上。',
            // '(3) 连续从事本职业工作8年以上。',
            // '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。'];
            if (condition_string.indexOf("gjg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 3);
                check_graduation_status(1, 10, false, true);

            } else if (condition_string.indexOf("gjg04_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("gjg04_3") > -1) {

                career_life_time(8);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2); //==============================

            } else if (condition_string.indexOf("gjg04_4") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, true); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("gjg03") > -1) {
            //高级（三级）

            //         gjg03 = ['(1) 取得本职业中级职业资格证书后 , 连续从事本职业工作 4 年以上 , 经本职业高级正规培训达规定标准学时数 , 并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业中级职业资格证书后 , 连续从事本职业工作6年以上。',
            // '(3__1) 取得高级技工学校本职业 ( 专业 ) 毕业证书。',
            // '(3__2)或经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
            // '(4) 取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生，连续从事本职业工作2年以上。'];
            if (condition_string.indexOf("gjg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 4);
                check_graduation_status(1, 11, false, true);

            } else if (condition_string.indexOf("gjg03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 6);
                check_graduation_status(2);

            } else if (condition_string.indexOf("gjg03_3__1") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 4, false, false);

            } else if (condition_string.indexOf("gjg03_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, false, true);

            } else if (condition_string.indexOf("gjg03_5") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, false, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('hntg') > -1) {
        // 混凝土工
        if (condition_string.indexOf("hntg05") > -1) {
            //五级（初级）
            //         hntg05 = ['（1）经本职业初级正规培训达规定标准学时数 , 并取得毕 ( 结)业证书。',
            // '(2) 在本职业连续见习工作 2 年以上。'];
            if (condition_string.indexOf("hntg05_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 9);

            } else if (condition_string.indexOf("sgmg05_2") > -1) {

                career_life_time(2);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                console.log("获取失败！");
            }

        } else if (condition_string.indexOf("hntg04") > -1) {

            //四级（中级）
            //         hntg04 = ['(1) 取得本职业初级职业资格证书后 , 连续从事本职业工作3年以上 , 经本职业中级正规培训达规定标准学时数 , 并取得毕 ( 结 ) 业证书。',
            // '(2) 取得本职业初级职业资格证书后 , 连续从事本职业工作 5 年以上。',
            // '(3) 连续从事本职业工作 6 年以上。',
            // '(4) 取得经人力资源和社会保障行政部门审核认定的、以中级技能为培养目标的中等以上职业学校本职业 ( 专业 ) 毕业证书。'];
            if (condition_string.indexOf("hntg04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 3);
                check_graduation_status(1, 10, false, true);

            } else if (condition_string.indexOf("hntg04_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("hntg04_3") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2); //==============================

            } else if (condition_string.indexOf("hntg04_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("hntg03") > -1) {
            //高级（三级）
            // hntg03 = ['(1) 取得本职业中级职业资格证书后 , 连续从事本职业工作 4 年以上 , 经本职业高级正规培训达规定标准学时数 , 并取得毕 ( 结 ) 业证书。',
            //     '(2) 取得本职业中级职业资格证书后 , 连续从事本职业工作 6 年以上。',
            //     '(3) 取得经人力资源和社会保障行政部门审核认定的、以高级技能为培养目标的高等职业学校本职业 ( 专业 ) 毕业证书。',
            //     '(4)取得本职业中级职业资格证书的大专以上本专业或相关专业毕业生，连续从事本职业工作2年以上。'];
            if (condition_string.indexOf("hntg03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(1, 11, false, true);

            } else if (condition_string.indexOf("hntg03_2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 6);
                check_graduation_status(2);

            } else if (condition_string.indexOf("hntg03_3") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 5, false, true);

            } else if (condition_string.indexOf("hntg03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('znlugly') > -1) {
        if (condition_string.indexOf("znlugly04") > -1) {

            //         znlugly04 = ['(1) 累计从事本职业或相关职业工作6年（含）以上。',
            // '(2-1) 取得技工学校本专业或相关专业毕业证书(含尚未取得毕业证书的在校应届毕业生)；',
            // '(2-1)取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。'];
            if (condition_string.indexOf("znlugly04_1") > -1) {
                //第1个条件

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("znlugly04_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, true);

            } else if (condition_string.indexOf("znlugly04_3__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, false, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("znlugly03") > -1) {
            //高级（三级）
            //             znlugly03 = ['(1) 取得本职业或相关职业四级/ 中级工职业资格证书(技能等级证书)后，累计从事本职业或相关职业工作５年(含)以上。',
            //     '(2-1) 取得本职业或相关职业四级/ 中级工职业资格证书 ( 技能等级证书) ，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。',
            //     '(2-2)取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。 ',
            //     '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级/ 中级工职业资格证书 ( 技能等级证书) 后，累计从事本职业或相关职业工作２年( 含) 以上。'
            // ];
            if (condition_string.indexOf("znlugly03_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("znlugly03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 2, false, false);

            } else if (condition_string.indexOf("znlugly03_3__2") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("znlugly03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else {
        new_add_worker_plus(condition_string)
    }
}

/**
 * 2019-08-13
 * 新增的工种类型中间件
 * @param condition_string
 */
function new_add_worker_plus(condition_string) {
    if (condition_string.indexOf('zsmds') > -1) {
        // 中式面点师
        if (condition_string.indexOf("zsmds05") > -1) {
            // zsmds05 = ['(1) 累计从事本职业或相关职业工作１年( 含)以上。',
            // '(2) 本职业或相关职业学徒期满'];
            if (condition_string.indexOf("zsmds05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("zsmds05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }

        } else if (condition_string.indexOf("zsmds04") > -1) {

            //     zsmds04 = ['(1) 取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
            // '(2) 累计从事本职业或相关职业工作6年（含）以上。',
            // '(3__1) 取得技工学校本专业或相关专业毕业证书(含尚未取得毕业证书的在校应届毕业生)；',
            // '(3__2) 或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。'];
            if (condition_string.indexOf("zsmds04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("zsmds04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("zsmds04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("zsmds04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("zsmds03") > -1) {
            //高级（三级）

            //         zsmds03 = ['(1) 取得本职业或相关职业四级/ 中级工职业资格证书(技能等级证书)后，累计从事本职业或相关职业工作５年(含)以上。',
            // '(2__1) 取得本职业或相关职业四级/ 中级工职业资格证书 ( 技能等级证书) ，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；',
            // '(2__2) 或取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。 ',
            // '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级 / 中级工职业资格证书(技能等级证书)后，累计从事本职业或相关职业工作２年(含)以上。',
            // '注：中式面点师' +
            // '1、相关职业：中式烹调师、西式烹调师、西式面点师、糕点面包烘焙工、米面主食制作工。' +
            // '2、相关专业: 中餐烹饪、西餐烹饪、中西面点工艺、烹调工艺与营养（烹饪工艺与营养）、烹饪与营养教育。' +
            // '中式烹调师' +
            // '1、相关职业：中式面点师、西式烹调师、西式面点师。' +
            // '2、相关专业: 中餐烹饪、西餐烹饪、烹调工艺与营养（烹饪工艺与营养）、烹饪与营养教育。'];
            if (condition_string.indexOf("zsmds03_1") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("zsmds03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 4, false, false);

            } else if (condition_string.indexOf("zsmds03_3__2") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("zsmds03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('zspts') > -1) {
        // 中式烹调师
        if (condition_string.indexOf("zspts05") > -1) {
            // zsmds05 = ['(1) 累计从事本职业或相关职业工作１年( 含)以上。',
            // '(2) 本职业或相关职业学徒期满'];
            if (condition_string.indexOf("zspts05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("zspts05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }

        } else if (condition_string.indexOf("zspts04") > -1) {

            //     zsmds04 = ['(1) 取得本职业或相关职业五级/初级工职业资格证书（技能等级证书）后，累计从事本职业或相关职业工作4年（含）以上。',
            // '(2) 累计从事本职业或相关职业工作6年（含）以上。',
            // '(3__1) 取得技工学校本专业或相关专业毕业证书(含尚未取得毕业证书的在校应届毕业生)；',
            // '(3__2) 或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。'];
            if (condition_string.indexOf("zspts04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("zspts04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("zspts04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("zspts04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("zspts03") > -1) {
            //高级（三级）

            //         zsmds03 = ['(1) 取得本职业或相关职业四级/ 中级工职业资格证书(技能等级证书)后，累计从事本职业或相关职业工作５年(含)以上。',
            // '(2__1) 取得本职业或相关职业四级/ 中级工职业资格证书 ( 技能等级证书) ，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；',
            // '(2__2) 或取得本职业或相关职业四级/ 中级工职业资格证书（技能等级证书），并具有经评估论证、以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。 ',
            // '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业或相关职业四级 / 中级工职业资格证书(技能等级证书)后，累计从事本职业或相关职业工作２年(含)以上。',
            // '注：中式面点师' +
            // '1、相关职业：中式烹调师、西式烹调师、西式面点师、糕点面包烘焙工、米面主食制作工。' +
            // '2、相关专业: 中餐烹饪、西餐烹饪、中西面点工艺、烹调工艺与营养（烹饪工艺与营养）、烹饪与营养教育。' +
            // '中式烹调师' +
            // '1、相关职业：中式面点师、西式烹调师、西式面点师。' +
            // '2、相关专业: 中餐烹饪、西餐烹饪、烹调工艺与营养（烹饪工艺与营养）、烹饪与营养教育。'];
            if (condition_string.indexOf("zspts03_1") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("zspts03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 4, false, false);

            } else if (condition_string.indexOf("zspts03_3__2") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("zspts03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        }
    } else if (condition_string.indexOf('mrs') > -1) {
        // 美容师
        if (condition_string.indexOf("mrs05") > -1) {
            // zsmds05 = ['(1) 累计从事本职业或相关职业工作１年( 含)以上。',
            // '(2) 本职业或相关职业学徒期满'];
            if (condition_string.indexOf("mrs05_1") > -1) {
                //第1个条件

                career_life_time(1);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("mrs05_2") > -1) {

                career_life_time();
                apprentice_check(true);
                check_has_qualification(2);
                check_graduation_status(2);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }

        } else if (condition_string.indexOf("mrs04") > -1) {
            // mrs04 = ['(1) 取得本职业五级/ 初级工职业资格证书( 技能等级证书)后，累计从事本职业工作４年(含)以上。',
            //     '(2) 累计从事本职业工作６年(含)以上。',
            //     '(3__1) 取得技工学校本专业或相关专业毕业证书( 含尚未取得毕业证书的在校应届毕业生)；',
            //     '(3__2) 或取得经评估论证、以中级技能为培养目标的中等及以上职业学校本专业或相关专业毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)。'];
            if (condition_string.indexOf("mrs04_1") > -1) {
                //第1个条件

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 5, 4);
                check_graduation_status(2);

            } else if (condition_string.indexOf("mrs04_2") > -1) {

                career_life_time(6);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(2);

            } else if (condition_string.indexOf("mrs04_3__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 2, false, false); //==============================

            } else if (condition_string.indexOf("mrs04_4__2") > -1) {

                career_life_time();
                apprentice_check(false);
                apprentice_check(false);
                check_has_qualification(2);
                check_graduation_status(1, 3, true, false); //==============================

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else if (condition_string.indexOf("mrs03") > -1) {
            //高级（三级）
            // mrs03 = ['(1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)后，累计从事本职业工作５ 年( 含) 以上。',
            // '(2__1) 取得本职业四级/ 中级工职业资格证书 ( 技能等级证书)，并具有高级技工学校、 技师学院毕业证书 ( 含尚未取得毕业证书的在校应届毕业生)；',
            // '(2__2) 或取得本职业四级/ 中级工职业资格证书，并具有经评估论证、 以高级技能为培养目标的高等职业学校本专业或相关专业毕业证书 (含尚未取得毕业证书的在校应届毕业生)。',
            // '(3) 具有大专及以上本专业或相关专业毕业证书，并取得本职业四级/ 中级工职业资格证书  ( 技能等级证书) 后，累计从事本职业工作２年( 含) 以上。',
            // '注：本专业和相关专业: 美容美体、服装与化妆造型、舞美、美容护理、美容养生、医疗美容、人物形象设计、美容美发形象设计等。'];
            if (condition_string.indexOf("mrs03_1") > -1) {
                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 5);
                check_graduation_status(2);

            } else if (condition_string.indexOf("mrs03_2__1") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 4, false, false);

            } else if (condition_string.indexOf("mrs03_3__2") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4);
                check_graduation_status(1, 5, false, false);

            } else if (condition_string.indexOf("mrs03_4") > -1) {

                career_life_time();
                apprentice_check(false);
                check_has_qualification(1, 4, 2);
                check_graduation_status(1, 6, true, true);

            } else {
                alert("没有相关的信息填报条件！，请查证后重新选择。");
            }
        } else {
            alert("没有相关的报考信息！，请查证后重新选择。");
        }
    }
}
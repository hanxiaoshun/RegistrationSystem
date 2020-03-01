/**
 * 适配新增的工种类型
 * @param worker
 * @param obj
 */
function report_add_new(worker, obj) {
    if (worker === "车工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "cg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "cg04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "cg05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "机床装调维修工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "jcztwxg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "jcztwxg04";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "电梯安装维修工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "dtanwxg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "dtanwxg04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "dtanwxg05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "起重装卸机械操作工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "qzzxjxczg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "qzzxjxczg04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "qzzxjxczg05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "架子工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "jzg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "jzg04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "jzg05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "防水工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "fsg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "fsg04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "fsg05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "手工木工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "sgmg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "sgmg04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "sgmg05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "砌筑工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "qzg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "qzg04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "qzg05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "钢筋工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "gjg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "gjg04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "gjg05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "混凝土工") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "hntg03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "hntg04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "hntg05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else if (worker === "智能楼宇管理员") {
        if (parseInt(obj) === 3) {
            // // 高级工
            let work_level_tag = "znlugly03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "znlugly04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            // let work_level_tag = "znlugly05";
            // put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else {
        report_add_new_plus(worker, obj);
    }
}


/**
 * 适配新增的工种类型
 * @param worker
 * @param obj
 */
function report_add_new_plus(worker, obj) {
    if (worker === "中式面点师") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "zsmds03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "zsmds04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "zsmds05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    }else if (worker === "中式烹调师") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "zspts03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "zspts04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "zspts05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    }else if (worker === "美容师") {
        if (parseInt(obj) === 3) {
            // 高级工
            let work_level_tag = "mrs03";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 4) {
            // 中级工
            let work_level_tag = "mrs04";
            put_select(work_level_tag, parseInt(obj));

        } else if (parseInt(obj) === 5) {
            // 初级工
            let work_level_tag = "mrs05";
            put_select(work_level_tag, parseInt(obj));

        } else {
            put_select('null', 0);
        }
    } else {
        let worker_level = $(".worker_level_desc");
        let worker_level_content = $(".worker_level_desc_content");
        worker_level.hide();
        worker_level_content.hide();
    }
}
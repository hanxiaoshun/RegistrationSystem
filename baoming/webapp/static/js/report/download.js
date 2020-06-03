/**
 * 化工类
 */
function reporter_chemical_search() {
    //关闭弹窗
    let formElement = document.querySelector('#form-search-chemical');
    formElement.setAttribute('action', '/report/administrator_search_chemical_download/');
    $('#submit-reporter-chemical-search').click();
    formElement.setAttribute('action', '/report/administrator_search_chemical/');
}

/**
 * 非化工类
 */
function reporter_chemical_not_search() {
    //关闭弹窗
    let formElement = document.querySelector('#form-search-chemical-not');
    formElement.setAttribute('action', '/report/administrator_search_chemical_not_download/');
    $('#submit-reporter-chemical-not-search').click();
    formElement.setAttribute('action', '/report/administrator_search_chemical_not/');
}

/**
 * 非化工类
 */
function reporter_electronic_communication() {
    //关闭弹窗
    let formElement = document.querySelector('#form-search-electronic-communication');
    formElement.setAttribute('action', '/report/electronic_communication_download/');
    $('#submit-reporter-electronic-search').click();
    formElement.setAttribute('action', '/report/administrator_reporter_electronic_communication/');
}


/**
 * 非化工类
 */
function reporter_spin() {
    //关闭弹窗
    let formElement = document.querySelector('#form-search-spin');
    formElement.setAttribute('action', '/report/spin_download/');
    $('#submit-reporter-spin-search').click();
    formElement.setAttribute('action', '/report/administrator_reporter_spin/');
}


function reporter_all_student_search() {
    //关闭弹窗
    let formElement = document.querySelector('#form-search-all-student');
    formElement.setAttribute('action', '/report/all_student_base_info_download/');
    $('#submit-reporter-all-student-search').click();
    formElement.setAttribute('action', '/report/all_student_base_info/');
}

function reporter_worker_years_6() {
    //关闭弹窗
    let formElement = document.querySelector('#form-search-worker-years-6');
    formElement.setAttribute('action', '/report/worker_years_6_download/');
    $('#submit-reporter-worker-years-6').click();
    formElement.setAttribute('action', '/report/administrator_worker_years_6/');
}
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


function reporter_all_student_search() {
    //关闭弹窗
    let formElement = document.querySelector('#form-search-all-student');
    formElement.setAttribute('action', '/report/all_student_base_info_download/');
    $('#submit-reporter-all-student-search').click();
    formElement.setAttribute('action', '/report/all_student_base_info/');
}



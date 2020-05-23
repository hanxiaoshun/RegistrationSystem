function getPageResizeWithSearch(size, pagesize_input_id, search_id) {
	console.log(size, pagesize_input_id, search_id)
	$("#" + pagesize_input_id).val(size);
	$("#" + search_id).click();
}

function gotoPageWithSearch(page, page_input_id, search_id) {
	console.log(page, page_input_id, search_id)
	$("#" + page_input_id).val(page);
	$("#" + search_id).click();
}

function gotoWithSearchToPage(page_number_input_id, page_input_id, search_id){
	console.log(page_number_input_id, page_input_id, search_id)
	$("#" + page_input_id).val($("#" + page_number_input_id).val());
	$("#" + search_id).click();
}

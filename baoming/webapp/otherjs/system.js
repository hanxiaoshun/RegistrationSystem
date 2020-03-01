$(function($){
	
	listUser();
	
});

function listUser() {
	var listUserUrl = "http://localhost:8080/icpcheck-web/api/user/list";
	$.getJSON(listUserUrl, function(data) {
		console.log(data);
		/*for (var i=0; i<=data.length;i++;){
			console.log(data[i]);
		}*/
		for(i in data){
			var obj = data[i];
			console.log(obj.username);
			tr_line = "<tr><td>"+ obj.account  +"</td>" +
					"<td>"+ obj.username  +"</td>" +
					"<td>"+ obj.contact  +"</td>" +
					"<td>"+ obj.status  +"</td>" +
					"<td>"+ obj.role  +"</td>" +
					"<td>"+ obj.organization  +"</td>" +
					"<td><a href='void();'>查看</a>|<a>编辑</a>|<a>注销</a></td>" +
					"</tr>";
			$("#pure_table_one").append(tr_line);
		}
	});
}
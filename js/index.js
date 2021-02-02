$("#link_button").on("click", function(){
	var link_url=$("#link_url").val();
	$.ajax({
		type: 'POST',
		//dataType: 'json', // what to expect back from the PHP script
		url: 'cgi-bin/example.py', // point to server-side PHP script 
		data: {
			"link_url": link_url
		},
		success: function (response) {
			alert("working"+response);
		},
		error: function (response) {
			alert("error wih python"+response);
		}
	});
	
})
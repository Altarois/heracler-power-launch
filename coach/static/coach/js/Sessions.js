$(document).ready(function(){

	document.getElementsByClassName('.area').value = $('.area').data('id');


	var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
	//$("#alert-container").hide();
		//console.log(csrfToken);

	$(".triger").click(function() {
		var serializedData = $("#ExerciseForm").serialize();
		var data = $("input[name=name]").val();
		var data1 = $("input[name=timing]").val();
		var data2 = $("input[name=estimation]").val();
		var data3 = $("textarea[name=detail]").val();
		var data4 = $(this).data('id');
		console.log("hey hey sesssssssion!");
		console.log(data);
		console.log(data3);
		$.ajax({ 
				   url: $(this).data('url'),
				   data :{name : data, timing : data1 , estimation:data2 , detail: data3, id:data4,
				    csrfmiddlewaretoken: csrfToken},
				   type: 'post',
				  
				   success: function(response) {

				   	console.log("success on air")
				   	$('#bdg').removeClass('badge badge-warning').addClass('badge badge-primary');
				   	$('#bdg').html('Assigned Now')

				   		 
				   }
			   })
		
	});

 
});
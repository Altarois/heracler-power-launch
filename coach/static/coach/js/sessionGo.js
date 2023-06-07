$(document).ready(function(){

	var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
	//$("#alert-container").hide();
		//console.log(csrfToken);

	$(".submit").click(function() {
		
		var dataID =$(this).data('id');
		console.log("hey hey session ID!",dataID);
		$.ajax({ 
				   url: $(this).data('url'),
				   data :{ csrfmiddlewaretoken : csrfToken , id :dataID , action: 'identification'},
				   type: 'post',
				  
				   success: function(response) {
				      window.location.replace('addsession'); 
				   }
			   })
		
	});

 
});
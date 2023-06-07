$(document).ready(function(){

	var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
	//$("#alert-container").hide();
		//console.log(csrfToken);

	$("#btn-submit").click(function() {
		var serializedData = $("#ClientForm").serialize();
		console.log("hey hey clients!");
		$.ajax({ 
				   url: $("ClientForm").data('url'),
				   data :{serializedData,action: 'client'},
				   type: 'post',
				  
				   success: function(response) {
				   		console.log(response.client.name);
						console.log($("#ClientList"))
						//var block ='<div class="heading-section animate-box"> <h2>Client </h2> </div> </div> <div class="col-md-12"> <div class="fh5co-blog animate-box"> <div class="inner-post"> <a href="#"><img class="img-responsive" src="images/user.jpg" alt=""><i class="fa fa-user fa-5x" style="margin: 20px;"></i></a> </div> <div class="desc" style="padding-bottom: 2rem;"> <span class="posted_by"></span> <span class="comment"></a></span> <h3>'+ response.client.name +'</h3> <h3>'+ response.client.email +'</h3>  <a href="addexercise.html" class="btn btn-success" style="margin-bottom: 1rem; margin-right: 2rem;">Add / Edit Exercises</a></div> <a href="client.html" class="btn btn-warning" style="margin-bottom: 1rem;">View</a> </div> '
				   		//var test = '<h2>'+ response.client.name +'</h2>'
						var test2 = document.createElement('div');
						test2.innerHTML = '<div class="list-group list-group-me"> <ul class="list-group list-group-horizontal"> <li class="list-group-item">'+ response.client.name +'</li>  <li class="list-group-item">'+ response.client.email +'</li> <li class="list-group-item"> Today </li> <li class="list-group-item list-group-item-warning">Inactive</li> <li class="list-group-item">025f55azg5</li>  <button type="button" class="btn btn-outline-info">Client Not Active</button> </ul> </div>'
						//var card = '<div class="card mt-2" id="taskCard" data-id="'+response.client.id+'"><div class="card-body" >'+ response.client.name +'<button type="button" class="close float-right" data-id="'+response.client.id+'" > <span aria-hidden="true">&times;</span></button></div></div>'
						//$(block).appendTo("#clientList")
						//$("#clientList").append(card).html();
						document.getElementById("clientList").appendChild(test2)
				   		//'<div class="col-md-12" id="clientList"><div class="col-md-12"><div class="heading-section animate-box"><h2>Client</h2></div></div> <div class="col-md-12"><div class="fh5co-blog animate-box"><div class="inner-post"><a href="#"><img class="img-responsive" src="images/user.jpg" alt=""><i class="fa fa-user fa-5x" style="margin: 20px;"></i></a></div><div class="desc" style="padding-bottom: 4rem;"><span class="posted_by"></span><span class="comment"></a></span><h3>Yoww</h3><a href="addexercise.html" class="btn btn-success" style="margin-bottom: 1rem; margin-right: 2rem;">Add / Edit Exercises</a><a href="client.html" class="btn btn-warning" style="margin-bottom: 1rem;">View</a></div> </div> </div>'
				   }
			   })
		$("#ClientForm")[0].reset()
	});

 
});
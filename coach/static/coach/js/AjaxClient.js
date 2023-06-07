$(document).ready(function(){

	var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
	
	
	$(function () {
  // Delegating to `document` just in case.
  $(document).on("hidden.bs.modal", "#assigned", function () {
  console.log("cleaning trash");
    $(this).find("span").html(""); // Just clear the contents.
    $(this).find("span").remove(); // Remove from DOM.
  });
});



	$("#alert-container").hide();
		//console.log(csrfToken);

	$("#btn-submit").click(function() {
		var serializedData = $("#ClientForm").serialize();
		var data1 = $("input[name=name]").val();
		var data2 = $("input[name=email]").val();
		console.log("hey hey clients!");
		$.ajax({ 
				   url: $("ClientForm").data('url'),
				   data : {
							csrfmiddlewaretoken: csrfToken,
							//serializedData,
							name : data1,
							email : data2,
							action: 'client'
						  },
				   type: 'post',
				  
				   success: function(response) {
				   		console.log(response.client.name);
						console.log($("#ClientList"))
						//var block ='<div class="heading-section animate-box"> <h2>Client </h2> </div> </div> <div class="col-md-12"> <div class="fh5co-blog animate-box"> <div class="inner-post"> <a href="#"><img class="img-responsive" src="images/user.jpg" alt=""><i class="fa fa-user fa-5x" style="margin: 20px;"></i></a> </div> <div class="desc" style="padding-bottom: 2rem;"> <span class="posted_by"></span> <span class="comment"></a></span> <h3>'+ response.client.name +'</h3> <h3>'+ response.client.email +'</h3>  <a href="addexercise.html" class="btn btn-success" style="margin-bottom: 1rem; margin-right: 2rem;">Add / Edit Exercises</a></div> <a href="client.html" class="btn btn-warning" style="margin-bottom: 1rem;">View</a> </div> '
				   		//var test = '<h2>'+ response.client.name +'</h2>'
						var test2 = document.createElement('div');
						test2.innerHTML = '<div class="list-group list-group-me"> <ul class="list-group list-group-horizontal"> <li class="list-group-item">'+ response.client.name +'</li>  <li class="list-group-item">'+ response.client.email +'</li> <li class="list-group-item"> Today </li> <li class="list-group-item list-group-item-warning">Inactif</li> <div class="btn-group"> <button type="button" class="btn btn-info" data-toggle="modal" data-target="#codeModal"> Voir</button> </div>  <button type="button" class="btn btn-outline-info">Client Inactif</button> </ul> </div>'
						//var card = '<div class="card mt-2" id="taskCard" data-id="'+response.client.id+'"><div class="card-body" >'+ response.client.name +'<button type="button" class="close float-right" data-id="'+response.client.id+'" > <span aria-hidden="true">&times;</span></button></div></div>'
						//$(block).appendTo("#clientList")
						//$("#clientList").append(card).html();
						document.getElementById("ulti").appendChild(test2)
				   		//'<div class="col-md-12" id="clientList"><div class="col-md-12"><div class="heading-section animate-box"><h2>Client</h2></div></div> <div class="col-md-12"><div class="fh5co-blog animate-box"><div class="inner-post"><a href="#"><img class="img-responsive" src="images/user.jpg" alt=""><i class="fa fa-user fa-5x" style="margin: 20px;"></i></a></div><div class="desc" style="padding-bottom: 4rem;"><span class="posted_by"></span><span class="comment"></a></span><h3>Yoww</h3><a href="addexercise.html" class="btn btn-success" style="margin-bottom: 1rem; margin-right: 2rem;">Add / Edit Exercises</a><a href="client.html" class="btn btn-warning" style="margin-bottom: 1rem;">View</a></div> </div> </div>'
				   }
			   })
		$("#ClientForm")[0].reset()
	});

	$(".AddSession").click(function(){


		var dataID = $(this).data('id');
		
		$.ajax({
		
			url: $(this).data('url'),
			data: {
			csrfmiddlewaretoken: csrfToken,
			id: dataID,
			action: 'session',
			//dataType:"json"
			},
			type : "post",

			success: function(response) {
				
				console.log("hey hey session over here");
				console.log(response)
				
				var obj = jQuery.parseJSON(response)
				//console.log(obj[1].fields.name)

				$('.assigned').find('span').remove()
				var Sarray = [];
				var Selector = $(".assigned");
				Selector.empty();
				var count = $(".assigned span")

				console.log(count.length)

			//used to limit the number of element on div on first click
			
			if(count.length < obj.length)	
			{
				for (i = 0 ; i < obj.length ; i++) {
					// console.log(obj[i].fields.name)
					 Sarray.push(obj[i].fields.name)
					 Selector.append('<a href="#"><span class="badge badge-success">'+ obj[i].fields.name +' x </span></a>')
					}

					console.log("yoow",Sarray.length)
			}
				
     }

		})

	});

	
	$(".showed").click(function(){
	
		console.log("showwwed")
		var dataID = $(this).data('id');
		console.log(dataID)

		$.ajax({

			url: $(this).data('url'),
			data : {
						csrfmiddlewaretoken: csrfToken,
						id: dataID,
						action: 'show',
				},
			type:"post",
			
			success: function(response){
			
			console.log(response.code);
			var bshow = $("#codeModal > .modal-body");
			var tshow = $("#codeModal > .modal-title");
			console.log(bshow);
			tshow.append('<h4> '+ response.code.name +' </h4>');
			bshow.append('<p> '+ response.code.token +' <p>');

			var test = document.createElement('div');
			test.innerHTML = '<p> '+ response.code.token +' </p>';
			console.log(document.getElementById('codeModal'));
			document.getElementById("tokenBody").appendChild(test)
			//document.getElementById('codeModal').getElementsByClassName('modal-title').append('<p>weeee</p>');

			}
		})

	});


	$(".activation").click(function(){
	
		var dataID = $(this).data('id');
		var clientID = $("#AddSession").data('id');

		$.ajax({
				url: $(this).data('url'),
				data : {
						csrfmiddlewaretoken: csrfToken,
						id: dataID,
						ClientID: clientID,
						action: 'active',
				},

				type : "post",

				success: function(response){
				
					console.log(response.session)

					/*if (response.status){

						//var obj = jQuery.parseJSON(response)
						console.log("legmi")
						console.log(response.session)
						var Selector = $("#assigned");
						Selector.append('<a href="#"><span class="badge badge-success"> New Session Added  x </span></a>')


					}

					else{
					console.log("pas de legmi")

					$("#alert-container").fadeIn().delay(3000).fadeOut();
					console.log("encore plus de legmi")
					}*/


				}

				
			})
	});
 
});
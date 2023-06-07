$(document).ready(function(){

	var csrfToken = $("input[name=csrfmiddlewaretoken]").val();

	$("#addExercise").click(function() {
		var serializedData = $("#TaskForm").serialize();
		var data2 = $("input[name=search]").val();
		console.log("hey hey!", data2);
		$.ajax({ 
				   url: $("TaskForm").data('url'),
				   data : {name: data2, 
							csrfmiddlewaretoken:csrfToken,
							action: 'search'},

				   type: 'post',
				   success: function(response) {
				   		$("#taskList").append('<div class="card mt-2 opens" id="taskCard" data-id="'+response.task.id+'"><div class="card-body" >'+ response.task.name +'<button type="button" class="close float-right" data-id="'+response.task.id+'" > <span aria-hidden="true">&times;</span></button></div></div>');
				   		
				   }
			   })
		$("#TaskForm")[0].reset()
	});

	$("#taskList").on('click', '.card', function(){

		var dataID = $(this).data('id');
		
		$.ajax({
			url: 'addsession/' + dataID + '/completed',
			data: {
				csrfmiddlewaretoken: csrfToken,
				id: dataID
			},
			type: 'post',
			success: function(){
				
				var cardItem = $('#taskCard[data-id=" ' + dataID + ' "] ');
				cardItem.css('text-decoration', 'line-througt').hide().slideDown();
				$("#taskList").append(cardItem);
			}
		});
		//The code for delete function start here 
	}).on('click', 'button.close', function(event){
		event.stopPropagation();

		var dataID = $(this).data('id');
		console.log(dataID)

		$.ajax({
			url: '' +dataID+ '/deleted',
			data: {
				csrfmiddlewaretoken: csrfToken,
				id: dataID
			},
			type: 'post',
			dataType: 'json',
			success: function(){
				console.log("fonctionne bien", dataID);
				cards = $('.opens').filter('[data-id="dataID"]');
				console.log(cards);
				$('.opens').filter('[data-id="'+dataID+'"]').remove();
				
			}
		})
	});


 	$("#Add").click(function(){
 		var dataName = $(this).data('name');
 		console.log("wesh alors")
 		console.log(dataName)
 		$.ajax({

 			url: $("ExeForm").data('url'),
				   data : {csrfmiddlewaretoken: csrfToken,
							name: dataName},
				   type: 'post',
				   success: function(response) {
				   		$("#taskList").append('<div class="card mt-2 opens" id="taskCard">'+ response.task.name +'<div class="card-body" ></div></div>');
 		}

 		})

 	});

	$(".submit").click(function() {
		//var serializedData = $("#TaskForm").serialize();
		var form = $(this).parents('form:first');
		console.log(form)
		var serializedData = form.serializeArray();
		serializedData.push({name: 'csrfmiddlewaretoken', value: csrfToken});
		serializedData.push({name: 'action', value: 'tasks'});
		var dataID = $(this).data('id');
		serializedData.push({name: 'id', value: dataID});
		console.log("hey hey!", serializedData);
		$.ajax({ 
				   url: $("ExerciseForm").data('url'),
				   data :serializedData,
							
				   type: 'post',
				   success: function(response) {
				   		$("#taskList").append('<div class="card mt-2 opens" id="taskCard" data-id="'+response.task.id+'"><div class="card-body" >'+ response.task.name +'<button type="button" class="close float-right" data-id="'+response.task.id+'" > <span aria-hidden="true">&times;</span></button></div></div>');
				   		
				   }
			   })
		$("#TaskForm")[0].reset()
	});



});
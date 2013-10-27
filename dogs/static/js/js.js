var adopted_dogs = $('#adopted_dogs');
if(adopted_dogs.length !== 0){
	adopted_dogs.carouFredSel({
		height: 200,

		auto : {
			timeoutDuration: 5000
		},
		swipe: {
			onTouch: true,
			onMouse: true
		}
	});

	var img = $('#adopted_dogs img');

	img.tooltip({placement: 'bottom'});

	img.each(function(){
		e = $(this);
		var url = e.attr('data-url');
		console.log(url);

		if(url){
			e.css({cursor: 'pointer'});
			e.click(function(){
				window.location = url;
			});
		}
	});
}

var mnhSelect = $('header select');
if(mnhSelect.length !== 0){
	mnhSelect.change(function(){
		var e = $(this);
		var maps = {home: '/', search: '/dogs/search/', testimonials: '/', login: '/accounts/login/'};
		window.location = maps[e.val()];
	});
}

var adoptionButton = $('#adoptionButton');
if(adoptionButton.length !== 0){
	$('#continueAdoption').click(function(){
		var errb = $('#adoptionMessageError');

		errb.hide();

		if($('#adoptionMessage').val() === '')
			errb.show();
		else
			$('form[name="adoptionMessageForm"]').submit();
	});

	adoptionButton.click(function(){
		$('#adoptionModal').modal();
	});
}

var process = $('#processModal');
if(process.length !== 0){

	var retrieve_messages = function(data){
		console.log(data);
	};

	var send_message = function(data){
	};

	$.ajax({
		type: 'POST',
		url: '/thread/',
		data: {csrfmiddlewaretoken: safecode, nome: 'BRENO'},
		success: retrieve_messages
	});

	$('.dogprocess').click(function(){
		var id = $(this).attr('data-id');
	})
}
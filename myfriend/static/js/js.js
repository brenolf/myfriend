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

	var maps = {home: '/', search: '/dogs/search/', testimonials: '/testimonials/', login: '/accounts/login/'};

	for(var i in maps)
		if(window.location.pathname == maps[i])
			mnhSelect.val(i);

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
	window.dog = null;

	$('#processModal').on('hide.bs.modal', function(){
		window.dog = null;
	});


	var retrieve_messages = function(data){
		$('#loader').hide();
		var canvas = $('#processThread');

		for(var i = 0, l = data.length; i < l; i++){
			var e = data[i];

			var nome = e.user === null ? 'Você' : e.user;
			style = e.user == null ? 'info' : 'default';

			canvas.append('<div class="panel panel-' + style + '">\
				<div class="panel-heading"><strong>' + nome + '</strong> diz: <small>' + e.date + '</small><div class="clear"></div></div>\
				<div class="panel-body">\
				' + e.content + '\
				</div>\
				</div>');
		}

		$('#formMessage, .modal-footer').show();
	};

	$('.dogprocess').click(function(){
		$('#loader').show();
		$('#formMessage, .modal-footer').hide();
		$('#formMessage textarea').val('');
		$('#processModal').modal();
		$('#processThread').empty();

		window.dog = $(this).attr('data-id');

		if($(this).attr('data-adopter') === '0')
			$('#denyAdoption, #confirmAdoption').css({display: 'inline-block'});
		else
			$('#denyAdoption, #confirmAdoption').hide();

		$.ajax({
			type: 'POST',
			url: '/thread/',
			data: {csrfmiddlewaretoken: safecode, dog: window.dog},
			success: retrieve_messages,
			dataType: 'json'
		});
	});

	var reload_thread = function(){
		$('#formMessage').hide();
		$('#formMessage textarea').val('');
		$('#processModal').modal();
		$('#processThread').empty();

		$.ajax({
			type: 'POST',
			url: '/thread/',
			data: {csrfmiddlewaretoken: safecode, dog: window.dog},
			success: retrieve_messages,
			dataType: 'json'
		});
	};

	var communication = function(deny, allow, success){
		if(success == undefined)
			success = reload_thread;

		$.ajax({
			type: 'POST',
			url: '/send_message/',
			data: {csrfmiddlewaretoken: safecode, content: $('#adoptionMessage').val(), dog: window.dog, deny: deny, allow: allow},
			success: success,
			dataType: 'json'
		});
	};

	$('#sendMessage').click(function(){
		var errb = $('#adoptionMessageError');

		errb.hide();

		if($('#adoptionMessage').val() === '')
			errb.show();

		else {
			$('#formMessage').hide();
			$('#processThread').empty();
			$('#loader').show();

			communication(false, false);
		}
	});

	$('#denyAdoption, #confirmAdoption').click(function(){
		var isConfirm = $(this).attr('id') === 'confirmAdoption';

		$('#processThread').empty();
		$('#formMessage, .modal-footer').hide();
		$('#loader').show();
		

		communication(!isConfirm, isConfirm, function(data){
			$('#loader').hide();
			action = isConfirm ? 'realizada' : 'negada';

			if(data.ok){
				$('#processThread').append('<h2>Adoção ' + action + ' com sucesso!</h2>');
				setTimeout(function(){window.location.reload(true);}, 2000);
			} else {
				$('.modal-footer').show();
				reload_thread();
			}
		});
	});
}
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
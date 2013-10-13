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

	$('#adopted_dogs img').tooltip({placement: 'bottom'});
}
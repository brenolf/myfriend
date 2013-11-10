function windowResponsive(){
	var isHome = $('#main_video').length !== 0;
	var W = $(window).width();
	var maxW = isHome ? 870 : 645;
	
	if(W < maxW){
		$('header ul').hide();
		$('header select').show();
		$('footer ul').hide();

		$('footer ul').hide();
		$('footer div:first-child').css({marginTop: '-20px'});
		$('footer div:first-child a').css({display: 'block', margin: '0 auto'});

		if(isHome){
			$('header').css({height: '300px'});
		}

	} else {
		$('header ul').show();
		$('header select').hide();

		$('footer ul').show();
		$('footer div:first-child').css({marginTop: 0});
		$('footer div:first-child a').css({display: 'inline-block', margin: '10px'});

		if(isHome){
			$('header').css({height: '600px'});
		}
	}
};

$(window).resize(function(){
	windowResponsive();
});

$(window).load(function(){
	windowResponsive();
});
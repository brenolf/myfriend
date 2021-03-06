if($('#wysiwyg-form').length !== 0){
	$('#wysiwyg-form select[name="color"], \
		#wysiwyg-form select[name="size"]').change(function(){
			var o = $(this);
			var ctt = o.val();

			if(o.attr('name') == 'color')
				colorEval(ctt);
			else
				sizeEval(ctt);
	});
}

if($('#full-search').length !== 0){
	var opts = window.location.search.substr(1).split('&');

	for(var i = 0; i < opts.length; i++){
		var e = opts[i].split('=');

		if(e[0] === 'color')
			colorEval(e[1]);
		
		else if(e[0] === 'size')
			sizeEval(e[1]);

	}
}

function colorEval(ctt){
	var map = {bl: '#333333', ma: '#8E6B18', wh: '#EBEBEB', gr: '#757575', go: '#EAB43E', bw: '-webkit-linear-gradient(top, #333 0%,#ffffff 50%)'};
	$('#dog-mask').css({background: map[ctt]});
}

function sizeEval(ctt){
	var map = {xs: 60, s: 85, m: 100, l: 120, xl: 150};
	$('#dog-mask').css({width: map[ctt], height: map[ctt]});
}
// get alltags

$(document).ready(function (){
     $.ajaxSetup({
	 success: function (data) {
	    var dict_tags;
	    dict_tags = $.parseJSON(data);
	    $.each( dict_tags, function (key, value) {
		    switch (value) {
		        case 2:
			     $('.alltags').append('<a href="/tags/'+key+'"><span class="type2">'+key+' '+'</span></a>')
			     break
			case 3:
			     $('.alltags').append('<a href="/tags/'+key+'"><span class="type3>'+key+' '+'</span></a>')
			     break
			case 4:
			     $('.alltags').append('<a href="/tags/'+key+'"><span class="type4>'+key+' '+'</span></a>')
			     break
			case 5:
			     $('.alltags').append('<a href="/tags/'+key+'"><span class="type5">'+key+' '+'</span></a>')
			     break
			default:
			     $('.alltags').append('<a href="/tags/'+key+'"><span class="type2">'+key+' '+'</span></a>')
                    }
		}
	    );
	 }
     });
     $.post('ajax/get_alltags/', {});
});


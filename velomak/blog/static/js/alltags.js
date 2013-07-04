// get alltags

$(document).ready(function (){
     $.ajaxSetup({
	 success: function (data) {
	    var dict_tags;
	    dict_tags = $.parseJSON(data);
	    $.each( dict_tags, function (key, value) {
		$('.alltags').append('<a href="/tags/'+key+'"><span class="type'+value+'">'+key+' '+'</span></a>');
		    }
	    );
	 }
     });
     $.post('ajax/get_alltags/', {});
});


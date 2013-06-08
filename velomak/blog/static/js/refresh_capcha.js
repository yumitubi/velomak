// отправляет ajax-запрос на сервер

$(document).ready(function (){
  $('#refresh_capcha').click(function(){
     $.ajaxSetup({
	 success: function(data) {
	    data = $.parseJSON(data);
	    $('#capcha_img').attr('src', '/static/images/capcha/'+data['img_name']);
	 }
     });
     $.post('ajax/get_capcha/', {});
   });
});
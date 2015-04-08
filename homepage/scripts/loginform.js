$(function() {
	$('#loginform').ajaxForm(function(data){
		$('#modal1').find('.modal-body').html(data);
	});//ajaxForm
}); //ready
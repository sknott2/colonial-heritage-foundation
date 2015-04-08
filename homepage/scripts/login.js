$(function () {

	$('#login_dialog').modal({
		show: false,
	});//modal

	$('#login').on('click', function(){
		$('#modal1').modal('show');
		$.ajax({
			url: '/homepage/login.loginform',
			success: function(data) {
				$('#login_dialog').find('.modal-body').html(data);
			},//success
		});//ajax
	});//click
});//ready
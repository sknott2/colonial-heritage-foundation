$(function() {

	$('#login').on('click', function(){
		$('#modal1').modal('show');
		$.ajax({
			url: '/homepage/login.loginform',
			success: function(data){
				$('#modal1').find('.modal-body').html(data);
			},//success
		});//ajax
	}),//click

	$('#shopping_cart').on('click', function() {

		$.loadmodal({
			url: '/homepage/shoppingcart/',
			title: 'Shopping Cart',
			width: '600px'
		})
	});
}); //ready


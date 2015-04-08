$(function() {
	console.log('3')
	$('#quantityform').ajaxForm(function(data) {
		console.log("Hi there")
		$('#jquery-loadmodal-js-body').html(data)
	});
	console.log('4')
}); //ready
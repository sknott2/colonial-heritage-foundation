$(function() {
	console.log('3')
	$('#quantityform').ajaxForm(function(data) {
		$('#jquery-loadmodal-js-body').html(data)
	});
	console.log('4')
}); //ready
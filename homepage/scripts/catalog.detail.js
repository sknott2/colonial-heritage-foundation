

$(function () {

        $('#add_cart').on('click', function() {

            var pid = $(this).attr('data-pid');
            console.log('1')
            $.loadmodal({
                url: "/homepage/shoppingcart.add/" + pid + "/",
                title: 'Shopping Cart',
                width: '600px'

            });
            console.log('2')
        });//click

        $('#cart').on('click', function() {
            var pid = $(this).attr('data-pid') ;
            var qty = $('.input-quantity').val;

            $.loadmodal({
                url: "/homepage/shoppingcart.add/" + pid + "/" + qty,
                title: 'Shopping Cart',
                width: '600px',
                type: "POST"

            });//loadmodal

        });//click



});//ready
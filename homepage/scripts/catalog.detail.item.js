$(function () {

        $('#add_cart').on('click', function() {
            console.log('1')
            var pid = $(this).attr('data-pid') ;
            var qty = 1
            console.log(pid)
            console.log(qty)
            $.loadmodal({
                url: "/homepage/shoppingcart.add_item/" + pid + "/" + qty,
                title: 'Shopping Cart',
                width: '600px'

            });//loadmodal*/
            console.log('2')

        });//click

});//ready
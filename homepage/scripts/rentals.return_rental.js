$(function () {
/*
    $('#DamageFee').modal({
        show: false,
    });// modal

    $('#damages').on('click', function() {
        $('#DamageFee').modal('show');
    });*/

       $('#damages').on('click', function() {
            console.log('Hi guys');

            var userid = $(this).attr('data-userid');
            var agentid = $(this).attr('data-agentid');
            var returnid = $(this).attr('data-returnid');
            var rentalid = $(this).attr('data-rentalid');
            var itemid = $(this).attr('data-itemid');

            $.loadmodal({
                url: "/homepage/rentals.return_damageFee/" + userid + "/" + agentid + "/" + returnid + "/" + rentalid + "/" + itemid,
                title: "Damages",
                width: '600px',
            })//loadmodal
        });//click

});//ready
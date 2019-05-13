$(function(){
    $('#modalopen10').click(function() {
    $('#modal-open').fadeIn();
    });
$(".modalClose10").click(function(){
    $(this).parents(".modal10").fadeOut();
    $(".modalOpen10").removeClass("open");
    return false;
    });  

});
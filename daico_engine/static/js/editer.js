$(function(){
    $('#modalopen100').click(function() {
    $('#modal-open1').fadeIn();
    });
$(".modalClose10").click(function(){
    $(this).parents(".modal10").fadeOut();
    $(".modalOpen10").removeClass("open");
    return false;
    });  

});
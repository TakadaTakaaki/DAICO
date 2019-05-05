$(function() {
    $('#login-show').click(function() {
      $('#login-modal').fadeIn();
    });
    $('#login-show2').click(function() {
      $('#login-modal2').fadeIn();
    });
    $('.close-modal').click(function() {
        $('#login-modal').fadeOut();
        $('#signup-modal').fadeOut();
      });
    $('.close-modal2').click(function() {
      $('#login-modal2').fadeOut();
      $('#signup-modal2').fadeOut();
    });
  });


$(function(){
    $('.maru').hover(
      function(){
        $(this).animate({
          'font-size':'90px'
        }, 300);
      },
      function(){
        $(this).animate({
          'font-size':'70px'
        }, 300);
      }
    );
    
  });
 
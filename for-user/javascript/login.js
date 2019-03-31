$(function() {
    $('#login-show').click(function() {
      $('#login-modal').fadeIn();
    });
    $('.close-modal').click(function() {
        $('#login-modal').fadeOut();
        $('#signup-modal').fadeOut();
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
 
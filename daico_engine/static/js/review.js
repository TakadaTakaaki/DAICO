$("#review").click(function(){
		
    var navClass = $(this).attr("class"),
        href = $(this).attr("href");
        
    if(href === "#modal02") {
    $(href).children(".inner0").css("animation","modal 0.5s forwards");
    }
    $(href).fadeIn();
    $(this).addClass("open");
    return false;
});
$('.close-modal1').click(function() {
  $('#modal04').fadeOut();
});

$(".modaltoukou1").click(function(){
  
  var parentsID = $(this).parents(".modal").attr("id");
  
  if(parentsID === "modal02") {
    $(this).parents(".modal03").children(".inner0").css("animation","modaltoukou 0.5s forwards");
  }
  
  $(this).parents(".modal03").fadeOut();
  $(".modalOpen1").removeClass("open");
  return false;
});  

// $(function() {
//   $('#review').click(function() {
//     $('#modal04').fadeIn();
//   });
//   $('.close-modal1').click(function() {
//       $('#save').fadeOut();
//     });
//   $('.close-modal2').click(function() {
//     $('#login-modal2').fadeOut();
//     $('#signup-modal2').fadeOut();
//   });
// });
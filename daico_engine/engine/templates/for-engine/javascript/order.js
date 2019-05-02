$(".modalOpen").click(function(){
		
    var navClass = $(this).attr("class"),
        href = $(this).attr("href");
        
    if(href === "#modal02") {
    $(href).children(".inner").css("animation","modal 0.5s forwards");
    }
    $(href).fadeIn();
    $(this).addClass("open");
    return false;
});

$(".modalClose1").click(function(){
  
  var parentsID = $(this).parents(".modal").attr("id");
  
  if(parentsID === "modal02") {
    $(this).parents(".modal00").children(".inner").css("animation","modalClose 0.5s forwards");
  }
  
  $(this).parents(".modal00").fadeOut();
  $(".modalOpen").removeClass("open");
  return false;
});  

$(".modalOpen_0").click(function(){
		
  var navClass = $(this).attr("class"),
      href = $(this).attr("href");
      
  if(href === "#modal02") {
  $(href).children(".inner_0").css("animation","modal 0.5s forwards");
  }
  $(href).fadeIn();
  $(this).addClass("open");
  return false;
});

$(".modalClose_1").click(function(){

var parentsID = $(this).parents(".modal").attr("id");

if(parentsID === "modal02") {
  $(this).parents(".modal_00").children(".inner_0").css("animation","modalClose_0 0.5s forwards");
}

$(this).parents(".modal_00").fadeOut();
$(".modalOpen_0").removeClass("open");
return false;
});  

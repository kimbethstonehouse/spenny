//
// NAME JQUERY
//

$('.name').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-paper-plane').addClass("next");
    } else {
      $('.icon-paper-plane').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.name').click(
  function(){
    console.log("Something");
    $('.name-section').addClass("fold-up");
    $('.income-section').removeClass("folded");
  }
);

//
// INCOME JQUERY
//

$('.income').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-money').addClass("next");
    } else {
      $('.icon-money').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.income').click(
  function(){
    console.log("Something");
    $('.income-section').addClass("fold-up");
    $('.dob-section').removeClass("folded");
  }
);

//
// DOB JQUERY
//

$('.dob').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-birth').addClass("next");
    } else {
      $('.icon-birth').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.dob').click(
  function(){
    console.log("Something");
    $('.dob-section').addClass("fold-up");
    $('.location-section').removeClass("folded");
  }
);

//
// LOCATION JQUERY
//

$('.location').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-location').addClass("next");
    } else {
      $('.icon-location').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.location').click(
  function(){
    console.log("Something");
    $('.location-section').addClass("fold-up");
    $('.occupation-section').removeClass("folded");
  }
);

//
// OCCUPATION JQUERY
//

$('.occupation').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-occupation').addClass("next");
    } else {
      $('.icon-occupation').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.occupation').click(
  function(){
    console.log("Something");
    $('.occupation-section').addClass("fold-up");
    $('.accomcost-section').removeClass("folded");
  }
);

//
// ACCOM JQUERY
//

$('.accomcost').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-accom').addClass("next");
    } else {
      $('.icon-accom').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.accomcost').click(
  function(){
    console.log("Something");
    $('.accomcost-section').addClass("fold-up");
    $('.adultdep-section').removeClass("folded");
  }
);

//
// ADULT JQUERY
//

$('.adultdep').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-adults').addClass("next");
    } else {
      $('.icon-adults').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.adultdep').click(
  function(){
    console.log("Something");
    $('.adultdep-section').addClass("fold-up");
    $('.childdep-section').removeClass("folded");
  }
);

//
// CHILD JQUERY
//

$('.childdep').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-children').addClass("next");
    } else {
      $('.icon-children').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.childdep').click(
  function(){
    console.log("Something");
    $('.childdep-section').addClass("fold-up");
    $('.smoker-section').removeClass("folded");
  }
);

//
// SMOKER JQUERY
//

$('.smoker').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-smoke').addClass("next");
    } else {
      $('.icon-smoke').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.smoker').click(
  function(){
    console.log("Something");
    $('.smoker-section').addClass("fold-up");
    $('.drinker-section').removeClass("folded");
  }
);

//
// DRINKER JQUERY
//

$('.drinker').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-drink').addClass("next");
    } else {
      $('.icon-drink').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.drinker').click(
  function(){
    console.log("Something");
    $('.drinker-section').addClass("fold-up");
    $('.email-section').removeClass("folded");
  }
);

//
// EMAIL JQUERY
//

$('.email').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-email').addClass("next");
    } else {
      $('.icon-email').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.email').click(
  function(){
    console.log("Something");
    $('.email-section').addClass("fold-up");
    $('.password-section').removeClass("folded");
  }
);

//
// PASSWORD JQUERY
//


$('.password').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-lock').addClass("next");
    } else {
      $('.icon-lock').removeClass("next");
    }
  }
);

$('.next-button.password').click(
  function(){
    console.log("Something");
    $('.password-section').addClass("fold-up");
    $('.success').css("marginTop", 0);
  }
);
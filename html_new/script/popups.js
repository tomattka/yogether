$(document).ready(function(){

    // Login form show
    $('#a-login').click(showLoginForm);
    $('#b-register').click(showLoginForm); // !!! temp

    // Forms close functions
    $('#darkscreen').click(closeAll);
    $('#popups').click(closeAll);
    $('#login-form-close').click(closeAll);
    $('#login-form').click(function(e){
        e.stopPropagation();
    });

    $('#bAddFriendMobile').click(showLoginForm); // !!! temp
});

function closeAll(){
    $('#popups').children().hide();
    $('#popups').hide();
    $('#darkscreen').hide();
}

function showLoginForm(){
    $('#darkscreen').show();
    $('#popups').css('display','flex');
    $('#login-form').show();
    scrollTopMobile();
    return false;
}

function scrollTop(event, speed=400) {
    event.preventDefault();
    $('html, body').animate({ scrollTop: 0 }, speed);
}

function scrollTopMobile(){
    windowWidth = $(window).width();
    if (windowWidth < 767)

    $('html, body').animate({ scrollTop: 0 }, 400);
}

var mobMenu, popups, darkscreen;

$(document).ready(function(){

    // Assigning elems to variables
    mobMenu = $("#mobile-menu");
    popups = $("#popups");
    darkscreen = $('#darkscreen');

    // --------- Mobile menu ---------- //
    $("#mobile-menu-close").click(closeMenu); // menu x button
    $("#aMobMenu").click(showMenu); // menu icon click

    // Login form show
    $('#aLogin').click(showLoginForm);
    $('#aLoginMob').click(showLoginForm);
    $('#bRegister').click(showLoginForm); // !!! temp

    // Forms close functions
    darkscreen.click(closeAll);
    popups.click(closeAll);
    $('#login-form-close').click(closeAll);
    $('#login-form').click(function(e){
        e.stopPropagation();
    });

});

$(window).resize(moveMenu); // correcting menu position on window resize

// !!!!!!!!!!!!!!!!!!!!!!!!!!! Здесь в попапс перепродумать логику

// --------------------- Popups ----------------------- //
function closeAll(){
    if (mobMenu.is(":visible"))
        closeMenu();
    else{
    popups.children().hide();
    popups.hide();
    darkscreen.hide();
    }
}

function showLoginForm(){
    darkscreen.show();
    popups.css('display','flex');
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

// ----------------- Mobile menu ------------------- //


function showMenu(){
    darkscreen.show();
    popups.css('display','flex');
    checkMenuHeight();
    mobMenu.animate({left: "-=" + mobMenu.width()}, 350);
    return false;
}

function closeMenu(){
    mobMenu.animate({left: "+=" + mobMenu.width()}, 350, 
    function(){ // menu animate end
        popups.hide();
        darkscreen.hide();
    });
    return false;
}

function moveMenu(){ // correcting menu position on window resize
    checkMenuHeight();
    if (mobMenu.is(":visible"))
    {
        leftPos = $(window).width() - mobMenu.width();
        mobMenu.css('left', leftPos + 'px');
    }
    else
        mobMenu.css('left', $(window).width() + 'px');
}

function checkMenuHeight(){
    if (mobMenu.height() < $(window).height())
        popups.css('height', '100%');
    if (popups.height() < mobMenu.height())
        popups.css('height', mobMenu.height() + 'px');
}
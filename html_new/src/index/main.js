$(document).ready(function(){
    // --------- Mobile menu ---------- //
    $("#x-close-mobmenu").click(closeMenu); // menu x button
    $("#darkened_menu").click(closeMenu); // darkened screen under menu
    $("#show-mob-menu").click(showMenu); // menu icon click
    // --------- Register dialog ---------- //
    $("#darkened").click(closeRegisterDialog); // darkened screen reg dialog click
    $("#x-close-form").click(closeRegisterDialog); // dialog x button    
    // --------- Register buttons ---------- //
    $("#b-reg2").click(showRegisterDialog); // register button click
    $("#b-reg").click(registerFromMobMenu); // register from top menu
    $("#b-regMob").click(registerFromMobMenu); // register from mobile menu
});

$(window).resize(moveMenu);

// ------------- Mobile menu ----------------- //

function showMenu(){
    $("#darkened_menu").show();
    $("#menuroll").show();
    checkMenuHeight();
    menu = $("#mobile_menu");
    menu.animate({left: "-=" + menu.width()}, 350);
    return false;
}

function closeMenu(){
    menu = $("#mobile_menu");
    menu.animate({left: "+=" + menu.width()}, 350, 
    function(){ // menu animate end
        $("#menuroll").hide();
        $("#darkened_menu").hide();
    });
    return false;
}

function moveMenu(){ // correcting menu position on window resize
    checkMenuHeight();
    menu = $("#mobile_menu");
    if (menu.is(":visible"))
    {
        leftPos = $(window).width() - menu.width();
        menu.css('left', leftPos + 'px');
    }
    else
        menu.css('left', $(window).width() + 'px');
}

function checkMenuHeight(){
    menuroll = $("#menuroll");
    menu = $("#mobile_menu");
    if (menu.height() < $(window).height())
        menuroll.css('height', '100%');
    if (menuroll.height() < menu.height())
        menuroll.css('height', menu.height() + 'px');
}

// -------------- Register form -------------- //

function showRegisterDialog(){
    $("#darkened").show();
    $("#regform").show();
    return false;
}

function closeRegisterDialog(){
    $("#darkened").hide();
    $("#regform").hide();
}

function registerFromMobMenu()
{
    closeMenu();
    $("#darkened_menu").hide();
    showRegisterDialog();
    return false;
}


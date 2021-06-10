var mobMenu, loginForm, logoutMessage, popups, darkscreen;

$(document).ready(function(){

    // Assigning elems to variables
    mobMenu = $("#mobile-menu");
    popups = $("#popups");
    darkscreen = $('#darkscreen');
    loginForm = $('#login-form');
    logoutMessage = $('#logout-confirm');

    // --------- Mobile menu ---------- //
    $("#mobile-menu-close").click(closeMenu); // menu x button
    $("#aMobMenu").click(showMenu); // menu icon click

    // Login form show
    $('#aLogin').click(showLoginForm);
    $('#aLoginMob').click(showLoginForm);
    // Logout message show
    $('#bRegister').click(showLogoutMessage); // !!! temp

    // Forms close functions
    darkscreen.click(closeAll);
    popups.click(closeAll);
    $('#login-form-close').click(closeAll);
    $('#logout-confirm-close').click(closeAll);
    $('#logout-cancel').click(closeAll);

    // Prevent form click reaction
    loginForm.click(function(e){
        e.stopPropagation();
    });
    logoutMessage.click(function(e){
        e.stopPropagation();
    });

});

$(window).resize(moveMenu); // correcting menu position on window resize

// !!!!!!!!!!!!!!!!!!!!!!!!!!! Здесь в попапс перепродумать логику

// --------------------- Popups ----------------------- //
function closeAll(){
    if (mobMenu.is(":visible"))
        closeMenu();
    else
    {
        //popups.children() - может пригодится потом
        popups.children().fadeOut(150, function(){            
            popups.hide();
            darkscreen.hide();
        });
        // loginForm.fadeOut(150, function(){            
        //     popups.hide();
        //     darkscreen.hide();
        // });
    }
}

function showLoginForm(){
    darkscreen.show();
    popups.css('display','flex');
    loginForm.fadeIn(150);
    scrollTopMobile();
    return false;
}

function showLogoutMessage(){
    darkscreen.show();
    popups.css('display','flex');
    logoutMessage.fadeIn(150);
    scrollTopMobile();
    return false;
}

// function scrollTop(event) {
//     event.preventDefault();
//     $('html, body').animate({ scrollTop: 0 }, 400);
// }

function scrollTopMobile(){
    windowWidth = $(window).width();
    if (windowWidth < 767)

    $('html, body').animate({ scrollTop: 0 }, 400);
}

// ----------------- Mobile menu ------------------- //


function showMenu(){
    mobMenu.show();
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
        mobMenu.hide();
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
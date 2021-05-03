function closeAll(){
    $('#darkscreen').children().hide();
    $('#darkscreen').hide();
}

function showLoginForm(){
    $('#darkscreen').css('display','flex');
    $('#login-form').show();
    return false;
}


$(document).ready(function(){

    // Login form show
    $('#a-login').click(showLoginForm);
    $('#b-register').click(showLoginForm); // !!! temp

    // Forms close functions
    $('#darkscreen').click(closeAll);
    $('#login-form-close').click(closeAll);
    $('#login-form').click(function(e){
        e.stopPropagation();
    });
});

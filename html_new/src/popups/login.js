var loginProgress, loginError;

$(document).ready(function(){
    loginProgress = $("#login-progress");
    loginError = $("#login-error");

    $("#login-form__login-button").click(ajaxLogin); // login button click
});

function ajaxLogin(e){
    e.preventDefault();
    username = $("#iLogin").val();
    password = $("#iPassword").val();

    if (username == '' || password == '') {
        loginError.html("Введите логин и пароль!");
        loginError.show();
    }
    else
    {
        loginError.hide();
        loginProgress.show();
        $.ajax({
            type: "POST",
            url: "login-check.html?username=" + username + "&password=" + password,
            data: { username: username, password: password } // change to post original data
          }).done(function(msg) {              
              loginProgress.hide();
              if (msg != "ok") {
                message = "Неизвестная ошибка";
                if (msg == "no user")
                    message = "Пользователя с указанным логином или e-mail не&nbsp;существует!";
                if (msg == "wrong password")
                    message = "Введено неверное сочетание логин-пароль!";
                loginError.html(message);
                loginError.show();
              }
              else {
                //$(this).unbind('submit').submit()
                window.location = e.target.href;
              }
              
          });       
    }
}
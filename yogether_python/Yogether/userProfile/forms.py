from allauth.account.forms import LoginForm


class YGLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(YGLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'login-form__input login-form__input_login',
            'placeholder': 'Логин'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'login-form__input login-form__input_password'
        })
        self.fields['remember'].widget.attrs.update({
            'checked': 'true',
            'style': 'display: none;'
        })

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(YGLoginForm, self).login(*args, **kwargs)
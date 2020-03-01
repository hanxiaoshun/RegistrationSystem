from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=20, min_length=2)
    nickname = forms.CharField()
    password = forms.CharField()

from django import forms


class RegisterTeacherForm(forms.Form):
    username = forms.CharField(label='username', max_length=20, min_length=2)
    nickname = forms.CharField()
    password = forms.CharField()
    real_name = forms.CharField(required=False)
    contact_number = forms.CharField(required=False)
    work_unit = forms.CharField(required=False)
    explain = forms.CharField(required=False)

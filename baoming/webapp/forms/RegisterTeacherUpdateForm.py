from django import forms


class RegisterTeacherUpdateForm(forms.Form):
    update_id = forms.IntegerField()
    username = forms.CharField(label='username', max_length=20, min_length=2, required=False)
    nickname = forms.CharField(required=False)
    real_name = forms.CharField(required=False)
    contact_number = forms.CharField(required=False)
    work_unit = forms.CharField(required=False)
    explain = forms.CharField(required=False)

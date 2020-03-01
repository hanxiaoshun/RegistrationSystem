from django import forms
from webapp.models import Picture


class PictureForm(forms.Form):
    # picture_name = forms.CharField(max_length=50, )
    file = forms.FileField()

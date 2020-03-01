from django import forms


class SystemMessageForm(forms.Form):
    receiver = forms.CharField(required=False)
    message_range = forms.IntegerField(required=False)
    message_level = forms.IntegerField(required=False)
    message_title = forms.CharField(required=True)
    message_content = forms.CharField(required=False)
    feedback_message = forms.IntegerField(required=False)

from django import forms
from app1.models import LogMessage

class LogForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ('title', 'message',)

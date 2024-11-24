from django import forms
from .models import OAuthKey

class OAuthKeyForm(forms.ModelForm):
    class Meta:
        model = OAuthKey
        fields = ["client_id", "client_secret"]
        widgets = {
            "client_secret": forms.PasswordInput(),
        }

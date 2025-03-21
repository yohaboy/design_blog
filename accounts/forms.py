from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # profile = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

        self.fields['password1'].label = "password"
        self.fields['password2'].label = "Confirm password"


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
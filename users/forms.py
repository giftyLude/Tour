from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in [
            "username",
            "email",
            "password1",
            "password2",
        ]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

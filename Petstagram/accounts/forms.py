from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import models

from Petstagram.accounts.models import PetstagramUser


class PetstagramUserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta(UserCreationForm.Meta):
        model = PetstagramUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
        help_texts = {
            'username': '',
            'email': ''
        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class PetstagramUserEditForm(models.ModelForm):
    class Meta:
        model = PetstagramUser
        fields = '__all__'
        exclude = ('password',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'picture': 'Image:',
            'gender': 'Gender:',
        }


from django import forms
from .models import Profile, Permission
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm

import re

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        #fields = ('bio', 'location', 'birth_date', 'gender', 'permission')


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    bio = forms.CharField(help_text='Required. Format: YYYY-MM-DD')
    location = forms.CharField(help_text='Required. Format: YYYY-MM-DD')
    GENDER = ((1, 'Masculino'), (2, 'Feminino'),)
    gender = forms.ChoiceField(choices=GENDER)
    permission = forms.ModelChoiceField(queryset=Permission.objects.all(), initial=4)
    #photo = forms.ImageField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')

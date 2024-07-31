from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .main_field import MultiEmailField
from .models import Contact

User = get_user_model()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=100)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.get(email=email):
            raise forms.ValidationError('Email Does Not Exist')
        return email

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.data.get('password')
        try:
            user = User.objects.get(username=username)
            print(user)
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
        except User.DoesNotExist:
            raise forms.ValidationError(f'{username} Does Not Exist')
        return password


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'The {email} is already registered')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password didn\'t match')
        return password


class UserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        exclude = ()


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipients = MultiEmailField()

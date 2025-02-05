from django import forms
from .models import BlogPost
from django.contrib.auth.models import User

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']



from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        error_messages={'required': 'Password is required.'}
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        error_messages={'required': 'Password confirmation is required.'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
        }
        help_texts = {
            'username': '', 
        }
        error_messages = {
            'username': {
                'required': 'Username is required.',
                'max_length': 'Username must be 150 characters or fewer.',
                'invalid': 'Enter a valid username.',
            },
            'email': {
                'required': 'Email address is required.',
                'invalid': 'Enter a valid email address.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        return username

"""
accounts/forms.py
Authentication and profile forms with full validation.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):
    """Registration form with email-first approach."""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-input'})
    )
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-input'})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-input'})
    )
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-input'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-input'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'form-input'})
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email.lower()


class LoginForm(AuthenticationForm):
    """Login form using email as identifier."""
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-input', 'autofocus': True})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-input'})
    )


class ProfileUpdateForm(forms.ModelForm):
    """User profile update form."""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'bio', 'company', 'job_title', 'avatar')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'bio': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'company': forms.TextInput(attrs={'class': 'form-input'}),
            'job_title': forms.TextInput(attrs={'class': 'form-input'}),
        }

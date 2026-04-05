from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-input'}),
            'subject': forms.TextInput(attrs={'placeholder': 'What is this about?', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us more...', 'class': 'form-input', 'rows': 5}),
        }

    def clean_message(self):
        message = self.cleaned_data.get('message', '')
        if len(message.strip()) < 20:
            raise forms.ValidationError('Please write a message of at least 20 characters.')
        return message

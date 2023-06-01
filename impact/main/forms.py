from django import forms

from .models import ContactQuestions


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your name',
        'id': 'name'
    }))

    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your email',
        'id': 'email'
    }))

    subject = forms.CharField(max_length=510, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject',
        'id': 'subject'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'rows': '7'
    }))

    class Meta:
        model = ContactQuestions
        fields = ('name',
                  'email',
                  'subject',
                  'message')

from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label=False, min_length=3, max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}))
    last_name = forms.CharField(label=False, min_length=3, max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}))
    subject = forms.CharField(label=False, min_length=3, max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}))
    email = forms.EmailField(label=False, min_length=6, max_length=30, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    message = forms.CharField(label=False, min_length=50, max_length=500, required=True, widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'}))
from django import forms



class ContactForm(forms.Form):
    name = forms.CharField(max_length=500, label="Name")
    email = forms.EmailField(max_length=500, label="Email")
    message = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Enter your comment here'}))
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100, min_length=3,required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}))
    email = forms.EmailField(label='Email',max_length=100, min_length=3, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Tu email'}))
    message = forms.CharField(label='Mensaje', max_length=1000, min_length=10, required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 4, 'cols': 40}))
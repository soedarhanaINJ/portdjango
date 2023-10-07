from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=125, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    massage = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
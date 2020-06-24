from django import forms


class NouveauContactForm(forms.Form):
    name = forms.CharField()
    profession = forms.CharField()
    avis = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
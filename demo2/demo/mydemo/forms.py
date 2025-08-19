from django import forms


class user_form(forms.Form):
    name = forms.CharField(label='Enter Your Name ',max_length=100)
    age = forms.IntegerField(label='Enter Your Age ')
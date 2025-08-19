from django import forms


class user_form(forms.Form):
    a = forms.IntegerField(label='Enter A ')
    b = forms.IntegerField(label='Enter B')
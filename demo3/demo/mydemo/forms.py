from django import forms


class user_form(forms.Form):
    num = forms.IntegerField(label='Enter Your Number ')
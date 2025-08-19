from django import forms


class user_form(forms.Form):
    p = forms.IntegerField(label='Enter Your Sub 1 ')
    r = forms.IntegerField(label='Enter Your Sub 2 ')
    t = forms.IntegerField(label='Enter Your Sub 3 ')

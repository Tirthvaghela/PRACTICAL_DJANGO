from django import forms


class user_form(forms.Form):
    sub1 = forms.IntegerField(label='Enter Your Sub 1 ')
    sub2 = forms.IntegerField(label='Enter Your Sub 2 ')
    sub3 = forms.IntegerField(label='Enter Your Sub 3 ')

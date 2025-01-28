from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    age = forms.IntegerField(max_value=999, required=True)

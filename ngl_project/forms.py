from django import forms

# Form for regestring a new user
class Register(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=20)
    last_name = forms.CharField(label="Last Name", max_length=20)
    username = forms.CharField(label="Userame", max_length=20)
    email = forms.EmailField(label="Email", )
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
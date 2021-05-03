from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    remember = forms.BooleanField(label="exampleCheck1", required=False)

class RegisterForm(forms.Form):
    name = forms.CharField(label="name")
    

class RetornoForm(forms.Form):
    regreso = forms.CharField(label="regreso")

class LeerForm(forms.Form):
    myFile = forms.CharField(label="myFile")
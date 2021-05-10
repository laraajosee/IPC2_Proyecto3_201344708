from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput(), label="password")
    remember = forms.BooleanField(label="exampleCheck1", required=False)

class RegisterForm(forms.Form):
    name = forms.CharField(label="name")
    # cualquiernombre       ###
    

class RetornoForm(forms.Form):
    regreso = forms.CharField(label="regreso")

class GraficarForm(forms.Form):
    comboBox = forms.CharField(label="comboBox")

class GraficarForm2(forms.Form):
    comboBox2 = forms.CharField(label="comboBox2")
   

    
class LeerForm(forms.Form):
    myFile = forms.CharField(label="myFile")


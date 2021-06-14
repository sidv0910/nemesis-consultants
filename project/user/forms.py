from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=15, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'size': 15, 'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=15, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    re_password = forms.CharField(max_length=15, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':100, 'class': 'form-control', 'placeholder': 'Address'}))

class UpdateForm(forms.Form):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'size': 15, 'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly': True, 'class': 'form-control', 'placeholder': 'Email Address'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size': 100, 'class': 'form-control', 'placeholder': 'Address'}))
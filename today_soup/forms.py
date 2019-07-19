from django import forms

class AuthenticationForm(forms.Form):
    """
    Login form
    """
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ['username', 'password']
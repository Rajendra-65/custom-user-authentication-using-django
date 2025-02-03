from django import forms
from account.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget = forms.PasswordInput
    )
    confirm_password = forms.CharField(
        widget = forms.PasswordInput
    )
    class Meta:
        model = User 
        fields = ["email","name","password","confirm_password"]

        def clean(self):
            cleaned_data = super().clen()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match")
            return cleaned_data
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email = email).exists():
                raise forms.ValidationError(
                    "A user with this email already exists."
                )
            return email
        
        
                
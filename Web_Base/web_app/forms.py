from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError


class RegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    terms = forms.BooleanField(
        label="I accepted the terms and conditions", required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'gender',
                  'date_of_birth', 'password1', 'password', 'terms']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email

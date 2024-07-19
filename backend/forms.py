from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'date_of_birth', 'date_of_death', 'content', 'author', 'submission_date', 'slug']

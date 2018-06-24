from django import forms
from .models import Advice, Profile
from django.forms import widgets


class AdviceModelForm(forms.ModelForm):
    class Meta:
        model = Advice
        fields = ['category', 'problem']


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'sex', 'birth_date', 'first_name', 'last_name', 'education']
        labels = {
            'email': 'Email:',
            'sex': 'Пол:',
            'birth_date': 'Дата рождения:',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'education': 'Образование',
        }
        widgets = {
            'birth_date': widgets.SelectDateWidget,
        }


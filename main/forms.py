from django import forms
from .models import Test

class TestForm(forms.ModelForm):
    option1 = forms.CharField(label='Вариант ответа 1', max_length=100)

    option2 = forms.CharField(label='Вариант ответа 2', max_length=100)

    option3 = forms.CharField(label='Вариант ответа 3', max_length=100)

    option4 = forms.CharField(label='Вариант ответа 4', max_length=100)

    class Meta:
        model = Test
        fields = ['title']

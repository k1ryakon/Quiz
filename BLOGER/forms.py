from .models import Quiz
from django import forms

class CreateQuizForm(forms.ModelForm):
    
    class Meta:
        model = Quiz
        fields = ('name', 'question1', 'question2', "question3")

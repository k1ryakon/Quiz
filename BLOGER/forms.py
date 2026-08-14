from .models import Quiz, Answer, Question
from django import forms


class CreateQuizForm(forms.ModelForm):
    
    class Meta:
        model = Quiz
        fields = ('name',)
               
class AnswerOnQuestion(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = ('is_correct', )
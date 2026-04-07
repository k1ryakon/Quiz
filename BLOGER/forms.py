from .models import Quiz, Answer, Question
from django import forms
from django_recaptcha.fields import ReCaptchaField

class CreateQuizForm(forms.ModelForm):
    
    recaptcha = ReCaptchaField()
    
    class Meta:
        model = Quiz
        fields = ('name',)
               
class AnswerOnQuestion(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = ('is_correct', )               
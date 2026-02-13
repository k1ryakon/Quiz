from .models import Quiz
from django import forms
from django_recaptcha.fields import ReCaptchaField

class CreateQuizForm(forms.ModelForm):
    
    recaptcha = ReCaptchaField()
    
    class Meta:
        model = Quiz
        fields = ('name', 'question1', 'question2', "question3")

class UpdateQuizForm(CreateQuizForm):
    class Meta:    
        model = Quiz
        fields = CreateQuizForm.Meta.fields + ('updater', "fixed")
               
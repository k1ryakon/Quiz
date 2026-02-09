from .models import Quiz, Comment
from django import forms

class CreateQuizForm(forms.ModelForm):
    
    class Meta:
        model = Quiz
        fields = ('name', 'question1', 'question2', "question3")

class UpdateQuizForm(CreateQuizForm):
    class Meta:    
        model = Quiz
        fields = CreateQuizForm.Meta.fields + ('updater', "fixed")
        
class CommentCreateForm(forms.ModelForm):
    """
    Форма добавления комментариев к статьям
    """
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'cols': 30, 'rows': 5, 'placeholder': 'Комментарий', 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('content',)        
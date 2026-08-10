from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField 

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    updater = models.ForeignKey(to=User, verbose_name='Обновил', on_delete=models.SET_NULL, null=True,
                            related_name='updater_posts', blank=True)
    fixed = models.BooleanField(verbose_name='Прикреплено', default=False)
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_NULL, related_name='author_posts')
    tags = TaggableManager(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'pk': self.pk})


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=350)
    
    def __str__(self):
        return self.text[:50]
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)


class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField() 
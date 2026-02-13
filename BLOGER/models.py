from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField 

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    question1 = models.CharField(max_length=200)
    question2 = models.CharField(max_length=200)
    question3 = RichTextField(config_name='awesome_ckeditor',max_length=200)
    updater = models.ForeignKey(to=User, verbose_name='Обновил', on_delete=models.SET_NULL, null=True,
                            related_name='updater_posts', blank=True)
    fixed = models.BooleanField(verbose_name='Прикреплено', default=False)
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_DEFAULT, related_name='author_posts',
                               default=1)
    tags = TaggableManager()
    
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('quiz_detail', kwargs={'pk': self.pk})

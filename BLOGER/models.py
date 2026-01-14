from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    question1 = models.CharField(max_length=200)
    question2 = models.CharField(max_length=200)
    question3 = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.name
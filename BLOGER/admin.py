from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Answer, QuizResult


class AnswerInLine(nested_admin.NestedTabularInline):
    model = Answer
    extra = 3


class QuestionInLine(nested_admin.NestedTabularInline):
    model = Question
    extra = 6
    inlines = [AnswerInLine]  # ← вот магия, вложенный inline


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInLine]
    list_display = ['name', 'author', 'fixed', 'created'] 

admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizResult)
admin.site.register(Question)

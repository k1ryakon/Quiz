from django.contrib import messages
from django.views.generic import ListView, RedirectView, DetailView
from .models import Quiz
from django.shortcuts import render

class Quizeble(ListView):
    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'zapupa'
    
class MyRedirectEpta(RedirectView):
    pattern_name = 'index'
    
    def get_redirect_url(self, *args, **kwargs):
        messages.success(self.request, 'uletaesh/ bb')
        return super().get_redirect_url(*args, **kwargs)
    
    
def my_redirect_aloha(request):
    context = {'message': 'Сейчас произойдёт редирект...'}
    return render(request, 'redirect_page.html', context)

class QuizDetail(DetailView):
    model = Quiz
    template_name = 'quiz_detail.html'
    context_object_name = 'quiz'
    
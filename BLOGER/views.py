from django.contrib import messages
from django.views.generic import ListView, RedirectView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quiz
from django.shortcuts import render
from .forms import CreateQuizForm, UpdateQuizForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Quizeble(ListView):
    paginate_by = 2
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
    



class QuizCreareView(LoginRequiredMixin, CreateView):
    model = Quiz
    template_name = 'quiz_create.html'
    form_class = CreateQuizForm
    success_url = reverse_lazy('index')
    login_url = 'index'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление нового Квиза'
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    



class QuizUpdateView(UpdateView):
    model = Quiz
    template_name = 'quiz_update.html'
    form_class = UpdateQuizForm
    
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Quizes'
        return context
    
class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = 'quiz_delete.html'
    success_url = reverse_lazy('index')
from django.contrib import messages
from django.views.generic import ListView, RedirectView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quiz
from django.shortcuts import render
from .forms import CreateQuizForm, UpdateQuizForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from taggit.models import Tag


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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



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
    
class QuizTagsView(ListView):
    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'zapupa'
    paginate_by = 3
    tag = None
    
    def get_queryset(self):
        self.tag = Tag.objects.get(slug=self.kwargs['tag'])
        queryset = Quiz.objects.filter(tags__slug=self.tag.slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Статьи по тегу: {self.tag.name}'
        return context
    
    
    
    
    
def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request=request, template_name='errors/404.html', status=404, context={
        'title': 'Страница не найдена: 404',
        'error_message': 'К сожалению такая страница была не найдена, или перемещена', 
    })


def tr_handler500(request):
    """
    Обработка ошибки 500
    """
    return render(request=request, template_name='errors/error_page.html', status=500, context={
        'title': 'Ошибка сервера: 500',
        'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу, отчёт об ошибке мы направим администрации сайта',
    })


def tr_handler403(request, exception):
    """
    Обработка ошибки 403
    """
    return render(request=request, template_name='errors/error_page.html', status=403, context={
        'title': 'Ошибка доступа: 403',
        'error_message': 'Доступ к этой странице ограничен',
    })
from django.contrib import messages
from django.views.generic import ListView, RedirectView, DetailView, CreateView, DeleteView
from .models import Quiz, Answer, Question, QuizResult
from django.shortcuts import render
from .forms import CreateQuizForm, AnswerOnQuestion
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from taggit.models import Tag
from django.http import HttpResponseForbidden


class Quizeble(ListView):
    paginate_by = 10
    model = Quiz
    template_name = 'quiz_list.html'
    context_object_name = 'zapupa'
    
    
class QuizDetail(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quiz_detail.html'
    context_object_name = 'quiz'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = Question.objects.filter(quiz=self.object)
        context['questions'] = questions
        context['answers'] = Answer.objects.filter(question__in=questions)
        return context
    
    def handle_no_permission(self):
        return HttpResponseForbidden('ahah log!')

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     questions = Question.objects.filter(quiz=self.object)
    #     answere = Answer.objects.filter(question=questions)
    #     score = 0
    #     total = questions.count()
        
    #     for question in questions:
    #         selected_answer_id = request.POST.get(f'question_{question.pk}')
    #         if selected_answer_id:
    #             answer = Answer.objects.get(pk=selected_answer_id)
    #             if answer.is_correct == Answer.Status.RIGHT:
    #                 score += 1
    #     # вот это переписать надо
    #     # score надо чтобы был привязан к пользователю, у меня это пока что наверное не сделано.и они должны как то сохраняться у опред. пользователя к опред. квизу. чтобы мы их не просто потом выводили а где-то в бд это значение сохранялось.
        
    #     QuizResult.objects.create(user=request.user, quiz=self.object, score=score)
        
    #     # context = self.get_context_data()
    #     # context['score'] = score
    #     # context['total'] = total
    #     # вот это надо добавить в метод по нормальному 
    #     return render(request, 'quiz_detail.html', context)


class QuizCreareView(LoginRequiredMixin, CreateView):
    template_name = 'quiz_create.html'
    form_class = CreateQuizForm
    success_url = reverse_lazy('index')
    login_url = 'index'
    initial = {'name': 'lol'}
    permission_denied_message = 'ebbbaaat'
    
    # def handle_no_permission(self):
    #     return HttpResponseForbidden('autorize!')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление нового Квиза'
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = 'quiz_delete.html'
    success_url = reverse_lazy('index')
    
    


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
    

class MyRedirectEpta(RedirectView):
    pattern_name = 'index'
    
    def get_redirect_url(self, *args, **kwargs):
        messages.success(self.request, 'uletaesh/ bb')
        return super().get_redirect_url(*args, **kwargs)
    
    
def my_redirect_aloha(request):
    context = {'message': 'Сейчас произойдёт редирект...'}
    return render(request, 'redirect_page.html', context)

    
from django.contrib import messages
from django.views.generic import ListView, RedirectView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quiz, Comment
from django.shortcuts import render, redirect
from .forms import CreateQuizForm, UpdateQuizForm, CommentCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.formats import date_format
from django.utils.timezone import localtime


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
        context['form'] = CommentCreateForm  # new
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
    
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentCreateForm

    def is_ajax(self):
        return self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    def form_invalid(self, form):
        if self.is_ajax():
            return JsonResponse({'error': form.errors}, status=400)
        return super().form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post_id = self.kwargs.get('pk')
        comment.author = self.request.user
        comment.parent_id = form.cleaned_data.get('parent')
        comment.save()

        if self.is_ajax():
            return JsonResponse({
                'is_child': comment.is_child_node(),
                'id': comment.id,
                'author': comment.author.username,
                'parent_id': comment.parent_id,
                'time_create': date_format(
                    localtime(comment.time_create),
                    format='DATETIME_FORMAT',
                    use_l10n=True,
                ),
                'avatar': comment.author.profile.avatar.url,
                'content': comment.content,
                'get_absolute_url': comment.author.profile.get_absolute_url()
            }, status=200)

        return redirect(comment.post.get_absolute_url())

    def handle_no_permission(self):
        return JsonResponse({'error': 'Необходимо авторизоваться для добавления комментариев'}, status=400)
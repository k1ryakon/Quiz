from django.urls import path
from .views import Quizeble, MyRedirectEpta, my_redirect_aloha, QuizDetail, QuizCreareView, QuizUpdateView
from django.views.generic import RedirectView



urlpatterns = [
    path('', Quizeble.as_view(), name='index'),
    path('emae/', RedirectView.as_view(pattern_name='index')),
    path('epta/', MyRedirectEpta.as_view()),
    path('aloha/', my_redirect_aloha),
    path('quiz/<int:pk>/update/',QuizUpdateView.as_view(), name='quiz_update'),
    path('quiz/<int:pk>', QuizDetail.as_view(), name='quiz_detail'),
    path('quiz/create', QuizCreareView.as_view(), name='quiz_create'),
]

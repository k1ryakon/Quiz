from django.urls import path, include
from .views import Quizeble, MyRedirectEpta, my_redirect_aloha, QuizDetail, QuizCreareView, QuizDeleteView, QuizTagsView
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', Quizeble.as_view(), name='index'),
    path('emae/', RedirectView.as_view(pattern_name='index')),
    path('epta/', MyRedirectEpta.as_view()),
    path('aloha/', my_redirect_aloha),
    path('quiz/<int:pk>/', QuizDetail.as_view(), name='quiz_detail'),
    path('quiz/create/', QuizCreareView.as_view(), name='quiz_create'),
    path('quiz/<int:pk>/delete/', QuizDeleteView.as_view(), name='quiz_delete'),
    path('quiz/tags/<slug:tag>/', QuizTagsView.as_view(), name='quiz_tags'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('quiz/some/', views.some, name='quiz_some'),
]
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path
from .views import Quizeble, MyRedirectEpta, my_redirect_aloha
from django.views.generic import RedirectView

urlpatterns = [
    path('', Quizeble.as_view(), name='index'),
    path('emae/', RedirectView.as_view(pattern_name='index')),
    path('epta/', MyRedirectEpta.as_view()),
    path('aloha/', my_redirect_aloha),
]

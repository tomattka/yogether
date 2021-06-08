from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfile.as_view()),
    path('user/logincheck.html', views.LoginCheck.as_view()),
]
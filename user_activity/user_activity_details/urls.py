from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserActivityLog.as_view()),
]
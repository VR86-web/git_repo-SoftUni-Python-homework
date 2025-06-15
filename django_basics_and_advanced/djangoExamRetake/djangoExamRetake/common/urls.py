from django.urls import path

from djangoExamRetake.common import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
]

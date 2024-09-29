from django.urls import path, include
from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='details'),
        path('edit/', views.edit_details, name='edit'),
        path('delete/', views.delete_page, name='delete'),
    ]))
]

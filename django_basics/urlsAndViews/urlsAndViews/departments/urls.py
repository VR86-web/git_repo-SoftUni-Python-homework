from django.urls import path

from urlsAndViews.departments.views import index, view_with_name, view_with_int_pk

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', view_with_int_pk),
    path('<param>/', view_with_name),
]

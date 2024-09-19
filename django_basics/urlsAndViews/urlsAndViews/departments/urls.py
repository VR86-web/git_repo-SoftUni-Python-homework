from django.urls import path

from urlsAndViews.departments.views import index, view_with_name, view_with_name_variable, view_with_int_pk, \
    view_with_slug

urlpatterns = [
    path('', index),
    path('<int:pk>/', view_with_int_pk),
    path('<slug:slug>/', view_with_slug),
    path('<variable>/', view_with_name_variable),
    path('<param>/', view_with_name),
    path('<path:variable>/', view_with_name)
]
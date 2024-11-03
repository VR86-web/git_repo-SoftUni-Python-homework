
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('regularExam.common.urls')),
    path('album/', include('regularExam.authors.urls')),
    path('profile/', include('regularExam.posts.urls')),
]

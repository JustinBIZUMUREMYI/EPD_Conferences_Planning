from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('conference_planning.urls')),
    path('admin/', admin.site.urls),
]

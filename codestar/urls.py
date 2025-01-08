from django.contrib import admin
from django.urls import path
from art.views import my_art

urlpatterns = [
    path('admin/', admin.site.urls),
    path('art/', my_art, name='art'),
]

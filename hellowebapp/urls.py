from django.conf.urls import path
from django.contrib import admin

from collection import views


urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
]

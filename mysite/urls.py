from django.contrib import admin
from django.urls import path, include
from main import views as main_views

urlpatterns = [
    path('', main_views.index, name="index"),
    path('admin/', admin.site.urls),
]

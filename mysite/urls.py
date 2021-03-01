from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('index/', main_views.index, name="index"),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/',obtain_auth_token)
]

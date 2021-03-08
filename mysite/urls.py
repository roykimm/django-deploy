from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index/', main_views.index, name="index"),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/',obtain_auth_token)
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
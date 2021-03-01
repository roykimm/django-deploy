from django.urls import path, include
from .views import MemoViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('memos', MemoViewSet, basename='memos')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
]
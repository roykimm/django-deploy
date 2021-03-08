from django.urls import path, include
from .views import MemoViewSet, UserViewSet, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('memos', MemoViewSet, basename='memos')
router.register('users', UserViewSet, basename='users')
router.register('books', BookViewSet, basename='books')



urlpatterns = [
    path('api/', include(router.urls))
    
]
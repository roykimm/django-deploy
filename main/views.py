from django.shortcuts import render
from .models import Memo, Book
from django.contrib.auth.models import User
from .serializer import MemoSerializer, UserSerializer, BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,"main/index.html")

class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    parser_classes = (JSONParser,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # override 
    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        Book.objects.create(title=title, cover=cover)
        return HttpResponse({'message' : 'Book created'}, status=200)
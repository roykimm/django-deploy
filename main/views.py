from django.shortcuts import render
from .models import Memo
from django.contrib.auth.models import User
from .serializer import MemoSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser


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
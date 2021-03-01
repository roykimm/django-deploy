from rest_framework import serializers
from .models import Memo
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        #field = ['id','title','cont']
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id','username','password']

        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'required' : True
            }
        }

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
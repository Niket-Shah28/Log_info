from rest_framework import serializers
from .models import *

class usermodel(serializers.ModelSerializer):
    #password=serializers.CharField(read_only=True)
    class Meta:
        model=USER
        fields=['username','password','email']


    def create(self,validated_data):
        # username=validated_data['username']
        # password=validated_data['password']
        # email=validated_data['email']
        # user=USER()
        user=USER(username=validated_data['username'],
        password=validated_data['password'],
        email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=USER
        fields=['email','password']

# class Infomodel(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['']
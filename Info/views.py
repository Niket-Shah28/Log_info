from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status, permissions
from .serializers import *
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


class Register(GenericAPIView):
    permission_classes=[permissions.AllowAny]
    serializer_class=usermodel

    def post(self,request,format=None):
        user=usermodel(data=request.data)
        print(user)
        if user.is_valid():
            user.save()
            return Response("Successfully Registered",status=status.HTTP_202_ACCEPTED)
        else:
            return Response("Error Occured",status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST',])
def signin(request):
    if request.method=='POST':
        email=request.POST['Email']
        # print(logged)
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            info=Info()
            print(request.user)
            info.user=USER.objects.get(email=request.user)
            info.Time_logged=timezone.now()
            info.save()
            return Response("Logged In",status=status.HTTP_202_ACCEPTED)
        else:
            return Response("Login Failed",status=status.HTTP_400_BAD_REQUEST)



@login_required
def signout(request):
    print(request.user)
    info=Info.objects.filter(user=USER.objects.get(email=request.user))
    last=info.order_by('-Time_logged_out').last()
    last.Time_logged_out=timezone.now()
    last.save()
    logout(request)
    return JsonResponse("Logged Out Successfully",safe=False,status=status.HTTP_202_ACCEPTED)


def check_activity(request):
    info=Info.objects.all()
    data=list(info.values())
    return JsonResponse(data,safe=False,status=status.HTTP_202_ACCEPTED)




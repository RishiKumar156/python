from django.shortcuts import render
from .models import NewUser
from .serializer import Register_serializer, Login_serializer
from rest_framework  import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import loader
from django.http import HttpResponse
# Create your views here.

@api_view(['POST'])
def RegisterUser(request):
    serializer = Register_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message" : "Registration was success, Please login."}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message" : "Registration failed."}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def ListRegister(request):
    register = NewUser.objects.all()
    serializer = Register_serializer(register, many=True)
    if register:
            return Response(serializer.data, status=status.HTTP_302_FOUND)
    else:
        return Response({"message" : "Registration failed."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['post'])
def Login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        find_user = NewUser.objects.get(email=email, password=password)
        response_data = {
            "message" : "verfication success",
            "user_id" : find_user.id
        }
        t = loader.get_template('token/')
        # return HttpResponse(t.render)
        return Response(response_data ,status=status.HTTP_200_OK)
    except find_user.DoesNotExist:
        return Response({"message" : "user not found"}, status=status.HTTP_404_NOT_FOUND)
    
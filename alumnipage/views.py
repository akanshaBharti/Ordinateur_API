from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import *


class StandardAPIView(APIView):
    def post(selfself, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        date_of_birth = request.data.get('date_of_birth')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        gender = request.data.get('gender')
        roll_no = request.data.get('roll_no')
        status = request.data.get('status')
        firm = request.data.get('firm')
        date =request.data.get('date')
        image = request.data.get('image')
        alumni = User.objects.create(first_name=first_name,last_name=last_name, date_of_birth=date_of_birth, email=email,phone_number=phone_number,
                                     gender=gender, roll_no=roll_no, status=status, firm=firm, date=date, image=image)
        serializer = AlumniSerializer(alumni)
        return Response({'data': serializer.data})

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        serializer = AlumniSerializer(user)
        return Response(serializer.data)
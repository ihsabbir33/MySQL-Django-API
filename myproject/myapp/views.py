from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import  status
import json,jsonify

from myapp.models import Registration
from myapp.serializers import RegistrationSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def registration_list(request):
    result ={"message":"succesfully done","status":"success"}
    if request.method =='GET':
        registrationData = Registration.objects.all()
        registration_serializer = RegistrationSerializer(registrationData,many=True)
        return JsonResponse(registration_serializer.data,safe=False)
    elif request.method =='POST':
        registration_data = JSONParser().parse(request)
        registration_serializer = RegistrationSerializer(data=registration_data)
        print(registration_serializer)
        if registration_serializer.is_valid():
            registration_serializer.save()
            return JsonResponse(registration_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(registration_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Registration.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

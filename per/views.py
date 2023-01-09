from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class PersonalMVS(ModelViewSet):
  queryset = Personal.objects.all()
  serializer_class= PersonalSerializer
  
class DepartmentMVS(ModelViewSet):
  queryset = Department.objects.all()
  serializer_class= DepartmentSerializer
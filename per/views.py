from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

# Create your views here.

class PersonalMVS(ModelViewSet):
  queryset = Personal.objects.all()
  serializer_class= PersonalSerializer
  
class DepartmentMVS(ReadOnlyModelViewSet):
  queryset = Department.objects.all()
  serializer_class= DepartmentSerializer
  
class DynamicDepartmentMVS(DepartmentMVS):
  serializer_class= DepartmentDynamicSerializer
  lookup_field = "name"
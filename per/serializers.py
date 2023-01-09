from rest_framework import serializers
from .models import *


class PersonalSerializer(serializers.ModelSerializer):
  created_user = serializers.StringRelatedField()
  # title = serializers.SerializerMethodField()
  # gender = serializers.SerializerMethodField()
  days_since_joined = serializers.SerializerMethodField()
  class Meta:
    model = Personal
    fields = ("id", "first_name", "last_name", "salary","title", 
              "gender", "is_staff", "department", "start_date",
              "days_since_joined", "created_user")
    
  def get_days_since_joined(self, obj):
    import datetime
    current_time = datetime.datetime.now()
    return current_time.day - obj.start_date.day
  
  # def get_created_user(self, obj):
  #   return self.context["request"].user.username
  
  def get_title(self, obj):
    if obj.title == "TL":
      return "Team Lead"
    elif obj.title == "ML":
      return "Mid Lead"
    else:
      return "Junior"
    
  def get_gender(self,request, obj):
    if request.method == "GET":
      if obj.title == 1:
        return "Male"
      elif obj.title == 2:
        return "Female"
      elif obj.title == 3:
        return "Other"
      else:
        return "Prefer Not Say"
      



class DepartmentSerializer(serializers.ModelSerializer):
  personals = PersonalSerializer(many=True, required=False)
  personal_count = serializers.SerializerMethodField()
  
  class Meta:
    model = Department
    fields = ("id", "name","personal_count","personals")
    
  def get_personal_count(self, obj):
    return obj.personals.count()

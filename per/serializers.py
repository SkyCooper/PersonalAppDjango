from rest_framework import serializers
from .models import *
from pprint import pprint


class PersonalSerializer(serializers.ModelSerializer):
  created_user = serializers.StringRelatedField()
  # created_user_id = serializers.IntegerField(read_only=True)
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
  
  # gender = serializers.SerializerMethodField()
  # def get_gender(self, obj):
  #   return obj.get_gender_display()
  
  # title = serializers.SerializerMethodField()
  # def get_title(self, obj):
  #   return obj.get_title_display()
  
  def to_representation(self, instance):
    representation = super().to_representation(instance)
    
    representation['gender_text'] = representation['gender']
    representation['gender'] = dict(Personal.GENDERS)[representation['gender_text']]
    representation['title'] = dict(Personal.TITLES)[representation['title']]
    representation['kadir'] = "erhan"
    return representation
  
  def create(self, validated_data):
    validated_data["created_user_id"] = self.context["request"].user.id
    return super().create(validated_data)

class DepartmentSerializer(serializers.ModelSerializer):
  personal_count = serializers.SerializerMethodField()
  
  class Meta:
    model = Department
    fields = ("id", "name","personal_count")
    
  def get_personal_count(self, obj):
    return obj.personals.count()
  
  
class DepartmentDynamicSerializer(serializers.ModelSerializer):
  personals = PersonalSerializer(many=True, required=False)
  personal_count = serializers.SerializerMethodField()
  id = serializers.StringRelatedField()
  
  class Meta:
    model = Department
    fields = ("id", "name","personal_count","personals")
    
  def get_personal_count(self, obj):
    return obj.personals.count()

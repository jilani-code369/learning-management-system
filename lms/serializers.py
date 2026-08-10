
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model 

from .models import *


# Getting the active user of the project
User = get_user_model()


# Category Serializer: 
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'



# Course Serializer: 
class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course 
        fields = '__all__'



# Enrollment Serializer: 
class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment 
        fields = '__all__'



# Assignment Serializer: 
class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment 
        fields = '__all__'




# Submission Serializer: 
class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission 
        fields = '__all__'



# Sponsorship Serializer: 
class SponsorshipSerializer(ModelSerializer):
    class Meta:
        model = Sponsorship 
        fields = '__all__'



# Payment Serializer: 
class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment 
        fields = '__all__'



# Notification Serializer: 
class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification 
        fields = '__all__'



# User Serializer: 
class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'


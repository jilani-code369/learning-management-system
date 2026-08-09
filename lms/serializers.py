
from rest_framework.serializers import ModelSerializer

from .models import *


# CategorySerializer: 

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'



# CourseSerializer: 

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course 
        fields = '__all__'



# EnrollmentSerializer: 

class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment 
        fields = '__all__'




# AssignmentSerializer: 

class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment 
        fields = '__all__'




# SubmissionSerializer: 

class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission 
        fields = '__all__'




# SponsorshipSerializer: 

class SponsorshipSerializer(ModelSerializer):
    class Meta:
        model = Sponsorship 
        fields = '__all__'



# PaymentSerializer: 

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment 
        fields = '__all__'



# NotificationSerializer: 

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification 
        fields = '__all__'



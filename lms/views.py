from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

# Create your views here.


# Category API: 
class CategoryAPI(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
# Course API: 
class CourseAPI(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
#  Enrollment API: 
class EnrollmentAPI(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
    
# Assignment API: 
class AssignmentAPI(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    
    
    
# Submission API: 
class SubmissionAPI(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    
    
    
# Sponsorship API: 
class SponsorshipAPI(ModelViewSet):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
    


# Payment API: 
class PaymentAPI(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    

# Notification API: 
class NotificationAPI(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
    
# User API: 
class UserAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
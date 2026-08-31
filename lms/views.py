from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .pagination import *
from .models import *
from .serializers import *

# Create your views here.


# Category API: 
class CategoryAPI(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    #Pagination
    pagination_class = PaginationOf10               # Using custom pagination
    
    
# Course API: 
class CourseAPI(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    #Pagination
    pagination_class = PaginationOf20  
    
    # Overiding destroy method to handle protected relationship with course
    def destroy(self, request, *args, **kwargs):
        course = self.get_object()
        if Enrollment.objects.filter(course = course).exists():
            return Response({"detail":"Protected! Cannot delete, related with Enrollment."})
        if Sponsorship.objects.filter(course = course).exists():
            return Response({"detail":"Protected! Cannot delete, related with Sponsorship."})
      
        course.delete()
        return Response({"detail":"Course deleted successfully."})
    
    
#  Enrollment API: 
class EnrollmentAPI(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    
    #Pagination
    pagination_class = PaginationOf20  
    
    
    
# Assignment API: 
class AssignmentAPI(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    
    #Pagination
    pagination_class = PaginationOf30
    
    
# Submission API: 
class SubmissionAPI(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    
    #Pagination
    pagination_class = PaginationOf30  
    
    
# Sponsorship API: 
class SponsorshipAPI(ModelViewSet):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
    
    #Pagination
    pagination_class = PaginationOf10  
    

# Payment API: 
class PaymentAPI(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    #Pagination
    pagination_class = PaginationOf10  

# Notification API: 
class NotificationAPI(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
    #Pagination
    pagination_class = PaginationOf30  
    
    
# User API: 
class UserAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    #Pagination
    pagination_class = PaginationOf30  

    # Overiding destroy method to handle protected relationships 
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if Enrollment.objects.filter(student = user).exists():
            return Response({"detail": "Protected! Cannot delete, related to Enrollment."}, status = status.HTTP_400_BAD_REQUEST)
        if Sponsorship.objects.filter(sponsor=user).exists():
            return Response({"detail": "Protected! Cannot delete, related to Sponsorship."}, status = status.HTTP_400_BAD_REQUEST)
        if Sponsorship.objects.filter(student=user).exists():
            return Response({"detail": "Protected! Cannot delete, related to Sponsorship."}, status = status.HTTP_400_BAD_REQUEST)
                
        user.delete()
        return Response({"detail":"User deleted successfully!"}, status = status.HTTP_204_NO_CONTENT)
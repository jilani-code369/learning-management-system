from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import *
from .models import *
from .serializers import *
from .filters import *


# Create your views here.



# Category API: 
class CategoryAPI(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    #Pagination
    pagination_class = PaginationOf10               # Using custom pagination
    
    #Filter
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    
    
    
    
# Course API: 
class CourseAPI(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    #Pagination
    pagination_class = PaginationOf20  
    
    #Filter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CourseFilter                                                  # Using custom filter to have 'less than' and 'greater than' feature for 'price' field
    ordering_fields = ['id', 'price']
    
    
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
    
    #Filter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EnrollmentFilter                                  # Using custom filter to implement 'less than' and 'greater than' feature for 'progress' field
    ordering_fields = ['id', 'progress']
    
    
    
    
# Assignment API: 
class AssignmentAPI(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    
    #Pagination
    pagination_class = PaginationOf30
    
    #Filtering
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AssignmentFilter                                          # Using custom filter to have 'less than' and 'greater than' feature for 'total_marks' and 'deadline' field
    ordering_fields = ['id', 'total_marks']

    
    
    
# Submission API: 
class SubmissionAPI(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    
    #Pagination
    pagination_class = PaginationOf30  
    
    #Filter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SubmissionFilter                                              # Using custom filter to have 'less than' and 'greater than' feature for 'marks_obtained' field
    ordering_fields = ['id', 'marks_obtained']

    
    
    
# Sponsorship API: 
class SponsorshipAPI(ModelViewSet):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer
    
    #Pagination
    pagination_class = PaginationOf10  
    
    #Filter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SponsorshipFilter                                        # Using custom filter to have 'less than' and 'greater than' feature for 'amount' field
    ordering_fields = ['id', 'amount']
    
    
    

# Payment API: 
class PaymentAPI(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    #Pagination
    pagination_class = PaginationOf10  
    
    #Filter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'payer', 'payment_status']
    ordering_fields = ['id', 'amount']
    
    
    

# Notification API: 
class NotificationAPI(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
    #Pagination
    pagination_class = PaginationOf30  
    
    #Filter
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['title']
    filterset_fields = ['sender', 'notification_type', 'is_read']
    ordering_fields = ['id', 'sent_at']
    
    
    
       
# User API: 
class UserAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    #Pagination
    pagination_class = PaginationOf30 
    
    #Filter
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_class = UserFilter                                                                        # Using custom filter to have 'less than' and 'greater than' feature for 'dob' field
    ordering_fields = ['id', 'username', 'dob'] 
    

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
    
    
    

from django_filters import FilterSet
from .models import *


# Course filter: 
class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {'title': ['icontains'], 'category': ['exact'], 'instructor' : ['exact'], 'difficulty_level':['exact'],  'price':['gt', 'lt'] }        # icontains for title, gt & lt for price
        
        
# Enrollment filter:
class EnrollmentFilter(FilterSet):
    class Meta:
        model = Enrollment
        fields = { 'student':['exact'], 'course':['exact'], 'enrollment_status':['exact'], 'progress':['gt', 'lt']  }                                 # gt & lt for progress
        
        
# Assignment filter:
class AssignmentFilter(FilterSet):
    class Meta:
        model = Assignment
        fields = { 'title':['icontains'],  'course':['exact'], 'total_marks':['gt', 'lt'], 'deadline':['gt', 'lt'] }                                # icontains for title, gt & lt for total_marks and deadline
        
        
# Submission filter:
class SubmissionFilter(FilterSet):
    class Meta:
        model = Submission
        fields = { 'assignment':['exact'],  'student':['exact'], 'submission_status':['exact'], 'marks_obtained':['gt', 'lt'] }                   # gt & lt for marks_obtained
        
        
# Sponsorship filter:
class SponsorshipFilter(FilterSet):
    class Meta:
        model = Sponsorship
        fields = { 'organization_name':['icontains'], 'sponsor':['exact'],  'student':['exact'], 'course':['exact'], 'sponsorship_status':['exact'],  'amount':['gt', 'lt'] }            # icontains for organization_name, gt & lt for amount
    
    
    
    
# User filter:
class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = { 'username':['icontains'], 'first_name':['icontains'],  'last_name':['icontains'], 'email':['icontains'], 'dob':['gt', 'lt'] }            # icontains for all, gt & lt for dob
    

        
   
from django.urls import path 

from .views import *


urlpatterns = [
    path('category/', CategoryAPI.as_view({"get":"list", "post":"create"})),
    path('category/<pk>/', CategoryAPI.as_view({"get":"retrieve", "put":"update", "patch":"partial_update", "delete":"destroy"})),
    path('course/', CourseAPI.as_view({"get":"list", "post":"create"})),
    path('course/<pk>/', CourseAPI.as_view({"get":"retrieve", "put":"update", "patch":"partial_update", "delete":"destroy"})),
    path('enrollment/', EnrollmentAPI.as_view({"get":"list", "post":"create"})),
    path('enrollment/<pk>/', EnrollmentAPI.as_view({"get":"retrieve", "put":"update", "patch":"partial_update", "delete":"destroy"})),    
    path('assignment/', AssignmentAPI.as_view({"get":"list", "post":"create"})),
    path('assignment/<pk>/', AssignmentAPI.as_view({"get":"retrieve", "put":"update", "patch":"partial_update", "delete":"destroy"})),
    path('submission/', SubmissionAPI.as_view({"get":"list", "post":"create"})),
    path('submission/<pk>/', SubmissionAPI.as_view({"get":"retrieve", "put":"update", "patch":"partial_update", "delete":"destroy"})),
    path('sponsorship/', SponsorshipAPI.as_view({"get":"list", "post":"create"})),
    path('sponsorship/<pk>/', SponsorshipAPI.as_view({"get":"retrieve", "put":"update", "patch":"partial_update", "delete":"destroy"})),
    path('payment/', PaymentAPI.as_view({"get":"list", "post":"create"})),
    path('payment/<pk>/', PaymentAPI.as_view({"get":"retrieve", "put":"update", "patch":"partial_update", "delete":"destroy"})),
    path('notification/', NotificationAPI.as_view({"get":"list", "post":"create"})),
    path('notification/<pk>/', NotificationAPI.as_view({"get":"retrieve", "put":"update", "patch":"partial_update", "delete":"destroy"})),
      
    
]
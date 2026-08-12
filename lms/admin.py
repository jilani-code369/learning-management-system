from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

# Register your models here.


# Category Admin
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ["id", "name"]
    list_editable = []
    list_display_links = ["id", "name"]
    list_filter= []
    list_per_page = 10
    search_fields = ["name"]


# Course Admin
@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ["id", "title", "description", "instructor", "price", "syllabus", "difficulty_level"]
    list_editable = ["price", "difficulty_level"]
    list_display_links = ["id", "title"]
    list_filter= ["difficulty_level"]
    list_per_page = 10
    search_fields = ["title"]


# Enrollment Admin
@admin.register(Enrollment)
class EnrollmentAdmin(ModelAdmin):
    list_display = ["id", "course", "student", "enrollment_status", "progress", "enrolled_at"]
    list_editable = ["progress", "enrollment_status"]
    list_display_links = ["id", "course"]
    list_filter= ["enrollment_status"]
    list_per_page = 10
    search_fields = ["course__title", "student__username"]       # 'course__title' and 'student__username' is used because course and student are FKs



# Assignment Admin
@admin.register(Assignment)
class AssignmentAdmin(ModelAdmin):
    list_display = ["id", "course", "title", "description", "total_marks", "deadline"]
    list_editable = ["total_marks", "deadline"]
    list_display_links = ["id", "course", "title"]
    list_filter= ["course"]
    list_per_page = 10
    search_fields = ["course__title", "title"]
    
    

# Submission Admin
@admin.register(Submission)
class SubmissionAdmin(ModelAdmin):
    list_display = ["id", "assignment", "student", "answer_file", "answer_text", "submission_status", "marks_obtained", "submitted_at"]
    list_editable = ["marks_obtained"]
    list_display_links = ["id", "assignment"]
    list_filter= ["submission_status"]
    list_per_page = 10
    search_fields = ["assignment__title", "student__username"]



# Sponsorship Admin
@admin.register(Sponsorship)
class SponsorshipAdmin(ModelAdmin):
    list_display = ["id", "sponsor", "organization_name", "student", "course", "amount", "sponsorship_status", "funded_at"]
    list_editable = ["amount", "sponsorship_status"]
    list_display_links = ["id", "sponsor"]
    list_filter= ["sponsorship_status"]
    list_per_page = 10
    search_fields = ["sponsor__username", "organization_name"]



# Payment Admin
@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ["id", "course", "payer", "amount", "payment_method", "payment_status", "transaction_id", "payment_date"]
    list_editable = ["payment_status"]
    list_display_links = ["id", "course"]
    list_filter= ["payment_status"]
    list_per_page = 10
    search_fields = ["payer__username", "course__title"]


# Notification Admin
@admin.register(Notification)
class NotificationAdmin(ModelAdmin):
    list_display = ["id", "title", "description", "sender", "receiver", "notification_type", "is_read", "sent_at"]
    list_editable = ["is_read", "notification_type"]
    list_display_links = ["id", "title"]
    list_filter= ["is_read"]
    list_per_page = 10
    search_fields = ["title", "sender__username", "receiver__username"]
    
    
    


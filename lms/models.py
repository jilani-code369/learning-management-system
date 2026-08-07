from django.db import models
from django.contrib.auth import get_user_model
import uuid    # to generate random string for transaction id

# Create your models here.


# 1. User Model
User = get_user_model()


# 2. Course
class Course(models.Model):
    DIFFICULTY_CHOICES = (
        ("beginner", "BEGINNER"),
        ("intermediate", "INTERMEDIATE"),
        ("advanced", "ADVANCED")
    )

    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null =True)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    price = models.DecimalField(max_digits=10, decimal_places = 2)
    syllabus = models.TextField(blank=True, null =True)
    difficulty_level = models.CharField(max_length=20, choices = DIFFICULTY_CHOICES, default = "beginner")
    course_image = models.ImageField(upload_to = 'images/', blank=True, null =True)       # to upload the image/thumbnail of courses
    created_at = models.DateTimeField(auto_now_add = True)              # this will store the date when table is first created
    updated_at = models.DateTimeField(auto_now = True)                  # this will change the date on every update in the table 



# 3. Enrollment
class Enrollment(models.Model):
    STATUS_CHOICES = (
        ("enrolled", "ENROLLED"),
        ("completed", "COMPLETED"),
        ("dropped", "DROPPED")
    )
    student = models.ForeignKey(User, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    enrollment_status = models.CharField(max_length=50, choices = STATUS_CHOICES, default = "enrolled")
    progress = models.IntegerField(blank=True, null =True)
    enrolled_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    # To prevent enrolling in one course twice (avoid duplication):
    class Meta:
        unique_together = ("student", "course")


# 4. Assignment
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    total_marks = models.IntegerField()
    deadline = models.DateTimeField()        # the deadline will be manually set by the instructor
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
        


# 5. Submission
class Submission(models.Model):
    SUBMISSION_STATUS = (
        ("pending", "PENDING"), 
        ("evaluated", "EVALUATED"),
        ("rejected", "REJECTED")
    )
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_file = models.FileField(upload_to = 'files/')          # to upload answer file like: pdf or .py
    answer_text = models.TextField(null=True, blank=True)
    submission_status = models.CharField(max_length=20, choices = SUBMISSION_STATUS, default="pending")
    marks_obtained = models.IntegerField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    # To prevent submitting twice to the same assignment (avoid duplication)
    class Meta:
        unique_together = ("assignment", "student")
        
    

# 6. Sponsorship
class Sponsorship(models.Model):
    SPONSORSHIP_STATUS = (
        ("pending", "PENDING"),
        ("approved", "APPROVED"),
        ("finished", "FINISHED")
    )
    sponsor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sponsorship_given')             # related_name is used bec there is two field pointing to the same FK model
    organization_name = models.CharField(max_length=100)
    sponsored_student = models.OneToOneField(User, on_delete=models.PROTECT, related_name='sponsorship_received')    # One-to-One Field is used to avoid giving sponsorship to same student twice
    sponsored_course = models.ForeignKey(Course, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    sponsorship_status = models.CharField(max_length=20, choices=SPONSORSHIP_STATUS, default="pending")
    funded_at = models.DateTimeField(null=True, blank=True)     # this will be the date when funding is approved not when the sponsorship table is created. User will manually enter it.
    updated_at = models.DateTimeField(auto_now = True)
          

# 7. Payment
class Payment(models.Model):
    PAYMENT_METHOD=(
        ("cash", "CASH"),
        ("online", "ONLINE")
    )
    
    PAYMENT_STATUS = (
        ("pending", "PENDING"), 
        ("paid", "PAID"),
        ("failed", "FAILED")
    )
    
    course = models.ForeignKey(Course, on_delete=models.PROTECT)           # it says, which course you are paying for
    payer = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    payment_method = models.CharField(max_length=20, choices = PAYMENT_METHOD, default = "cash")
    payment_status = models.CharField(max_length=20, choices = PAYMENT_STATUS, default="pending")
    transaction_id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False)   # uuid.uuid4 is used to generate random. UUIDField to store 128-bit universally unique identifier
    payment_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)     
    updated_at = models.DateTimeField(auto_now = True)
           


# 8. Notification
class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ("informative", "INFORMATIVE"), 
        ("warning", "WARNING"),
        ("system", "SYSTEM")
    )
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete= models.CASCADE, related_name="sent_notifications")
    receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'received_notifications')
    notification_type = models.CharField(max_length=20, choices = NOTIFICATION_TYPES, default = "informative")
    is_read= models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    
    
    

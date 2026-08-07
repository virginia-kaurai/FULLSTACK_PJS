from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db import models
from django.utils import timezone
from django.conf import settings




class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", "admin")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self.create_user(
            email=email,
            password=password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("teacher", "Teacher"),
        ("student", "Student"),
    )

    email = models.EmailField(
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_verified = models.BooleanField(
        default=False
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "first_name",
        "last_name"
    ]

    def __str__(self):
        return self.email

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    slogan = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Class(models.Model):


    class ClassObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='active')
        
    name =models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    population = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in months")
    created_at = models.DateTimeField(default=timezone.now)
    options= (
        ('active', 'active'),
        ('graduated', 'graduated'),
    )
    status= models.CharField(max_length=20, choices=options, default='active')


    objects = models.Manager() # default manager
    class_objects = ClassObject() # custom manager


    class Meta:
        ordering = ['-created_at']
        

    def __str__(self):
        return self.name


class ClassDetail(models.Model):
    name = models.ForeignKey(Class, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    staff_number = models.CharField(max_length=20, primary_key=True)
    Experience = models.IntegerField(help_text="Experience in years")
    Qualification = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
         null=True,
    blank=True
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    Registration_number = models.CharField(max_length=20 , primary_key=True) 
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    Home_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
             null=True,
    blank=True
        )
    

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    choices = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )
    status = models.CharField(max_length=10, choices=choices)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"        
class Results(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student.name} - {self.subject} - {self.marks}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student.name} - {self.class_name.name} - {self.enrollment_date}"       
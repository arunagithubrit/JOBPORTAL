from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    user_type_choices=[
        ('jobseeker', 'jobseeker'),
        ('company' ,'company'),
    ]
    user_type=models.CharField(max_length=50,choices=user_type_choices,default='jobseeker')
    phone=models.CharField(max_length=10)

class User(CustomUser):
    
    address=models.CharField(max_length=200,null=True)


class Company(CustomUser):
    company_name=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    address=models.CharField(max_length=600)
    company_logo=models.ImageField(upload_to="images")
    office_location=models.CharField(max_length=500)
    pin=models.PositiveIntegerField()
    website=models.URLField(max_length=200, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)


class JobCategory(models.Model):
    options=(
        ("IT","IT"),
        ("NON-IT","NON-IT"),
        ("OTHERS","OTHERS"),
        ("NONE","NONE"),
        
    )
    

    name=models.CharField(max_length=200,choices=options,default="NONE")
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.name
    

class JobDescription(models.Model):
    openings=models.CharField(max_length=100)
    requirements=models.CharField(max_length=300)
    experience=models.CharField(max_length=100)
    job_type=models.CharField(max_length=100)
    salary=models.CharField(max_length=100)
    schedule=models.CharField(max_length=100)
    work_location=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    is_active=models.BooleanField(default=True)


class Job(models.Model):
    title=models.CharField(max_length=250)
    category=models.ForeignKey(JobCategory,on_delete=models.CASCADE)
    posted_on=models.DateTimeField(auto_now_add=True)
    closing_on=models.DateTimeField(auto_now_add=True)
    contact_email=models.EmailField()
    brief_description=models.ForeignKey(JobDescription,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.title


class Application(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    options=(
        ("male","male"),
        ("female","female"),
        ("none","none"),
        
    )
    gender=models.CharField(max_length=200,choices=options,default="none")
    resume=models.FileField(null=True,blank=True,upload_to="filesfolder")
    options=(
        ("higher secondary","higher secondary"),
        ("post graduation","post graduation"),
        ("graduation","graduation"),
        ("none","none"),


        
    )
    qualifications=models.CharField(max_length=200,choices=options,default="none")
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=10)
    job_applied=models.ForeignKey(Job,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    is_active=models.BooleanField(default=True)

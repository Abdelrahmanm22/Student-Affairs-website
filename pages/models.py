from django.db import models
# Create your models here.
# class Login(models.Model):
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)


class Student(models.Model):
    dept = [
    ('DS','DS'),
    ('CS','CS'),
    ('IS','IS'),
    ('IT','IT'),
    ('AI','AI'),
    ]
    L  = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        
    ]
    G=[
        ('Male','Male'),
        ('Female','Female'),
    ]

    Name = models.CharField(max_length=50)
    StudentID = models.CharField(max_length=11)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=11)
    GPA = models.DecimalField(max_digits=3,decimal_places=2)
    Department = models.CharField(max_length=2, choices=dept)
    level = models.IntegerField( choices=L)
    Gender = models.CharField(max_length=20,choices=G)
    Date = models.DateField(blank=True,null=True)
    activation = models.BooleanField(default=False,null=True,blank=True)
    def __str__ (self):
        return self.StudentID


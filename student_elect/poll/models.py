from django.db import models
import datetime
from student_elect import settings

# Create your models here.

class Poll(models.Model):
    title = models.TextField(null=True)
    datecreated = models.DateTimeField(null = True, default=datetime.date.today())
    round = models.IntegerField(default=0, null=True)
    status = models.TextField(choices = (('Active', 'A'),('Inactive','I')), default = 'I')
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)

class Candidate(models.Model):
    firstname = models.TextField(null=True)
    lastname = models.TextField(null=True)
    status = models.TextField(choices = (('Active', 'A'),('Inactive','I')), default = 'A') 
    imagefile = models.ImageField(upload_to='candidates', default="default.png")
    poll = models.ForeignKey("Poll", on_delete=models.CASCADE)

class Vote(models.Model):
    round = models.IntegerField(null=True)
    candidate = models.ForeignKey("Candidate", on_delete=models.CASCADE)
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    poll = models.ForeignKey("Poll", on_delete=models.CASCADE)

class Student(models.Model):
    studentID = models.TextField(null=True)
    user = models.ForeignKey("account.User", on_delete=models.DO_NOTHING, null=True)

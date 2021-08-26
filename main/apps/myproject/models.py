from __future__ import unicode_literals
from functools import update_wrapper
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateTimeField, proxy
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Sources(models.Model):
    source_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class Candidates(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    target_date = models.DateTimeField()
    cover_letter_url = models.TextField()
    current_ctc = models.CharField(max_length=45)
    excepted_ctc = models.CharField(max_length=45)
    source = models.ForeignKey(Sources, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class Skills(models.Model):
    name = models.CharField(max_length=45)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Statuses(models.Model):
    interview_status = models.CharField(max_length=45)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Interviews(models.Model):
    round_number = models.IntegerField()
    round_date = models.DateTimeField()
    notes = models.TextField()
    decision = models.CharField(max_length=45)
    candidate_id = models.ForeignKey(Candidates, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Candidates_Skills(models.Model):
    candidates_id = models.ForeignKey(Candidates, on_delete=models.PROTECT)
    skills_id = models.ForeignKey(Skills, on_delete=models.PROTECT)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)    

class Employment_Types(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Interviewers(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    interview_id = models.ForeignKey(Interviews, on_delete=models.PROTECT)

class Positions(models.Model):
    position_name = models.CharField(max_length=45)
    description = models.TextField()
    location = models.CharField(max_length=45)
    employment_type = models.ForeignKey(Employment_Types, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Interview_Positions(models.Model):
    position_id = models.ForeignKey(Positions, on_delete=models.PROTECT)
    interview_id = models.ForeignKey(Interviews, on_delete=models.PROTECT)

class Position_Skills(models.Model):
    position_id = models.ForeignKey(Positions, on_delete=models.PROTECT)
    skills_id = models.ForeignKey(Skills, on_delete=models.PROTECT)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)  
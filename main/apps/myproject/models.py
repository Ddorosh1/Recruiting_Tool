from __future__ import unicode_literals
from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Source(models.Model):
    source_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class Candidate(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    target_date = models.DateTimeField()
    cover_letter_url = models.TextField()
    current_ctc = models.CharField(max_length=45)
    excepted_ctc = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    # source = models.ForeignKey(Source, related_name="sources")


class Skill(models.Model):
    name = models.CharField(max_length=45)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Status(models.Model):
    interview_status = models.CharField(max_length=45)

class Interview(models.Model):
    round_number = models.IntegerField()
    round_date = models.DateTimeField()
    notes = models.TextField()
    decision = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # candidate_id = models.ForeignKey(Candidate, related_name='candidates')

from django.db import models
from django.utils import timezone


class Guide (models.Model):
  trackingNumber = models.CharField(max_length = 15, unique = True)
  origin = models.CharField(max_length = 100)
  destination = models.CharField(max_length = 100)
  createdAt = models.DateTimeField(default = timezone.now)
  updatedAt = models.DateTimeField (auto_now = True)
  currentStatus = models.CharField(max_length = 20)


class StatusHistory (models.Model):
  guideid = models.IntegerField()
  status = models.CharField(max_length = 20)
  timestamp = models.DateTimeField(default = timezone.now)
  updateBy = models.CharField(max_length = 20)


class User (models.Model):
  name = models.CharField(max_length = 50)
  email = models.CharField(max_length = 50)
  password = models.CharField(max_length = 20)
  createAt = models.DateTimeField(default = timezone.now)
  updateAt = models.DateTimeField(auto_now = True)

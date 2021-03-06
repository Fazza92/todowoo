from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


class Todo(models.Model):
  name = models.CharField(max_length=100)
  memo = models.TextField(blank=True)
  datecompleted = models.DateTimeField(null=True)
  created = models.DateTimeField(auto_now_add=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
  

from django.db import models

# Create your models here.

class Elements(models.Model):
  element = models.CharField(max_length=20)
  symbol = models.CharField(max_length=5)
  atomic_no = models.IntegerField()
  mass_no = models.FloatField()
  group = models.IntegerField()
  kind = models.CharField(max_length=30)
  
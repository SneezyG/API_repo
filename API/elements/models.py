from django.db import models
from datetime import datetime
# Create your models here.


date = datetime.now()
date = date.strftime("%m/%d/%Y, %H:%M:%S")

class Elements(models.Model):
  element = models.CharField(max_length=20)
  symbol = models.CharField(max_length=5)
  atomic_no = models.IntegerField()
  mass_no = models.FloatField()
  group = models.IntegerField()
  kind = models.CharField(max_length=30)
  
  def __str__(self):
     return self.element
  
  
class AllElements(models.Model):
  atomic_no = models.CharField(max_length=200, default='')
  element = models.CharField(max_length=200, default='')
  symbol = models.CharField(max_length=200, default='')
  atomic_mass = models.CharField(max_length=200, default='')
  neurons = models.CharField(max_length=200, default='')
  protons = models.CharField(max_length=200, default='')
  Electrons = models.CharField(max_length=200, default='')
  period = models.CharField(max_length=200, default='')
  group = models.CharField(max_length=200, default='')
  phase = models.CharField(max_length=200, default='')
  radioactive = models.BooleanField()
  natural = models.BooleanField()
  metal = models.BooleanField()
  Nonmetal = models.BooleanField()
  metalloid = models.BooleanField()
  kind = models.CharField(max_length=200, default='')
  atomic_radius = models.CharField(max_length=200, default='')
  eletro_negativity = models.CharField(max_length=200, default='')
  ionization_Energy = models.CharField(max_length=200, default='')
  Density = models.CharField(max_length=200, default='')
  Melting_point = models.CharField(max_length=200, default='')
  Boiling_point = models.CharField(max_length=200, default='')
  isotopes = models.CharField(max_length=200, default='')
  discoverer = models.CharField(max_length=200, default='')
  year = models.CharField(max_length=200, default='')
  specific_heat = models.CharField(max_length=200, default='')
  shells = models.CharField(max_length=200, default='')
  valence_electron = models.CharField(max_length=200, default='')
  
  def __str__(self):
     return self.element


class constants(models.Model):
  constant = models.CharField(max_length=200)
  symbol = models.CharField(max_length=200)
  value = models.CharField(max_length=200)
  
  def __str__(self):
     return self.constant
     
     
def path(instance, filename):
  return 'user_{0}/{1}'.format(instance.id, filename)

     
class users(models.Model):
  user = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  mug_shot = models.ImageField(upload_to=path, null=True)
  project_key = models.CharField(max_length=500)
  secret_key = models.CharField(max_length=500)
  mail = models.EmailField(max_length=300, null=True)
  project_name = models.CharField(max_length=200, default="")
  user_age = models.CharField(max_length=200, default= date)
  
  def __str__(self):
     return self.users
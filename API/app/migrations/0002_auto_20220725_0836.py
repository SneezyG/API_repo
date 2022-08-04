# Generated by Django 4.0.3 on 2022-07-25 07:36

from django.db import migrations
import csv
import os
from dotenv import load_dotenv
from django.db import transaction
from django.db import IntegrityError
from dotenv import load_dotenv

load_dotenv()

def convert(value):
  return value == 'yes'

def load(apps, schema_editor):
  Element = apps.get_model('app', 'Element')
  Chemical = apps.get_model('app', 'ChemicalConstant')
  Physical = apps.get_model('app', 'PhysicalConstant')
  Particle = apps.get_model('app', 'Particle')
  
  
  
  
  elem = open(os.getenv('element'))
  reader1 = csv.reader(elem)
  for atomic, element, symbol, mass, neuron, proton, electron, period, group, phase, radio, natural, metal, nonmetal, metalloid, kind, radius, negativity, ionization, density, mp, bp, isotope, discoverer, year, heat, shell, valence in reader1:
    try:
      with transaction.atomic():
        record = Element(atomic_no=atomic, element=element, symbol=symbol, atomic_mass=mass, neurons=neuron, protons=proton, Electrons=electron, period=period, group=group, phase=phase, radioactive=convert(radio), natural=convert(natural), metal=convert(metal), Nonmetal=convert(nonmetal), metalloid=convert(metalloid), kind=kind, atomic_radius=radius, eletro_negativity=negativity, ionization_Energy=ionization, Density=density, Melting_point=mp, Boiling_point=bp, isotopes=isotope, discoverer=discoverer, year=year, specific_heat=heat, shells=shell, valence_electron=valence)
        record.save()
    except IntegrityError:
      record.delete()
     
  elem.close()
  
  
  chem= open(os.getenv('chem'))
  reader2 = csv.reader(chem)
  for constant, symbol, value in reader2:
    try:
      with transaction.atomic():
        record = Chemical(constant=constant, symbol=symbol, value=value)
        record.save()
    except IntegrityError:
      record.delete()
      
  chem.close()
  
  
  phy = open(os.getenv('phy'))
  reader3 = csv.reader(phy)
  for name, value, unit, uncertainty in reader3:
    try:
      with transaction.atomic():
        record = Physical(name=name, value=value, unit=unit, uncertainty=uncertainty)
        record.save()
    except IntegrityError:
      record.delete()
      
  phy.close()
  
  
  part = open(os.getenv('particle'))
  reader4 = csv.reader(part)
  for name, kind, spin, charge, mass in reader4:
    try:
      with transaction.atomic():
        record = Particle(name=name, kind=kind, spin=spin, charge=charge, mass=mass)
        record.save()
    except IntegrityError:
      record.delete()
      
  part.close()
  
  
 
 
 
  
def reverse_load(apps, schema_editor):
  Element = apps.get_model('app', 'Element')
  Chemical = apps.get_model('app', 'ChemicalConstant')
  Physical = apps.get_model('app', 'PhysicalConstant')
  Particle = apps.get_model('app', 'Particle')
  
  Element.objects.all().delete()
  Chemical.objects.all().delete()
  Physical.objects.all().delete()
  Particle.objects.all().delete()



class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
      migrations.RunPython(load, reverse_load),
    ]

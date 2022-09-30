

from django.forms import ModelForm
from .models import Element, ChemicalConstant, PhysicalConstant, Particle


class ElementForm(ModelForm):
  """
  form input generated for elements mutations.
  """
  class Meta:
    model = Element
    fields = ['name','discoverer', "year",]
    
    
class ChemicalForm(ModelForm):
  """
  form input generated for chemical-constants  mutations.
  """
  class Meta:
    model = ChemicalConstant
    fields = ['name', 'value',]
    
    
class PhysicalForm(ModelForm):
  """
  form input generated for physical-constants mutations.
  """
  class Meta:
    model = PhysicalConstant
    fields = ['name', 'value',]
    
    
class ParticleForm(ModelForm):
  """
  form input generated for particles mutations.
  """
  class Meta:
    model = Particle
    fields = ['name', 'kind', 'mass']
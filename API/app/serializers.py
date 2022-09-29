
from .models import Element, ChemicalConstant, PhysicalConstant, Particle
from rest_framework import serializers
from graphene_django import DjangoObjectType

  
        
"""
serializers class for restfull api endpoint.
"""
class ElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Element
        fields = "__all__"
        
        
class ChemicalConstantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChemicalConstant
        fields = "__all__"
        

class PhysicalConstantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhysicalConstant
        fields = "__all__"
        
        
class ParticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Particle
        fields = "__all__"
       
       
       
       



"""
serializers class for graphql api endpoint.
"""
class ElementType(DjangoObjectType):
  class Meta:
    model = Element
    field = "__all__"

class ChemicalConstantType(DjangoObjectType):
  class Meta:
    model = ChemicalConstant
    field = "__all__"
    
class PhysicalConstantType(DjangoObjectType):
  class Meta:
    model = PhysicalConstant
    field = "__all__"
    
class ParticleType(DjangoObjectType):
  class Meta:
    model = Particle
    field = "__all__"       
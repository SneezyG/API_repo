
import graphene
from graphene_django import DjangoObjectType
from django.http import JsonResponse
from .models import Element, ChemicalConstant, PhysicalConstant, Particle




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



class Query(graphene.ObjectType):
  
  element = graphene.Field(ElementType, name=graphene.String(required=True))
  
  chemicalconstant = graphene.Field(ChemicalConstantType, name=graphene.String(required=True))
  
  physicalconstant = graphene.Field(PhysicalConstantType, name=graphene.String(required=True))
  
  particle = graphene.Field(ParticleType, name=graphene.String(required=True))
  
   
  def resolve_element(root, info, name):
    try:
      return Element.objects.get(element=name)
    except Element.DoesNotExist:
      return None
  
  def resolve_chemicalconstant(root, info, name):
    try:
      return ChemicalConstant.objects.get(constant=name)
    except ChemicalConstant.DoesNotExist:
      return None

  def resolve_physicalconstant(root, info, name):
    try:
      return PhysicalConstant.objects.get(name=name)
    except PhysicalConstant.DoesNotExist:
      return None

  def resolve_particle(root, info, name):
    try:
      return Particle.objects.get(name=name)
    except Particle.DoesNotExist:
      return None

schema = graphene.Schema(query=Query)


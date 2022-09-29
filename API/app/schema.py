
import graphene
from .models import Element, ChemicalConstant, PhysicalConstant, Particle
from app.serializers import ElementType, ChemicalConstantType, PhysicalConstantType, ParticleType




class Query(graphene.ObjectType):
  
  element = graphene.Field(ElementType, name=graphene.String(required=True))
  
  chemicalconstant = graphene.Field(ChemicalConstantType, name=graphene.String(required=True))
  
  physicalconstant = graphene.Field(PhysicalConstantType, name=graphene.String(required=True))
  
  particle = graphene.Field(ParticleType, name=graphene.String(required=True))
  
   
  def resolve_element(root, info, name):
    try:
      return Element.objects.get(name=name)
    except Element.DoesNotExist:
      return None
  
  def resolve_chemicalconstant(root, info, name):
    try:
      return ChemicalConstant.objects.get(name=name)
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


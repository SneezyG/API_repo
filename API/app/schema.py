
import graphene
from .models import Element, ChemicalConstant, PhysicalConstant, Particle
from .serializers import ElementType, ChemicalConstantType, PhysicalConstantType, ParticleType
from .form import ElementForm, ChemicalForm, PhysicalForm, ParticleForm
from graphene_django.forms.mutation import DjangoModelFormMutation




"""
below are queries created for for getting data out of all app models.
"""

class Query(graphene.ObjectType):
  
  # create query endpoint against model.
  element = graphene.Field(ElementType, name=graphene.String(required=True))
  
  chemicalconstant = graphene.Field(ChemicalConstantType, name=graphene.String(required=True))
  
  physicalconstant = graphene.Field(PhysicalConstantType, name=graphene.String(required=True))
  
  particle = graphene.Field(ParticleType, name=graphene.String(required=True))
  
   
  # create resolver for the query endpoint.
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







"""
below are mutations created for updating and changing data in all app models.
"""

class ElementMutation(DjangoModelFormMutation):
  element = graphene.Field(ElementType)
  
  @classmethod
  def mutate(cls, root, info, input):
    element = Element.objects.get(name=input.name)
    element.discoverer = input.discoverer
    element.year = input.year
    element.save()
    return ElementMutation(element=element)
  
  class Meta:
    form_class = ElementForm



class ChemicalMutation(DjangoModelFormMutation):
  chemical = graphene.Field(ChemicalConstantType)
  
  @classmethod
  def mutate(cls, root, info, input):
    chemical = ChemicalConstant.objects.get(name=input.name)
    chemical.value = input.value
    chemical.save()
    return ChemicalMutation(chemical=chemical)
    
  class Meta:
    form_class = ChemicalForm



class PhysicalMutation(DjangoModelFormMutation):
  physical = graphene.Field(PhysicalConstantType)
  
  @classmethod
  def mutate(cls, root, info, input):
    physical = PhysicalConstant.objects.get(name=input.name)
    physical.value = input.value
    physical.save()
    return PhysicalMutation(physical=physical)
  
  class Meta:
    form_class = PhysicalForm



class ParticleMutation(DjangoModelFormMutation):
  particle = graphene.Field(ParticleType)
  
  @classmethod
  def mutate(cls, root, info, input):
    particle = Particle.objects.get(name=input.name)
    particle.kind = input.kind
    particle.mass = input.mass
    particle.save()
    return ParticleMutation(particle=particle)
  
  class Meta:
    form_class = ParticleForm




# register my mutation class to a single class.
class Mutation(graphene.ObjectType):
    update_element = ElementMutation.Field()
    update_chemical = ChemicalMutation.Field()
    update_physical = PhysicalMutation.Field()
    update_particle = ParticleMutation.Field()
    


# register my queries and mutations.
schema = graphene.Schema(query=Query, mutation=Mutation)



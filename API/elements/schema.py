import graphene
from graphene_django import DjangoObjectType
from django.http import JsonResponse
from .models import Elements, AllElements, constants


class ElementsType(DjangoObjectType):
  class Meta:
    model = Elements
    field = "__all__"

class AllElementsType(DjangoObjectType):
  class Meta:
    model = AllElements
    field = "__all__"

class ConstantsType(DjangoObjectType):
  class Meta:
    model = constants
    field = "__all__"



class Query(graphene.ObjectType):
  element = graphene.Field(ElementsType, name=graphene.String(required=True))
  
  elementProps = graphene.Field(AllElementsType, name=graphene.String(required=True))
  
  constant = graphene.Field(ConstantsType, name=graphene.String(required=True))
  
  def resolve_element(root, info, name):
    try:
      return Elements.objects.get(element=name)
    except Elements.DoesNotExist:
      return None
   
  def resolve_elementProps(root, info, name):
    try:
      return AllElements.objects.get(element=name)
    except Elements.DoesNotExist:
      return None
  
  def resolve_constant(root, info, name):
    try:
      return constants.objects.get(constant=name)
    except Elements.DoesNotExist:
      return None

schema = graphene.Schema(query=Query)
import graphene
from graphene_django import DjangoObjectType
from django.http import JsonResponse
from .models import Elements


class ElementsType(DjangoObjectType):
  class Meta:
    model = Elements
    field = "__all__"

class Query(graphene.ObjectType):
  element = graphene.Field(ElementsType, name=graphene.String(required=True))
  
  def resolve_element(root, info, name):
    try:
      return Elements.objects.get(element=name)
    except Elements.DoesNotExist:
      return None


schema = graphene.Schema(query=Query)
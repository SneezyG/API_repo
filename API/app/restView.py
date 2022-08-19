
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import ElementSerializer, ChemicalConstantSerializer, PhysicalConstantSerializer, ParticleSerializer
from .models import Element, ChemicalConstant, PhysicalConstant, Particle
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


class ElementDetail(APIView):
     
  def get(self, request, element, format=None):
      context = {
            'request': request,
        }

      try:
         element = Element.objects.get(element=element)
      except Element.DoesNotExist:
          raise Http404
      serializer = ElementSerializer(element, context=context)
      return Response(serializer.data)
      
      
class ChemConstantDetail(APIView):
      
  def get(self, request, constant, format=None):
      context = {
            'request': request,
        }
      try:
         constant = ChemicalConstant.objects.get(constant=constant)
      except ChemicalConstant.DoesNotExist:
          raise Http404
      serializer = ChemicalConstantSerializer(constant, context=context)
      return Response(serializer.data)
      

class PhyConstantDetail(APIView):
      
  def get(self, request, name, format=None):
      context = {
                  'request': request,
              }
      try:
         constant = PhysicalConstant.objects.get(name=name)
      except PhysicalConstant.DoesNotExist:
          raise Http404
      serializer = PhysicalConstantSerializer(constant, context=context)
      return Response(serializer.data)
            

class ParticleDetail(APIView):
      
  def get(self, request, name, format=None):
      context = {
                 'request': request,
            }
      try:
         particle = Particle.objects.get(name=name)
      except Particle.DoesNotExist:
          raise Http404
      serializer = ParticleSerializer(particle, context=context)
      return Response(serializer.data)






class ElementViewSet(viewsets.ModelViewSet):

    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   


class ChemicalConstantViewSet(viewsets.ModelViewSet):
    queryset = ChemicalConstant.objects.all()
    serializer_class = ChemicalConstantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class PhysicalConstantViewSet(viewsets.ModelViewSet):
    queryset = PhysicalConstant.objects.all()
    serializer_class = PhysicalConstantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class ParticleViewSet(viewsets.ModelViewSet):
    queryset = Particle.objects.all()
    serializer_class = ParticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    


from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import ElementSerializer, ChemicalConstantSerializer, PhysicalConstantSerializer, ParticleSerializer
from .models import Element, ChemicalConstant, PhysicalConstant, Particle





class ElementViewSet(viewsets.ModelViewSet):
  
    """
    This is the elements api data endpoint.\n
    It return a list of all the available elements with all their attributes.\n
    It will also return the details of individual elements by appending the current url with the element name.
    """

    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   


class ChemicalConstantViewSet(viewsets.ModelViewSet):

    """
    This is the chemical constant api data endpoint.\n
    It return a list of all the available chemical constants with their attributes.\n
    It will also return the details of individual constant by appending the current url with the constant name.
    """    
    
    queryset = ChemicalConstant.objects.all()
    serializer_class = ChemicalConstantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class PhysicalConstantViewSet(viewsets.ModelViewSet):

    """
    This is the physical constant api data endpoint.\n
    It return a list of all the available physical constants with their attributes.\n
    It will also return the details of individual constant by appending the current url with the constant name.
    """    
      
    queryset = PhysicalConstant.objects.all()
    serializer_class = PhysicalConstantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class ParticleViewSet(viewsets.ModelViewSet):
  
    """
    This is the particle api data endpoint.\n
    It return a list of all the available particles with their attributes.\n
    It will also return the details of individual particle by appending the current url with the particle name.
    """    
    
    queryset = Particle.objects.all()
    serializer_class = ParticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    


from .models import Element, ChemicalConstant, PhysicalConstant, Particle
from rest_framework import serializers

        
        
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
       
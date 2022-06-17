
from elements.models import Elements, AllElements, constants
from rest_framework import serializers


class ElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Elements
        fields = "__all__"
        
        
class AllElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllElements
        fields = "__all__"
        
        
class constantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = constants
        fields = "__all__"
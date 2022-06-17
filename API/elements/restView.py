from rest_framework import viewsets
from rest_framework import permissions
from elements.serializers import ElementSerializer, AllElementSerializer, constantSerializer
from elements.models import Elements, AllElements, constants


class ElementViewSet(viewsets.ModelViewSet):

    queryset = Elements.objects.all()
    serializer_class = ElementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
 
class AllElementViewSet(viewsets.ModelViewSet):

    queryset = AllElements.objects.all()
    serializer_class = AllElementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   


class ConstantViewSet(viewsets.ModelViewSet):

    queryset = constants.objects.all()
    serializer_class = constantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
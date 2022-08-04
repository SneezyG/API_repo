
# from django.contrib import admin
import sys
import os
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework import routers
from app import restView
from django.views.decorators.csrf import csrf_exempt
from app.schema import schema
from rest_framework.urlpatterns import format_suffix_patterns

sys.path.append(os.path.abspath(os.path.join('..', 'elements')))




router = routers.DefaultRouter()
router.register(r'element', restView.ElementViewSet)
router.register(r'chemicalconstant', restView.ChemicalConstantViewSet)
router.register(r'physicalconstant', restView.PhysicalConstantViewSet)
router.register(r'particle', restView.ParticleViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(('app.urls', 'app'), namespace='apps')),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    
]





# from django.contrib import admin
import sys
import os
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework import routers
from elements import restView
from django.views.decorators.csrf import csrf_exempt
from elements.schema import schema

sys.path.append(os.path.abspath(os.path.join('..', 'elements')))




router = routers.DefaultRouter()
router.register(r'element', restView.ElementViewSet)
router.register(r'allElement', restView.AllElementViewSet)
router.register(r'constant', restView.ConstantViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', include(('elements.urls', 'elements'), namespace='elements')),
  
    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    
]

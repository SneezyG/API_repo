from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import restView


urlpatterns = [
  
    path('element/<str:element>/', restView.ElementDetail.as_view()),
    path('particle/<str:name>/', restView.ParticleDetail.as_view()),
    path('chemicalConstant/<str:constant>/', restView.ChemConstantDetail.as_view()),
    path('physicalConstant/<str:name>/', restView.PhyConstantDetail.as_view()),
  
  ]
  
urlpatterns = format_suffix_patterns(urlpatterns)
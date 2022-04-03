from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('guide/', views.guide, name='guide'),
  path('<str:element>/', views.data, name='data')
]
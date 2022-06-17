from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('verifyMail/', views.verifyMail, name='verifyMail'),
  path('create/', views.create, name='create'),
  path('createProject/', views.createProject, name='createProject'),
  path('login/', views.login, name='login'),
  path('forgetPass/', views.forgetPass, name='forgetPass'),
  path('changePass/', views.changePass, name='changePass'),
  path('upload/', views.upload, name='upload'),
]



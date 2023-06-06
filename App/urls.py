from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='Home'),
    path('Create/', Create, name='Create'),
    path('allProf/', allProf, name='allProf'),
    path('singleProf/<int:id>/', singleProf, name='singleProf'),
    path('deleteProf/<int:id>/', deleteProf, name='deleteProf'),
    path('updateProfile/<int:id>/', updateProfile, name='updateProfile'),

]

from django.urls import path
from .views import *

urlpatterns = [

    path('login/', log_in, name='login'),
    path('reg/', reg, name='reg'),
    path('log_out/', log_out, name='log_out'),

]

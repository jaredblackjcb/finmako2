from django.urls import path, include
from apps.calculator import views

app_name = 'calculator'

urlpatterns = [
    path('pmi/', views.pmi_calculator, name='pmi_calculator'),
    path('annuity/', views.annuity_calculator, name='annuity_calculator')
]
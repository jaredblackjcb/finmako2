from django.urls import path, include
from apps.backtester import views

app_name = 'backtester'

urlpatterns = [
    path('', views.backtester, name='backtester')
]
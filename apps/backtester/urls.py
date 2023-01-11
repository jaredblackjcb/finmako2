from django.urls import path, include
from apps.backtester import views
urlpatterns = [
    path('', views.backtester, name='backtester')
]
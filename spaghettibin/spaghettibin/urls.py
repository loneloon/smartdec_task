from rest_framework import routers
from django.urls import path, re_path, include


urlpatterns = [
    path('api/', include('api.urls', namespace='api')),
    path('', include('mainapp.urls', namespace='main')),
]

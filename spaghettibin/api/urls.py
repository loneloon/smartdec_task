from django.urls import path, re_path
import api.views as api

app_name = 'api'

urlpatterns = [
    path('', api.get_list, name='get_scripts'),
    path('read/<str:pk>/', api.read_script, name='read_script'),
    path('create/', api.create_script, name='create_script'),
    path('update/<str:pk>/', api.update_script, name='update_script'),
    path('delete/<str:pk>/', api.delete_script, name='delete_script'),
]

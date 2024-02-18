from django.urls import path, re_path
from apps.gamemodule import views

urlpatterns = [    
    path('', views.index, name='index'),
]
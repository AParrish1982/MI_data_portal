from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='MI_dashboard'),
    path('ngs_in_progress', views.ngs_in_progress, name='ngs_in_progress'),
]

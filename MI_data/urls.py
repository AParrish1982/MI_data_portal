from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.dashboard, name='MI_dashboard'),
    path('ngs_in_progress', views.ngs_in_progress, name='ngs_in_progress'),
    path('ngs_in_progress/<ordno>/', views.ngs_sample_in_progress, name='ngs_sample_in_progress'),
]

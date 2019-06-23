from django.conf import settings
from django.db import models
from django.utils import timezone
import plotly.plotly as py
import plotly.figure_factory as ff

# Create your models here.

class Ngs_in_progress(models.Model):
    ordno = models.CharField(verbose_name='ordno', max_length=12)
    name_fullname = models.TextField(verbose_name='Patient name')
    family_number = models.TextField(verbose_name='Family number')
    team = models.TextField(verbose_name='Team')
    disease = models.TextField(verbose_name='Investigation')
    profile = models.TextField(verbose_name='Profile')
    urg = models.BooleanField(verbose_name='Urgent?')
    received = models.DateField(verbose_name='Received')
    activated = models.DateField(verbose_name='Activated')
    fragmentation = models.DateField(verbose_name='Fragmentation date')
    fragmentation_batch = models.CharField(verbose_name='Fragmentation batch', max_length=7)
    library_prep = models.DateField(verbose_name='Library prep date')
    library_prep_batch = models.CharField(verbose_name='Library prep batch', max_length=7)
    library_completion = models.DateField(verbose_name='Library completion date')
    library_completion_batch = models.CharField(verbose_name='Library completion batch', max_length=7)
    reporting = models.DateField(verbose_name='Reporting batch date')
    reporting_batch = models.CharField(verbose_name='Reporting batch', max_length=7)
    report_generated = models.DateField(verbose_name='Report Generation date')
    status = models.CharField(verbose_name='Status', max_length=6)
    
    def __str__(self):
        return self.ordno


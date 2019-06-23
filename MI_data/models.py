from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Ngs_in_progress(models.Model):
    ordno = models.CharField(max_length=12)
    name_fullname = models.TextField()
    family_number = models.TextField()
    team = models.TextField()
    disease = models.TextField()
    profile = models.TextField()
    urg = models.BooleanField()
    received = models.DateField()
    activated = models.DateField()
    fragmentation = models.DateField()
    fragmentation_batch = models.CharField(max_length=7)
    library_prep = models.DateField()
    library_prep_batch = models.CharField(max_length=7)
    library_completion = models.DateField()
    library_completion_batch = models.CharField(max_length=7)
    reporting = models.DateField()
    reporting_batch = models.CharField(max_length=7)
    report_generated = models.DateField()
    status = models.CharField(max_length=6)

    def __str__(self):
        return self.ordno


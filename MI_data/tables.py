import django_tables2 as tables
from .models import Ngs_in_progress

# Create your models here.

class Ngs_in_progress_table(tables.Table):
    
    class Meta:
        model = Ngs_in_progress
        fields = ('ordno','name_fullname', 'family_number', 'team', 'disease', 'profile', 'urg', 'received', 'activated', 'fragmentation', 'fragmentation_batch', 'library_prep', 'library_prep_batch', 'library_completion', 'library_completion_batch', 'reporting', 'reporting_batch', 'report_generated', 'status')
        template_name = 'django_tables2/bootstrap-responsive.html'


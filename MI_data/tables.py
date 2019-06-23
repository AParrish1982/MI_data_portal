import django_tables2 as tables
from .models import Ngs_in_progress
from django_tables2.utils import A

# Create your models here.

class Ngs_in_progress_table(tables.Table):
    ordno = tables.Column(linkify=("ngs_sample_in_progress", {"ordno": tables.A("ordno")}))
    
    class Meta:
        model = Ngs_in_progress
        fields = ('ordno','name_fullname', 'family_number', 'team', 'disease', 'profile', 'urg', 'received', 'activated', 'fragmentation', 'fragmentation_batch', 'library_prep', 'library_prep_batch', 'library_completion', 'library_completion_batch', 'reporting', 'reporting_batch', 'report_generated', 'status')
        ordno = tables.LinkColumn('ordno', args=[A('ordno')])
        template_name = 'django_tables2/bootstrap-responsive.html'


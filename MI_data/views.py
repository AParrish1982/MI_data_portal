from django.shortcuts import render, get_object_or_404, redirect
from django_tables2 import RequestConfig
from .models import Ngs_in_progress
from .tables import Ngs_in_progress_table

# Create your views here.

def dashboard(request):
    return render(request, 'MI_data/dashboard.html', {})

def ngs_in_progress(request):
    table = Ngs_in_progress_table(Ngs_in_progress.objects.all())
    RequestConfig(request).configure(table)
# return render(request, 'MI_data/ngs_in_progress.html', {'table': table})
    ngs_in_progress = Ngs_in_progress.objects.all()
    return render(request, 'MI_data/ngs_in_progress.html', {'ngs_in_progress': ngs_in_progress})

def ngs_sample_in_progress(request, ordno):
    sample = get_object_or_404(Ngs_in_progress, ordno=ordno)
    return render(request, 'MI_data/ngs_sample_in_progress.html', {'sample': sample})
                    #ordno=Ngs_in_progress.ordno)
#return render(request, 'MI_data/ngs_sample_in_progress.html', {})

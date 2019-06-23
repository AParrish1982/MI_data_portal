from django.shortcuts import render
from django.utils import timezone
from .models import Ngs_in_progress

# Create your views here.

def dashboard(request):
    return render(request, 'MI_data/dashboard.html', {})

def ngs_in_progress(request):
    ngs_in_progress = Ngs_in_progress.objects.filter(received__lte=timezone.now()).order_by('activated')
    return render(request, 'MI_data/ngs_in_progress.html', {'ngs_in_progress':ngs_in_progress})

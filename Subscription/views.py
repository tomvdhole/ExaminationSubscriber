from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ParticipantForm
from .models import Participant
from .reports import SubscriptionReport
from openpyxl.writer.excel import save_virtual_workbook

# Create your views here.
def index(request):
    return render(request, 'Subscription/index.html', {})

def succes(request, saved):
    return render(request, 'Subscription/succes.html', {'saved': saved})

def subscribe(request):
    if request.method == 'GET':
        form = ParticipantForm()
        return render(request, 'Subscription/subscribe.html', {'form' : form})
    else:
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            participant.save()
            return redirect('succes', saved=participant.saved)
        else:
            return render(request, 'Subscription/subscribe.html', {'form' : form})

def reports(request):
    return render(request, 'Subscription/reports.html', {})

def download_report(request):
    report = SubscriptionReport()
    response = HttpResponse(save_virtual_workbook(report.create_reports()), content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Reports.xlsx'
    return response

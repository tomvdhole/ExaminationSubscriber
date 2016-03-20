from django.shortcuts import render, redirect
from .forms import ParticipantForm
from .models import Category, Participant

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
            participant = form.save(commit=False)
            participant.save()
            return redirect('succes', saved=participant.saved)
        else:
            return render(request, 'Subscription/subscribe.html', {'form' : form})

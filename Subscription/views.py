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
        print("get")
        form = ParticipantForm()
        return render(request, 'Subscription/subscribe.html', {'form' : form})
    else:
        print("post")
        form = ParticipantForm(request.POST)
        print("form created")
        if form.is_valid():
            participant = form.save()
            #participant.save_data()
            participant.save()
            print("object created")
            print("in view")
            print(participant.age)
            print(participant.number_of_red_ribbons)
            print(participant.category)
            print(participant.saved)
            print("uit view")


            return redirect('succes', saved=participant.saved)
        else:
            return render(request, 'Subscription/subscribe.html', {'form' : form})

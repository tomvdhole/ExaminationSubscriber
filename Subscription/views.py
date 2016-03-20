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
            saved = __save_data(form)
            #define_category
            return redirect('succes', saved=saved)
        else:
            return render(request, 'Subscription/subscribe.html', {'form' : form})


#Private methods
def __save_data(form):
    age = form.cleaned_data['age']
    grade = form.cleaned_data['grade']
    number_of_red_ribbons = form.cleaned_data['number_of_red_ribbons']
    saved = False

    if age == 7 and (number_of_red_ribbons == 0 or number_of_red_ribbons == 1):
        if number_of_red_ribbons == 0:
            category = Category.objects.get(type_of_competitors='Kids', examination_type='Form')
            saved = True
        if number_of_red_ribbons == 1:
            category = Category.objects.get(type_of_competitors='Kids', examination_type='Rhytm')
            saved = True

    return saved

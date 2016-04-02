from django import forms
from django.forms import extras
from .models import Participant

class ParticipantForm(forms.ModelForm):
    gsm = forms.RegexField(regex=r"^04[0-9]{8,8}$", error_messages={'invalid':'GSM nummer moet bestaan uit 10 nummers en het moet starten met 04!'}, label="Gsm")
    license_number = forms.RegexField(regex=r"^[0-9]{1,6}$", error_messages={'invalid':'Licentie nummer mag enkel bestaan uit maximum 6 cijfers!'}, label="Licentienummer")
    age = forms.RegexField(regex=r"^[0-9]{1,2}$", error_messages={'invalid': 'Leeftijd moet bestaan uit maximum 2 cijfers!'}, label="Leeftijd")
    date_till_license_is_valid= forms.DateField(widget = extras.SelectDateWidget(), label="Licentie geldigheids datum")

    class Meta:
        model = Participant
        fields = ['last_name',
                  'first_name',
                  'license_number',
                  'date_till_license_is_valid',
                  'grade',
                  'number_of_red_ribbons',
                  'age',
                  'gsm',
                  'email']

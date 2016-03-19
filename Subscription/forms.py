from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    gsm = forms.RegexField(regex=r"^04[0-9]{8,8}$", error_messages={'invalid':'GSM number must consists of 10 numbers and it must start with a 04!'})
    license_number = forms.RegexField(regex=r"^[0-9]{1,6}$", error_messages={'invalid':'License number may only consists of maximum 6 figures!'})
    age = forms.RegexField(regex=r"^[0-9]{1,2}$", error_messages={'invalid': 'Age must consists of a numerical value of maximum 2 figures!'})

    class Meta:
        model = Participant
        fields = ['last_name',
                  'first_name',
                  'gsm',
                  'email',
                  'license_number',
                  "grade",
                  "number_of_red_ribbons",
                  "age"]

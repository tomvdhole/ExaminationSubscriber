from django.db import models
from django.core.validators import RegexValidator

BELT_TO_GRADE = (("0e Kyu", "Witte gordel"), ("9e Kyu", "Witte gordel met zwart streepje"), ("9e Kyu", "Rode gordel"), ("8e Kyu", "Gele gordel"), ("7e Kyu", "Oranje gordel"), ("6e Kyu", "Groene gordel"), ("5e Kyu", "Blauwe gordel"), ("4e Kyu", "Blauwe gordel met wit streepje"), ("3e Kyu", "Bruine gordel"), ("2e Kyu", "Bruine gordel met wit streepje"),)
RED_RIBBONS = ((0, "0"), (1, "1"), (2, "2"),)
TYPE_OF_PARTICIPANTS = (("Beginners", "Beginners"), ("Advanced", "Gevorderden"), ("Kids", "Kinderen"), ("Youth", "Jeugd"),)
EXAMINATION_TYPE = (("Form", "Vorm"), ("Rhytm", "Ritme"), ("Official", "Officieel"),)

class Category(models.Model):
    type_of_participants = models.CharField(max_length=20, choices=TYPE_OF_PARTICIPANTS)
    examination_type = models.CharField(max_length=10, choices= EXAMINATION_TYPE)

    def __str__(self):
        return self.type_of_participants + " " + self.examination_type

class Participant(models.Model):
    last_name = models.CharField(max_length=30, verbose_name="Naam")
    first_name = models.CharField(max_length=30, verbose_name="Voornaam")
    gsm = models.CharField(max_length=10, validators=[RegexValidator(r"^04[0-9]{8}$", "GSM nummer moet bestaan uit 10 nummers en het moet starten met 04!")], verbose_name="Gsm")
    email = models.EmailField(verbose_name="Email")
    license_number = models.CharField(max_length=6, validators=[RegexValidator(r"^[0-9]{1,6}$", "Licentie nummer mag enkel bestaan uit maximum 6 cijfers!")], verbose_name="Licentienummer")
    date_till_license_is_valid = models.DateField(verbose_name="Licentie geldigheids datum")
    grade = models.CharField(max_length=6, choices=BELT_TO_GRADE, verbose_name="Graad")
    number_of_red_ribbons = models.PositiveSmallIntegerField(choices=RED_RIBBONS, verbose_name="Aantal rode lintjes")
    age = models.CharField(max_length=2, validators= [RegexValidator(r"^[0-9]{1,2}$", "Leeftijd moet bestaan uit maximum 2 cijfers!")], verbose_name="Leeftijd")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        self.__saved = False
        self.__save_data()
        if self.__saved == True:
            super().save(*args, **kwargs)

    #private method
    def __save_data(self):
        self.age = int(self.age)

        if self.age == 7 and (self.number_of_red_ribbons == 0 or self.number_of_red_ribbons == 1):
            if self.number_of_red_ribbons == 0:
                self.category = Category.objects.get(type_of_participants='Kids', examination_type='Form')
                self.__saved = True
            if self.number_of_red_ribbons == 1:
                self.category = Category.objects.get(type_of_participants='Kids', examination_type='Rhytm')
                self.__saved = True

        if (self.age >= 8 and self.age < 11) and (self.grade == "0e Kyu" or self.grade == "9e Kyu" or self.grade == "8e Kyu" or self.grade == "7e Kyu" or self.grade == "6e Kyu"):
            if self.number_of_red_ribbons == 0:
                self.category = Category.objects.get(type_of_participants='Kids', examination_type='Form')
                self.__saved = True
            if self.number_of_red_ribbons == 1:
                self.category = Category.objects.get(type_of_participants='Kids', examination_type='Rhytm')
                self.__saved = True
            if self.number_of_red_ribbons == 2:
                self.category = Category.objects.get(type_of_participants='Kids', examination_type='Official')
                self.__saved = True

        if (self.age >= 11 and self.age < 14) and (self.grade == "0e Kyu" or self.grade == "9e Kyu" or self.grade == "8e Kyu" or self.grade == "7e Kyu" or self.grade == "6e Kyu"):
            if self.number_of_red_ribbons == 0:
                self.Category = Category.objects.get(type_of_participants='Youth', examination_type='Form')
                self.__saved = True
            if self.number_of_red_ribbons == 1:
                self.category = Category.objects.get(type_of_participants='Youth', examination_type='Rhytm')
                self.__saved = True
            if self.number_of_red_ribbons == 2:
                self.category = Category.objects.get(type_of_participants='Youth', examination_type='Official')
                self.__saved = True

        if self.age >= 14 and (self.grade == "0e Kyu" or self.grade == "9e Kyu" or self.grade == "8e Kyu" or self.grade == "7e Kyu" or self.grade == "6e Kyu"):
            if self.number_of_red_ribbons == 0:
                self.Category = Category.objects.get(type_of_participants='Beginners', examination_type='Form')
                self.__saved = True
            if self.number_of_red_ribbons == 1:
                self.category = Category.objects.get(type_of_participants='Beginners', examination_type='Rhytm')
                self.__saved = True
            if self.number_of_red_ribbons == 2:
                self.category = Category.objects.get(type_of_participants='Beginners', examination_type='Official')
                self.__saved = True

        if self.grade == "5e Kyu" or self.grade == "4e Kyu" or self.grade == "3e Kyu" or self.grade == "2e Kyu":
            if self.number_of_red_ribbons == 0:
                self.Category = Category.objects.get(type_of_participants='Advanced', examination_type='Form')
                self.__saved = True
            if self.number_of_red_ribbons == 1:
                self.category = Category.objects.get(type_of_participants='Advanced', examination_type='Rhytm')
                self.__saved = True
            if self.number_of_red_ribbons == 2:
                self.category = Category.objects.get(type_of_participants='Advanced', examination_type='Official')
                self.__saved = True

    @property
    def saved(self):
        return self.__saved

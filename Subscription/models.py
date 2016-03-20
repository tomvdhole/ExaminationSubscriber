from django.db import models
from django.core.validators import RegexValidator

BELT_TO_GRADE = (("0e Kyu", "Witte gordel"), ("9e Kyu", "Witte gordel met zwart streepje"), ("9e Kyu", "Rode gordel"), ("8e Kyu", "Gele gordel"), ("7e Kyu", "Oranje gordel"), ("6e Kyu", "Groene gordel"), ("5e Kyu", "Blauwe gordel"), ("4e Kyu", "Blauwe gordel met wit streepje"), ("3e Kyu", "Bruine gordel"), ("2e Kyu", "Bruine gordel met wit streepje"), ("1e Kyu", "Bruine gordel met twee witte streepjes"), )
RED_RIBBONS = ((0, "0"), (1, "1"), (2, "2"),)
TYPE_OF_COMPETITORS = (("Beginners", "Beginners"), ("Advanced", "Gevorderden"), ("Kids", "Kinderen"), ("Youth", "Jeugd"),)
EXAMINATION_TYPE = (("Form", "Vorm"), ("Rhytm", "Ritme"), ("Official", "Officieel"),)

class Category(models.Model):
    type_of_competitors = models.CharField(max_length=20, choices=TYPE_OF_COMPETITORS)
    examination_type = models.CharField(max_length=10, choices= EXAMINATION_TYPE)

    def __str__(self):
        return self.type_of_competitors + " " + self.examination_type

class Participant(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    gsm = models.CharField(max_length=10, validators=[RegexValidator(r"^04[0-9]{8}$", "GSM number must consists of 10 numbers and it must start with a 0!")])
    email = models.EmailField()
    license_number = models.CharField(max_length=6, validators=[RegexValidator(r"^[0-9]{1,6}$", "License number may only consists of maximum 6 figures!")])
    grade = models.CharField(max_length=6, choices=BELT_TO_GRADE)
    number_of_red_ribbons = models.PositiveSmallIntegerField(choices=RED_RIBBONS)
    age = models.CharField(max_length=2, validators= [RegexValidator(r"^[0-9]{1,2}$", "Age must consists of a numerical value of maximum 2 figures!")])
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
        if self.age == '7' and (self.number_of_red_ribbons == 0 or self.number_of_red_ribbons == 1):
            if self.number_of_red_ribbons == 0:
                self.category = Category.objects.get(type_of_competitors='Kids', examination_type='Form')
                self.__saved = True
            if self.number_of_red_ribbons == 1:
                self.category = Category.objects.get(type_of_competitors='Kids', examination_type='Rhytm')
                self.__saved = True

    @property
    def saved(self):
        return self.__saved

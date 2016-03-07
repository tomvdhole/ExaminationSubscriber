from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

BELT_TO_GRADE = (
#!!!!! to check voor de groene streepjes !!!!!!
    ("0e Kyu", "Witte gordel"),
    ("0e Kyu", "Witte gordel met groen streepje"),
    ("0e Kyu", "Witte gordel met twee groene streepjes"),
    ("9e Kyu", "Witte gordel met zwart streepje"),
    ("9e Kyu", "Rode gordel"),
    ("8e Kyu", "Gele gordel"),
    ("7e Kyu", "Oranje gordel"),
    ("6e Kyu", "Groene gordel"),
    ("5e Kyu", "Blauwe gordel"),
    ("4e Kyu", "Blauwe gordel met wit streepje"),
    ("3e Kyu", "Bruine gordel"),
    ("2e Kyu", "Bruine gordel met wit streepje"),
    ("1e Kyu", "Bruine gordel met twee witte streepjes"),
)

RED_RIBBONS = (
    (0, "0"),
    (1, "1"),
    (2, "2"),
)

TYPE_OF_COMPETITORS = (
    ("Beginners", "Beginners"),
    ("Advanced", "Gevorderden"),
    ("Kids", "Kinderen"),
    ("Youth", "Jeugd"),
)

EXAMINATION_TYPE = (
    ("Form", "Vorm"),
    ("Rhytm", "Ritme"),
    ("Official", "Officieel"),
)

class Participant(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    license_number = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(
                r"^[0-9]{1,6}$",
                "License number may only consists of maximum 6 figures!"
            )
        ]
    )
    color_belt = models.CharField(max_length=6, choices=BELT_TO_GRADE)
    number_of_red_ribbons = models.PositiveSmallIntegerField(choices=RED_RIBBONS)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    type_of_competitors = models.CharField(max_length=20, choices=TYPE_OF_COMPETITORS)
    examination_type = models.CharField(max_length=10, choices= EXAMINATION_TYPE)

    def __str__(self):
        return self.type_of_competitors + " " + self.examination_type

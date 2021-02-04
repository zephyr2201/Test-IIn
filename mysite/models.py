from django.db import models
import datetime
import math


class Person(models.Model):
    iin = models.CharField(max_length=12, unique=True)

    @property
    def calculated_age(self):
        today = datetime.datetime.today()
        years = self.iin[:2]
        month = self.iin[2:4]
        days = self.iin[4:6]
        century = self.iin[6:7]
        if int(century) == 1 or int(century) == 2:
            years = '18' + years
        elif int(century) == 3 or int(century) == 4:
            years = '19' + years
        else:
            years = '20' + years
        iin_convert = f"{years}-{month}-{days}"
        iin_convert = datetime.datetime.strptime(iin_convert, "%Y-%m-%d")
        return math.floor((today - iin_convert).days / 365.25)

    def __str__(self):
        return self.iin

from django.db import models
from django.core.validators import MinLengthValidator


class Log(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    description = models.TextField()

    def __str__(self):
        return f'{self.date} {self.title}'

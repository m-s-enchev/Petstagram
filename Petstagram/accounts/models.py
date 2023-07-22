from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class PetstagramUser(AbstractUser):
    first_name = models.CharField(max_length=30,
                                  validators=[MinLengthValidator(2),
                                              RegexValidator(r'^[a-zA-Z]+$')])
    last_name = models.CharField(max_length=30,
                                 validators=[MinLengthValidator(2),
                                             RegexValidator(r'^[a-zA-Z]+$')])
    email = models.EmailField(unique=True)
    choices = [("male", "Male"), ("female", "Female"), ("do not show", "Do not show")]
    gender = models.CharField(choices=choices, max_length=11)
    picture = models.URLField()



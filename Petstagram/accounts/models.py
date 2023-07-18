from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class PetstagramUser(AbstractUser):
    first_name = models.CharField(max_length=30,
                                  validators=[MinLengthValidator(2),
                                              RegexValidator(regex='[A-Za-z]')])
    last_name = models.CharField(max_length=30,
                                 validators=[MinLengthValidator(2),
                                             RegexValidator(regex='[A-Za-z]')])
    email = models.EmailField(unique=True)
    choices = [("male", "Male"), ("female", "Female"), ("do not show", "Do not show")]
    gender = models.CharField(choices=choices)
    picture = models.URLField()



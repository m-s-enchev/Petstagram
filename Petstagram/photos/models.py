from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.accounts.models import PetstagramUser
from Petstagram.pets.models import Pet
from Petstagram.photos.validator import validate_file_size
# Create your models here.


class Photo(models.Model):
    photo = models.ImageField(upload_to='images', validators=(validate_file_size,))
    description = models.TextField(max_length=300,
                                   validators=(MinLengthValidator(10),), blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
    user = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE)

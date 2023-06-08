from django.shortcuts import render

# Create your views here.


def add(request):
    return render(request, template_name='pets/pet-add-page.html')


def pet_details(request):
    return render(request, template_name='pets/pet-details-page.html')


def pet_edit(request):
    return render(request, template_name='pets/pet-edit-page.html')


def pet_delete(request):
    return render(request, template_name='pets/pet-delete-page.html')


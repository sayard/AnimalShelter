from django.shortcuts import render
from .models import Animal


def adopt(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    animal.is_visible = False
    animal.save()
    return render(request, 'home_page/adopt.html', {'animal': animal})

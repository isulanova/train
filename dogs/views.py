from django.shortcuts import render
from dogs.models import DogsTable

def dogs(request):

    dogs = DogsTable.objects.all()

    context = {
        'dogs': dogs
    }


    return render(request, 'dogs/all_dogs.html', context)

def appearance(request, dog_slug):

    dog = DogsTable.objects.get(slug=dog_slug)

    context = {
        'dog': dog
    }

    return render(request, 'dogs/appearance.html', context=context)

def character(request, dog_slug):
    dog = DogsTable.objects.get(slug=dog_slug)

    context = {
        'dog': dog
    }

    return render(request, 'dogs/character.html', context=context)


def care(request, dog_slug):
    dog = DogsTable.objects.get(slug=dog_slug)

    context = {
        'dog': dog
    }

    return render(request, 'dogs/care.html', context=context)


def illness(request, dog_slug):
    dog = DogsTable.objects.get(slug=dog_slug)

    context = {
        'dog': dog
    }

    return render(request, 'dogs/illness.html', context=context)




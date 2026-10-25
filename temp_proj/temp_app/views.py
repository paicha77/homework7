from django.shortcuts import render


def info(request):
    context = {
        'name': 'Nikoloz',
        'surname': 'Paichadze',
        'age': 16,
        'height': 175,
        'city': 'Tbilisi',
    }

    return render(request, 'info.html', context)


def hobbies(request):
    context = {
        'hobbies': [
            'Playing Minecraft',
            'Programming',
            'Gaming',
            'Learning Django',
        ],
        'grade': 11,
    }

    return render(request, 'hobbies.html', context)

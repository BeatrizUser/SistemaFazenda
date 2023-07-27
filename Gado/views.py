from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from Gado.models import Animal

def dashboard(request):
    animais = Animal.objects.all()

    # Filtrar as ações do Django para o modelo Animal
    content_type = ContentType.objects.get_for_model(Animal)
    latest_actions = LogEntry.objects.filter(content_type=content_type).order_by('-action_time')[:10]
    total_animais = animais.count()
    context = {
        'animais': animais,
        'latest_actions': latest_actions,
        'total_animais': total_animais,
    }

    return render(request, 'pages/index.html', context)

def home(request):
    return redirect('dashboard')

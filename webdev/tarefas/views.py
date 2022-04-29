from django.shortcuts import render
from django.http import HttpResponseRedirect
from webdev.tarefas.forms import TarefaNovaForm
from django.urls import reverse

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            return render(request, 'tarefas/home.html', {'form': form}, status=400)
    #  busca o endereço do template
    return render(request, 'tarefas/home.html')
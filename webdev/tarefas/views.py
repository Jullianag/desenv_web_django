from django.shortcuts import render
from django.http import HttpResponseRedirect
from webdev.tarefas.forms import TarefaNovaForm, TarefaForm
from django.urls import reverse
from webdev.tarefas.models import Tarefa



def home(request):

    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_feitas = Tarefa.objects.filter(feita=True).all()
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
            return render(
                request, 'tarefas/home.html',
                {
                    'form': form,
                    'tarefas_pendentes': tarefas_pendentes,
                    'tarefas_feitas': tarefas_feitas,
                },
                status=400)

    #  busca o endereço do template
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    return render(
        request, 'tarefas/home.html',
        {
            'tarefas_pendentes': tarefas_pendentes,
            'tarefas_feitas': tarefas_feitas,
        }
        )


def detalhe(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST, instance=tarefa)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('tarefas:home'))
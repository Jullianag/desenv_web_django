import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.tarefas.models import Tarefa



@pytest.fixture
# o código se repete, por isso foi criada a função resposta e fixture
def resposta(client, db):
    # desse jeito o teste não fica dependende do endereço escrito
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


#  verifica se exite o formulário
def test_formulario_presente(resposta):
    #  garantimos que na resposta deve vir a tag de '<form'
    assertContains(resposta, '<form')


# garante a existencia do botão
def test_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')


@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Tarefa 1', feita=False),
        Tarefa(nome='Tarefa 2', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def lista_de_tarefas_feitas(db):
    tarefas = [
        Tarefa(nome='Tarefa 3', feita=False),
        Tarefa(nome='Tarefa 4', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def resposta_com_lista_de_tarefas(client, lista_de_tarefas_pendentes, lista_de_tarefas_feitas):
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_lista_de_tarefas_pendentes_presentes(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    for tarefa in lista_de_tarefas_pendentes:
        # ver se o nome de cada uma das tarefas da lista aparace
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)


def test_lista_de_tarefas_feitas_presentes(resposta_com_lista_de_tarefas, lista_de_tarefas_feitas):
    for tarefa in lista_de_tarefas_feitas:
        # ver se o nome de cada uma das tarefas da lista aparace
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)
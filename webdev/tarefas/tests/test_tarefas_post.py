import pytest
from django.urls import reverse
from webdev.tarefas.models import Tarefa



@pytest.fixture
# o código se repete, por isso foi criada a função resposta e fixture
# macado com db para o banco de dados
def resposta(client, db):
    # desse jeito o teste não fica dependende do endereço escrito, o data='name' foi definido no template
    resp = client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})
    return resp


def test_tarefa_existe_no_bd(resposta):
    #  objects acessa os dados no banco de dados
    assert Tarefa.objects.exists()


def test_tarefa_redirecionamento_depois_do_salvamento(resposta):
    assert resposta.status_code == 302


@pytest.fixture
def resposta_dado_invalido(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome': ''})
    return resp


def test_tarefa_nao_existe_no_bd(resposta_dado_invalido):
    assert not Tarefa.objects.exists()


def test_pagina_com_dados_invalidos(resposta_dado_invalido):
    assert resposta_dado_invalido.status_code == 400
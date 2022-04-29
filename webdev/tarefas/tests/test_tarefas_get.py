import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains



@pytest.fixture
# o código se repete, por isso foi criada a função resposta e fixture
def resposta(client):
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
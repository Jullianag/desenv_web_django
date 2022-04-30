from django.urls import path

from webdev.tarefas import views

app_name = 'tarefas'

urlpatterns=[
    #  path define o caminho
    path('', views.home, name='home'),
    path('<int:tarefa_id>', views.detalhe, name='detalhe'),
]
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns=[
    path('tarefas/',views.index),
    path('tarefas/delete/<slug:id>',views.delete_tarefa),
    path('tarefas/editar/<int:id>',views.editar_tarefa, name='editar tarefa'),
    path('',RedirectView.as_view(url='tarefas/'))
]


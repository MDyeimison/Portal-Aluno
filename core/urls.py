from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lists', views.pags, name='pags'),
    path('aluno', views.search, name='search'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('edit/editaluno/<int:pk>', views.editaluno, name='editaluno'),
    path('student/<int:pk>', views.student, name='student'),

    # CBV

    path('alunos-list', views.AlunosList.as_view(), name='alunos-list' ),
    # path('register', views.register, name='register')
    # path('mine/', MyView.as_view(), name='my-view')
]
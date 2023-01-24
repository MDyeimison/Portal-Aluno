from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lists', views.pags, name='pags'),
    path('aluno', views.search, name='search')
    #path('mine/', MyView.as_view(), name='my-view')
]
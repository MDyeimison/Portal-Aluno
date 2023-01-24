from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lists', views.pags, name='pags'),
    path('aluno', views.search, name='search'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    #path('mine/', MyView.as_view(), name='my-view')
]
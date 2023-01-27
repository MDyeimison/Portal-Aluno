from django.urls import path

from . import views

urlpatterns = [
    # ListView
    path('', views.IndexView.as_view(), name='index'),
    
    #path('aluno', views.search, name='search'),
    #path('aluno', views.SearchView.as_view(), name='search'),
    
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('edit/editaluno/<int:pk>', views.editaluno, name='editaluno'),
    path('detail/<int:pk>', views.StudentView.as_view(), name='detail'),

    # DetailView
    # path('student/<int:pk>', views.StudentView, name='student'),
]
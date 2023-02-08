from django.urls import path

from . import views

urlpatterns = [
    # ListView
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<uuid:id>', views.StudentView.as_view(), name='detail'),
    path('update/<uuid:id>', views.StudentUpdate.as_view(), name='update'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('delete/<uuid:id>', views.StudentDelete.as_view(), name='delete'),
    path('aluno-list', views.StudentList.as_view(), name='list')
]
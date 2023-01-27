from django.urls import path

from . import views

urlpatterns = [
    # ListView
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.StudentView.as_view(), name='detail'),
    path('update/<int:pk>', views.StudentUpdate.as_view(), name='update'),
    
    path('delete/<int:pk>', views.delete, name='delete'),
    # path('edit/<int:pk>', views.edit, name='edit'),
    # path('edit/editaluno/<int:pk>', views.editaluno, name='editaluno'),
]
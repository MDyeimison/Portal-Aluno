from django.urls import path

from . import views

urlpatterns = [
    # ListView
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.StudentView.as_view(), name='detail'),
    path('update/<int:pk>', views.StudentUpdate.as_view(), name='update'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('delete/<int:pk>', views.StudentDelete.as_view(), name='delete'),
]
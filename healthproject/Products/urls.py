from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('add/', views.add),
    path('delete/<int:id>/', views.delete),
    path('get/<int:id>/', views.get),
    path('edit/', views.edit),
]

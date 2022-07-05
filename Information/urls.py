from django.urls import path
from Information import views


urlpatterns = [
    path('', views.display_and_add, name="display_and_add"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('edit/<int:id>/', views.update, name="edit"),
]
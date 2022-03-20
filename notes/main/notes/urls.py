from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.notes, name = "notes"),
    path('note/<str:pk>/', views.note, name= "note"),
    path('note-form', views.createNote, name= "note-form"),
    

]



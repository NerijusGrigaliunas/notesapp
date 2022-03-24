from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.notes, name = "notes"),
    path('note/<str:pk>/', views.note, name= "note"),
    path('note-form', views.createNote, name= "note-form"),
    path('update-form/<str:pk>/', views.updateNote, name="update-note" ),
    path('delete-note/<str:pk>/', views.deleteNote, name="delete-note" ),

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),

]



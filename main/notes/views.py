
from ast import Not
from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Note
from. forms import NoteForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def notes(request):
    notes = Note.objects.all()
    context = { 'notes': notes}
    return render(request, 'notes.html', context)

def note(request, pk):
    note = Note.objects.get(id=pk)
    category = note.category.all()
    return render(request, 'note.html', {'note': note, 'category': category})

def createNote(request):
    form = NoteForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('notes')
    context = {'form': form}
    return render(request, 'note-form.html', context)



def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance = note)

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES,  instance = note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    context = {'form': form}
    return render (request, 'note-form.html', context)


def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    context = {'note': note}
    return render (request, 'delete-note.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:

            print ('Username does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('notes')
        else: 
                print("Username or password is incorect")

    return render(request, 'login_register.html')
        

def logoutUser(request):
    logout(request)
    return redirect('login')
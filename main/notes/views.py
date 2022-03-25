
from ast import Not
from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Note
from. forms import NoteForm, CategoryForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

def notes(request):
    notes = Note.objects.all()
    context = { 'notes': notes}
    return render(request, 'notes.html', context)

def note(request, pk):
    note = Note.objects.get(id=pk)
    category = note.category.all()
    return render(request, 'note.html', {'note': note, 'category': category})

@login_required(login_url="login")
def createNote(request):
    form = NoteForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('notes')
    context = {'form': form}
    return render(request, 'note-form.html', context)

def createCategory(request):
    form = CategoryForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('notes')
    context = {'form': form}
    return render(request, 'category-form.html', context)

@login_required(login_url="login")
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

@login_required(login_url="login")
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

           messages.error(request, 'User or password is not correct')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('notes')
        else: 
                messages.error(request, 'User does not exist')

    return render(request, 'login_register.html')
        

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logget out!')
    return redirect('login')
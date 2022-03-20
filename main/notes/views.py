
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

def notes(request):
    notes = Note.objects.all()
    context = { 'notes': notes}
    return render(request, 'notes.html', context)

def note(request, pk):
    note = Note.objects.get(id=pk)
    category = note.category.all()
    return render(request, 'note.html', {'note': note, 'category': category})
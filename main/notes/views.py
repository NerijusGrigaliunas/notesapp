
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def notes(request):
    return render(request, 'notes.html')

def note(request , pk):
    return HttpResponse('note.html')
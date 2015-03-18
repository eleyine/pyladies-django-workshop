from django.shortcuts import render
from django.http import HttpResponse

from notes.models import Note
 
def index(request):
    notes = Note.objects.all()
    output = ' / '.join([note.title for note in notes])
    return HttpResponse(output)

def archive_index(request):
    return HttpResponse("You're looking at the archive.")

def pinned_index(request):
    return HttpResponse("You're looking at your pinned notes.")

def detail(request, note_id):
    return HttpResponse("You're looking at note {0}.".format(note_id))

def create_note(request):
    return HttpResponse("You're creating a note.")

def edit_note(request, note_id):
    return HttpResponse("You're editing note {0}.".format(note_id))
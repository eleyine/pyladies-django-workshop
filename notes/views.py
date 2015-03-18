from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from notes.models import Note
 
def index(request):
    template = loader.get_template('notes/index.html')
    context = RequestContext(request, {
        'notes': Note.objects.all(),
    })
    return HttpResponse(template.render(context))

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
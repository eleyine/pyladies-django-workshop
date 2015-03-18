from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from notes.models import Note
 
def index(request):
    context = {
        'notes': Note.objects.all(),
        'colors': Note.COLOR_CHOICES
    }
    return render(request, 'notes/index.html', context)

def archive_index(request):
    return HttpResponse("You're looking at the archive.")

def pinned_index(request):
    return HttpResponse("You're looking at your pinned notes.")

def detail(request, note_id):
    return HttpResponse("You're looking at note {0}.".format(note_id))

def create_note(request):
    if request.method == 'POST':
        allowed_fields = ('title', 'content', 'color', )
        create_options = {}
        for name, value in request.POST.iteritems():
            if name in allowed_fields:
                create_options[name] = value
        Note.objects.create(**create_options)
        messages.success(request, 'Your note has been saved.')
    return HttpResponseRedirect(reverse('index'))

def edit_note(request, note_id):
    return HttpResponse("You're editing note {0}.".format(note_id))
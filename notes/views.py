from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views import generic

from notes.models import Note
 
class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'notes'
    index_type = 'index'
    filter_options = {'is_archived': False}

    def get_queryset(self):
        """Return all non archived notes."""
        return Note.objects.filter(**self.filter_options)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['colors'] = Note.COLOR_CHOICES
        context['index_type'] = self.index_type
        return context

class ArchiveIndexView(IndexView):
    index_type = 'archive'
    filter_options = {'is_archived': True}

class PinnedIndexView(IndexView):
    index_type = 'pinned'
    filter_options = {'is_pinned': True, 'is_archived': False}

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
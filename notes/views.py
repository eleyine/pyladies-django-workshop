from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
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

class EditFormView(generic.DetailView):
    template_name = 'notes/note-form.html'
    model = Note

    def get_object(self):
        return get_object_or_404(Note, id=self.kwargs['note_id'])

    def get_context_data(self, **kwargs):
        context = super(generic.DetailView, self).get_context_data(**kwargs)
        context['colors'] = Note.COLOR_CHOICES
        context['is_edit_form'] = True
        return context


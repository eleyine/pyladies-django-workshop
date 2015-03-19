from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views import generic

from notes.models import Note, Tag
from notes.forms import NoteForm, ArchiveNoteForm, PinnedNoteForm
 
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

class SearchIndexView(IndexView):
    index_type = 'search'

    def get_queryset(self):
        print self.kwargs
        if 'tag_keyword' in self.kwargs:
            return Note.objects.filter(
                tags__keyword__icontains=self.kwargs['tag_keyword'])
        else:
            messages.error(request, 'Invalid Search')
            return []

class TagJsonListView(generic.TemplateView):

    def render_to_response(self, context, **response_kwargs):
        keywords = [{'name': t.keyword} for t in Tag.objects.all()]
        return JsonResponse(keywords, safe=False)

class NoteAction(generic.View):
    form_class = NoteForm
    template_name = 'notes/index.html'

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('index'))

    def post(self, request, *args, **kwargs):
        do_update = 'note_id' in self.kwargs

        if do_update:
            note_instance = get_object_or_404(Note, 
                id=self.kwargs['note_id'])
            form = self.form_class(request.POST, instance=note_instance)
        else:
            form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your note has been saved.')
        else:
            # not so sure about this
            for error, message in form.errors.iteritems():
                messages.error(request, 'Invalid field ' + error)
        return HttpResponseRedirect(reverse('index'))

class DeleteAction(NoteAction):
    def post(self, request, *args, **kwargs):
        if 'note_id' in self.kwargs:
            note_instance = get_object_or_404(Note, id=self.kwargs['note_id'])
            note_instance.delete()
        return HttpResponseRedirect(reverse('index'))

class ArchiveNoteAction(NoteAction):
    form_class = ArchiveNoteForm

class PinnedNoteAction(NoteAction):
    form_class = PinnedNoteForm

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


from django import forms
from notes.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'color')

class ArchiveNoteForm(NoteForm):
    class Meta:
        model = Note
        fields = ('is_archived',)

class PinnedNoteForm(NoteForm):
    class Meta:
        model = Note
        fields = ('is_pinned',)

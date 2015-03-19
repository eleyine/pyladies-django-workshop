from django.forms import ModelForm
from notes.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'color')
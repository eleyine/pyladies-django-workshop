from django.contrib import admin
from notes.models import Note, Tag, NoteCollection

admin.site.register(Note)
admin.site.register(Tag)
admin.site.register(NoteCollection)
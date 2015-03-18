from django.apps import AppConfig

class NotesConfig(AppConfig):
    name = 'notes'

    def ready(self):
        import notes.signals
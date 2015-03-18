from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from notes.models import Note

from loremipsum import get_sentence, get_paragraph
from random import randint

class Command(BaseCommand):
    args = 'numNotes [--reset]'
    help = 'Create notes using lorem ipsum generator'

    option_list = BaseCommand.option_list + (
        make_option('--reset',
            action='store_true',
            dest='reset',
            default=False,
            help='Delete all notes before generating new ones.'),
        )

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Usage: {0}'.format(self.args))

        if options['reset']:
            Note.objects.all().delete()

        numNotes = args[0]

        try:
            Command.generate_notes(int(numNotes))
        except ValueError:
            raise CommandError('Usage: you must pass a valid number.')
        except:
            raise CommandError('A vague error occured while generating notes')

        self.stdout.write('Successfully generated {0} notes'.format(numNotes))

    @staticmethod
    def generate_notes(n, **kwargs):
        for i in range(n):
            Note.objects.create(**Command.generate_note_data(**kwargs))

    @staticmethod
    def generate_note_data(max_length=300):
        content = get_paragraph()[:max_length]
        # add random hashtags
        content += '\n' + get_sentence().replace(' ', ' #')
        data =  {
            'title':  get_sentence(), 
            'content': content,
            'color': Command.random_color()
            }
        return data

    @staticmethod
    def random_color():
        random_color_i = randint(0, len(Note.COLOR_CHOICES)-1)
        return Note.COLOR_CHOICES[random_color_i][0]


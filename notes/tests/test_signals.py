from django.test import TestCase
from notes.models import Note, Tag

class SignalsTestCase(TestCase):
    def test_note_creates_tags(self):
        """
        Tests Tags are automatically created based on Note content. 
        """
        # check that tags are associated with saved object in database
        note = Note(title='My first note', 
            content='Noteworthy content for #pyladies')
        note.save()

        self.assertEqual(Tag.objects.count(), 1)
        self.assertTrue(Tag.objects.get(keyword='pyladies'))
        self.assertEqual(Note.objects.get(pk=note.pk).tags.count(), 1)
        self.assertEqual(Tag.objects.get(keyword='pyladies').notes.count(), 1)

        # check tags are not duplicated and are grouped
        note = Note(title='My second note', 
            content='Noteworthy content for #pyladies with the same hashtag.')
        note.save()
        
        self.assertEqual(Tag.objects.count(), 1)
        self.assertTrue(Tag.objects.get(keyword='pyladies'))
        self.assertEqual(Note.objects.get(pk=note.pk).tags.count(), 1)
        self.assertEqual(Tag.objects.get(keyword='pyladies').notes.count(), 2)

    def test_note_updates_tags(self):
        """
        Tests Tags are automatically updated based on Note content. 
        """
        note = Note(title='My first note', 
            content='Noteworthy content for #pyladies')
        note.save()

        for i in range(3):
            if i == 0:
                note.content = '... but it can be improved. #workshop #python'
            elif i == 1:
                note.content = '... but it can be improved some more. #workshop #python'
            else:
                pass # test saving twice

            note.save()

            self.assertTrue(Tag.objects.get(keyword='workshop'))
            self.assertTrue(Tag.objects.get(keyword='python'))
            self.assertEqual(Tag.objects.filter(keyword='pyladies').count(), 0)

            self.assertEqual(Tag.objects.count(), 2)

            self.assertEqual(note.tags.count(), 2)
            self.assertEqual(Note.objects.get().tags.count(), 2)

    def test_loose_tags_removed_when_note_deleted(self):
        """
        Tests 'loose' tags (i.e. Tags associated with no notes) are removed 
        when Note is deleted. 
        """
        note = Note(title='My first note', 
            content='Noteworthy content for #pyladies')
        note.save()
        note = Note(title='My second note', 
            content='Noteworthy content for #workshop')
        note.save()

        Note.objects.all().delete()
        self.assertEqual(Tag.objects.count(), 0)
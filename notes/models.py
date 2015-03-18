from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100, default='')
    content = models.TextField(default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_pinned = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    note_collection = models.ForeignKey('NoteCollection', 
        null=True, related_name='notes')

    COLOR_CHOICES = (
        ('white', 'White'),
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('turquoise', 'Turquoise'),
        ('blue', 'Blue'),
        ('gray', 'Gray'),
    )

    color = models.CharField(max_length=9,
                             choices=COLOR_CHOICES,
                             default=COLOR_CHOICES[0][0])

    @staticmethod
    def parsed_tags(note__content):
        import re
        HASHTAG_REGEX = r"\B#(\w*[a-zA-Z]+)\w*"
        return re.findall(HASHTAG_REGEX, note__content)

    class Meta:
        # when ordering by boolean, false comes first (db dependant)
        ordering = ('-is_pinned', 'is_archived', '-updated_at' )

    def __unicode__(self):
        return '{0}'.format(self.title)

class Tag(models.Model):
    keyword = models.CharField(max_length=50)
    notes = models.ManyToManyField('Note', related_name='tags')

    def __unicode__(self):
        return '#{0}'.format(self.keyword)

class NoteCollection(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '{0}'.format(self.name)

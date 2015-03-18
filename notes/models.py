from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __unicode__(self):
        return '{0}'.format(self.title)

class Tag(models.Model):
    keyword = models.CharField(max_length=50)

    def __unicode__(self):
        return '#{0}'.format(self.keyword)

class NoteCollection(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return '{0}'.format(self.name)

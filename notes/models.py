from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Tag(models.Model):
    keyword = models.CharField(max_length=50)

class NoteCollection(models.Model):
    name = models.CharField(max_length=50)


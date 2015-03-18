from django.db.models import Count
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from notes.models import Note, Tag

@receiver(post_save, sender=Note)
def update_created_note_tags(sender, instance, created=False, **kwargs):
    note_instance = instance
    if created:
        tag_instances = []
        # If Note is created, create associated Tags
        for t in Note.parsed_tags(note_instance.content):
            tag_instance, created = Tag.objects.get_or_create(keyword=t)
            tag_instances.append(tag_instance)

        note_instance.tags.add(*tag_instances)

# The reason I have the update logic in a pre_save signal instead of post_save 
# is because there's no way to check for content change after the object has 
# been saved.
# Conversely, the creation logic can't be in pre_save because you can't add tags 
# only after the Note has been saved. Send a pull request if you find a more 
# elegant solution!
@receiver(pre_save, sender=Note)
def update_note_tags(sender, instance, **kwargs):
    note_instance = instance

    # check if note has already been created
    if instance.pk:
         # Update tags if note content has changed
        old_note_instance = Note.objects.get(pk=note_instance.pk)

        if note_instance.content != old_note_instance.content:
            new_tags = set(Note.parsed_tags(note_instance.content))
            old_tags = set([t.keyword for t in old_note_instance.tags.all()])

            # Add tags new to the note
            tags_to_add = new_tags.difference(old_tags)
            tag_instances = []
            for t in tags_to_add:
                tag_instance, created = Tag.objects.get_or_create(keyword=t)
                tag_instances.append(tag_instance)
            note_instance.tags.add(*tag_instances)

            # Remove tags no longer present in note
            tags_to_remove = old_tags.difference(new_tags)
            tags_to_remove_set = Tag.objects.filter(keyword__in=tags_to_remove)
            note_instance.tags.remove(*tags_to_remove_set.all())

            remove_loose_tags(tag_queryset=tags_to_remove_set)

@receiver(post_delete, sender=Note)
def update_tags_if_note_deleted(sender, instance, **kwargs):
    remove_loose_tags()

def remove_loose_tags(tag_queryset=Tag.objects):
    # Remove tag instances if they are associated with no notes
    tags_with_no_notes = tag_queryset.annotate(num_notes=Count('notes')
        ).filter(num_notes=0)
    tags_with_no_notes.delete()



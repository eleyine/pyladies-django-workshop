from django.conf.urls import patterns, url
 
from notes import views
 
urlpatterns = patterns('',
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /archive.
    url(r'^archive/$', views.archive_index, name='archive'),
    # ex: /pinned/
    url(r'^pinned/$', views.pinned_index, name='pinned'),
    # ex: /5/
    url(r'^(?P<note_id>\d+)/$', views.detail, name='detail'),
    # ex: /create/
    url(r'^create$', views.create_note, name='create_note'),
    # ex: /5/edit
    url(r'^(?P<note_id>\d+)/edit$', views.edit_note, name='edit_note'),
)
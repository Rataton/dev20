from django.conf.urls import url
from . import views as cViews

urlpatterns = [
    url(r'^$', cViews.get_notas, name='get_notas'),
    url(r'^new/$', cViews.NoteView.as_view(), name='note_new'),
    url(r'^edit/(?P<id>\d+)/$', cViews.NoteEdit.as_view(), name='note_edit'),
    url(r'^delete/(?P<id>\d+)/$', cViews.NoteDelete.as_view(), name='note_delete'),
]

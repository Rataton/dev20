from django.conf.urls import url
from . import views as cViews

urlpatterns = [
    url(r'^$', cViews.get_contactos, name='get_contactos'),
    url(r'^new/$', cViews.PersonView.as_view(), name='person_new'),
    url(r'^edit/(?P<id>\d+)/$', cViews.PersonEdit.as_view(), name='person_edit'),
    url(r'^delete/(?P<id>\d+)/$', cViews.PersonDelete.as_view(), name='person_delete'),
]

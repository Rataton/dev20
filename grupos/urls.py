from django.conf.urls import url
from . import views as cViews

urlpatterns = [
    url(r'^$', cViews.get_grupos, name='get_grupos'),
    url(r'^new/$', cViews.GroupView.as_view(), name='group_new'),
    url(r'^edit/(?P<id>\d+)/$', cViews.GroupEdit.as_view(), name='group_edit'),
    url(r'^delete/(?P<id>\d+)/$', cViews.GroupDelete.as_view(), name='group_delete'),
]

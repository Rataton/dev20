from django.conf.urls import url
from . import views as aViews

urlpatterns = [
    url(r'^login/$', aViews.Login.as_view(), name='login'),
    url(r'^my-account/$', aViews.my_account, name='my_account'),
    url(r'^signup/$', aViews.register, name='signup'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login'}, name='logout')
]
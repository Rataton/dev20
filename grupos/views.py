from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.template.context_processors import csrf
from contactos.models import Group
from django.views.generic import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms as cForms


class GroupView(FormView):
    template_name = 'grupos/group.html'
    form_class = cForms.GroupForm

    def form_valid(self, form):
        self.success_url = reverse('grupos:get_grupos')
        form.save(user=self.request.user)
        return super(GroupView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(GroupView, self).dispatch(request, *args, **kwargs)


class GroupEdit(UpdateView):
    template_name = 'grupos/group_edit.html'
    form_class = cForms.GroupFormEdit
    success_url = reverse_lazy('grupos:get_grupos')

    def form_valid(self, form):
        form.save(None)
        return super(GroupEdit, self).form_valid(form)

    def get_success_url(self):
        return self.success_url

    def get_object(self, queryset=None):
        obj = Group.objects.get(id=self.kwargs['id'])
        return obj

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(GroupEdit, self).dispatch(request, *args, **kwargs)


class GroupDelete(DeleteView):
    template_name = 'grupos/group_delete.html'
    form_class = cForms.GroupFormEdit
    success_url = reverse_lazy('grupos:get_grupos')

    def form_valid(self, form):
        form.delete()
        return super(GroupDelete, self).form_valid(form)

    def get_success_url(self):
        return self.success_url

    def get_object(self, queryset=None):
        obj = Group.objects.get(id=self.kwargs['id'])
        return obj

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(GroupDelete, self).dispatch(request, *args, **kwargs)


def home(request):
    return render(request, 'index.html')


@login_required
def get_grupos(request):
    user = request.user
    grupos = Group.objects.filter(user=user)

    return render(
        request,
        'grupos/grupos.html',
        {'grupos': grupos}
    )

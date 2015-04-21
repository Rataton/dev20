from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.template.context_processors import csrf
from contactos.models import Notes
from django.views.generic import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms as cForms


class NoteView(FormView):
    template_name = 'notas/note.html'
    form_class = cForms.NoteForm

    def form_valid(self, form):
        self.success_url = reverse('notas:get_notas')
        form.save(user=self.request.user)
        return super(NoteView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NoteView, self).dispatch(request, *args, **kwargs)


class NoteEdit(UpdateView):
    template_name = 'notas/note_edit.html'
    form_class = cForms.NoteFormEdit
    success_url = reverse_lazy('notas:get_notas')

    def form_valid(self, form):
        form.save(None)
        return super(NoteEdit, self).form_valid(form)

    def get_success_url(self):
        return self.success_url

    def get_object(self, queryset=None):
        obj = Note.objects.get(id=self.kwargs['id'])
        return obj

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NoteEdit, self).dispatch(request, *args, **kwargs)


class NoteDelete(DeleteView):
    template_name = 'notas/note_delete.html'
    form_class = cForms.NoteFormEdit
    success_url = reverse_lazy('notas:get_notas')

    def form_valid(self, form):
        form.delete()
        return super(NoteDelete, self).form_valid(form)

    def get_success_url(self):
        return self.success_url

    def get_object(self, queryset=None):
        obj = Note.objects.get(id=self.kwargs['id'])
        return obj

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(NoteDelete, self).dispatch(request, *args, **kwargs)


def home(request):
    return render(request, 'index.html')


@login_required
def get_notas(request):
    user = request.user
    notas = Note.objects.filter(user=user)

    return render(
        request,
        'notas/notas.html',
        {'notas': notas}
    )

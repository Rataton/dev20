from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.template.context_processors import csrf
from .models import Person
from django.views.generic import View
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms as cForms
from django.http import Http404


class PersonView(FormView):
    template_name = 'contactos/person.html'
    form_class = cForms.PersonForm

    def form_valid(self, form):
        self.success_url = reverse('contactos:get_contactos')
        form.save(user=1)
        print self.request.user
        return super(PersonView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PersonView, self).dispatch(request, *args, **kwargs)


class PersonDelete(DeleteView):
    template_name = 'contactos/person_delete.html'
    form_class = cForms.PersonForm
    success_url = reverse_lazy('contactos:get_contactos')
    
    def form_valid(self, request, *args, **kwargs):
        # self.success_url = reverse('contactos:get_contactos')
        # self.object = self.get_object()
        form.delete()
        # self.object.delete()
        return super(PersonView, self).form_valid(form)

    def get_success_url(self):
        return self.success_url

    def get_object(self, queryset=None):
        obj = Person.objects.get(id=self.kwargs['id'])
        return obj    

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PersonDelete, self).dispatch(request, *args, **kwargs)


class PersonEdit(UpdateView):
    template_name = 'contactos/person_edit.html'
    form_class = cForms.PersonForm
    success_url = reverse_lazy('contactos:get_contactos')

    def form_valid(self, form):
        form.save()
        return super(PersonEdit, self).form_valid(form)

    # def get(self, request, **kwargs):
    #     self.object = Person.objects.get(id=self.kwargs['id'])
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     context = self.get_context_data(object=self.object, form=form)
    #     return self.render_to_response(context)
    
    def get_success_url(self):
        return self.success_url

    def get_object(self, queryset=None):
        obj = Person.objects.get(id=self.kwargs['id'])
        return obj
    

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PersonEdit, self).dispatch(request, *args, **kwargs)


def home(request):
    return render(request, 'index.html')


@login_required
def get_contactos(request):
    user = request.user
    contactos = Person.objects.filter(user=user)

    return render(
        request,
        'contactos/contactos.html',
        {'contactos': contactos}
    )


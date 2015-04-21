from django import forms
from .models import Person

class PersonForm(forms.ModelForm):

	def save(self, *args, **kwargs):
		self.instance.user = kwargs.pop('user')
		super(PersonForm, self).save(*args, **kwargs)

	class Meta:
		model = Person
		exclude = ('user', )
		# fields

class PersonFormEdit(forms.ModelForm):

	def save(self, *args, **kwargs):
		super(PersonFormEdit, self).save(*args, **kwargs)

	class Meta:
		model = Person
		exclude = ('user', )
		# fields
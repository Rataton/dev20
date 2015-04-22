from django import forms
from .models import Group
from contactos.models import Person

class GroupForm(forms.ModelForm):

	def save(self, *args, **kwargs):
		self.instance.user = kwargs.pop('user')
		super(GroupForm, self).save(*args, **kwargs)

	class Meta:
		model = Group
		exclude = ('user', )
		# fields

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(GroupForm, self).__init__(*args, **kwargs)
		self.fields['person'].queryset = Person.objects.filter(user=user)


class GroupFormEdit(forms.ModelForm):

	def save(self, *args, **kwargs):
		super(GroupFormEdit, self).save(*args, **kwargs)

	class Meta:
		model = Group
		exclude = ('user', )
		# fields

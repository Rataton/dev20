from django import forms
from contactos.models import Group

class GroupForm(forms.ModelForm):

	def save(self, *args, **kwargs):
		self.instance.user = kwargs.pop('user')
		super(GroupForm, self).save(*args, **kwargs)

	class Meta:
		model = Group
		exclude = ('user', )
		# fields

class GroupFormEdit(forms.ModelForm):

	def save(self, *args, **kwargs):
		super(GroupFormEdit, self).save(*args, **kwargs)

	class Meta:
		model = Group
		exclude = ('user', )
		# fields
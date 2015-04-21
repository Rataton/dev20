from django import forms
from contactos.models import Note

class NoteForm(forms.ModelForm):

	def save(self, *args, **kwargs):
		self.instance.user = kwargs.pop('user')
		super(NoteForm, self).save(*args, **kwargs)

	class Meta:
		model = Note
		exclude = ('user', )
		# fields

class NoteFormEdit(forms.ModelForm):

	def save(self, *args, **kwargs):
		super(NoteFormEdit, self).save(*args, **kwargs)

	class Meta:
		model = Note
		exclude = ('user', )
		# fields
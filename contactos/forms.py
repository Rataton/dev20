from django import forms
from .models import Person

class PersonForm(forms.ModelForm):

	def save(self, user=None, *args, **kwargs):
		print self.instance.user
		# if not self.instance.user:
			# self.instance.user = kwargs.pop('user')
		self.instance.user = user
		super(PersonForm, self).save(*args, **kwargs)

	class Meta:
		model = Person
		exclude = ('user', )
		# fields
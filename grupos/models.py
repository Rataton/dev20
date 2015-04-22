from django.db import models
from django.contrib.auth.models import User
from contactos.models import Person


class Group(models.Model):
    name = models.CharField(max_length=120, verbose_name=u'Nombre')
    description = models.CharField(max_length=300, verbose_name=u'Descripcion')
    person = models.ManyToManyField(Person)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    NONE = ''
    INFO = 'bg-info'
    DANGER = 'bg-danger'
    WARNING = 'bg-warning'
    SUCCESS = 'bg-success'

    COLOR_CHOICES = (
        (NONE, 'Ninguno'),
        (INFO, 'Blue'),
        (DANGER, 'Red'),
        (WARNING, 'Yellow'),
        (SUCCESS, 'Green'),
    )
    title = models.CharField(max_length=50, verbose_name='Titulo')
    content = models.TextField(max_length=300, verbose_name='contenido')
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default=NONE, verbose_name='Color')
    # color = models.IntegerField(choices=COLOR_CHOICES)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

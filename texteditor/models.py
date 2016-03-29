from django.db import models

# Create your models here.

class Editor(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    def __unicode__(self):
        return '%s' % self.title
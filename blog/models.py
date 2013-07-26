from django.core.urlresolvers import reverse
from datetime import datetime
from django.db import models
from django.db.models import signals
from meu_blog.utils import slug_pre_save

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    class Meta:
        ordering = ('-publicacao',)

    def get_absolute_url(self):
        return reverse('artigo', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.titulo

# SIGNALS

signals.pre_save.connect(slug_pre_save, sender=Artigo)

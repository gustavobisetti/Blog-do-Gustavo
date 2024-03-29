from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import signals
from meu_blog.utils import slug_pre_save

class Album(models.Model):
    """Um album eh um pacote de imagens, ele tem um titulo e um slug para sua
    identificacao."""
    class Meta:
        ordering = ('titulo',)

    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('galerias.views.album', args=[str(self.slug)])

class Imagem(models.Model):
    """Cada instancia desta classe contem uma imagem da galeria, com seu
    respectivo thumbnail (miniatura) e imagem em tamanho natural.
    Varias imagens podem conter dentro de um Album"""

    class Meta:
        ordering = ('album','titulo',)

    album = models.ForeignKey('Album')
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    descricao = models.TextField(blank=True)
    original = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/original',
    )
    thumbnail = models.ImageField(
        null=True,
        blank=True,
        upload_to='galeria/thumbnail',
    )
    publicacao = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('imagem', kwargs={'slug': self.slug})
# SIGNALS
signals.pre_save.connect(slug_pre_save, sender=Album)
signals.pre_save.connect(slug_pre_save, sender=Imagem)

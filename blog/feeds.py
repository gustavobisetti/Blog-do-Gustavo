from django.contrib.syndication.views import Feed

from .models import Artigo

class UltimosArtigos(Feed):
    title = 'Ultimos artigos do blog'
    link = '/'
    description_template = 'feeds/ultimos_description.html'
    title_template = 'feeds/ultimos_title.html'

    def items(self):
        return Artigo.objects.all()


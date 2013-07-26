from django.conf.urls.defaults import *

urlpatterns = patterns('galerias.views',
    url(r'^$', 'albuns', name='albuns'),
    url(r'^(?P<slug>[\w_-]+)/$', 'album', name='album'),
    url(r'^imagem/(?P<slug>[\w_-]+)/$', 'imagem', name='imagem'),
)

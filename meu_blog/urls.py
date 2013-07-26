from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.feeds import UltimosArtigos

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.Artigos', name='home'),
    url(r'^galeria/', include('galerias.urls')),
    url(r'^tags/', include('tags.urls')),
    # url(r'^meu_blog/', include('meu_blog.foo.urls')),
    url(r'^contato/$', 'meu_blog.views.contato', name='contato'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^meu_blog/$', 'blog.views.Artigos', name="blog_gustavo"),
    url(r'^artigo/(?P<slug>[\w_-]+)/$', 'blog.views.MostraArtigo', name="artigo"),
    url(r'^comments/', include('django.contrib.comments.urls'), name="comentarios"),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^rss/ultimos/$', UltimosArtigos())
)

from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Artigo
from django.template import RequestContext
from django.shortcuts import get_object_or_404

def Artigos(request):
    queryset=Artigo.objects.all()
    return render_to_response('blog/artigo_arquive.html', RequestContext(
        request,
        {'Artigos': queryset}
    ))

def MostraArtigo(request, slug):
    return render_to_response('blog/artigo.html', RequestContext(
        request,
        {'artigo': get_object_or_404(Artigo, slug=slug)}
    ))

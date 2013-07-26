from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from .models import Tag

def tags(request):
    return render(request,
        'tags/tags.html',
        {'lista': Tag.objects.all(),}
    )

def tag(request, tag_nome):
    return render(request,
        'tags/tag.html',
        {'tag': get_object_or_404(Tag, nome=tag_nome)}
    )

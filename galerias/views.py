from django.shortcuts import get_object_or_404, render

from models import Album, Imagem

def albuns(request):
    return render(
        request,
        'galerias/albuns.html',
        {'lista': Album.objects.all()}
    )

def album(request, slug):
    album_ = get_object_or_404(Album, slug=slug)
    return render(
        request,
        'galerias/album.html',
        {
            'album': album_,
            'imagens': Imagem.objects.filter(album=album_)
        }
    )

def imagem(request, slug):
    imagem_ = get_object_or_404(Imagem, slug=slug)
    return render(
        request,
        'galerias/imagem.html',
        {
            'imagem': imagem_
        }
    )

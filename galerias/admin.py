try:
    import Image
except ImportError:
    from PIL import Image

from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from models import Album, Imagem
from tags import aplicar_tags, tags_para_objeto

class AdminAlbum(ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

class FormImagem(forms.ModelForm):
    class Meta:
        model = Imagem

    tags = forms.CharField(max_length=30, required=False)

    def __init__(self, *args, **kwargs):
        super(FormImagem, self).__init__(*args, **kwargs)

        if self.instance.id:
            self.initial['tags'] = tags_para_objeto(
            self.instance
            )

class AdminImagem(ModelAdmin):
    list_display = ('album','titulo',)
    list_filter = ('album',)
    search_fields = ('titulo','descricao',)
    form = FormImagem

    def save_model(self, request, obj, form, change):
        """Metodo declarado para criar miniatura da imagem depois de salvar"""
        super(AdminImagem, self).save_model(request, obj, form, change)

        if 'original' in form.changed_data:
            extensao = obj.original.name.split('.')[-1]
            obj.thumbnail = 'galeria/thumbnail/%s.%s'%(
                obj.id, extensao)

            miniatura = Image.open(obj.original.path)
            miniatura.thumbnail((100,100), Image.ANTIALIAS)
            miniatura.save(obj.thumbnail.path)

            obj.save()

        aplicar_tags(obj, form.cleaned_data['tags'])

admin.site.register(Album, AdminAlbum)
admin.site.register(Imagem, AdminImagem)

from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import FormContato

def contato(request):
    mostrar = ''
    if request.method == 'POST':
        form = FormContato(request.POST)

        if form.is_valid():
            form.enviar()
            mostrar = 'Contato enviado!'
    else:
        form = FormContato()


    return render_to_response(
        'contato.html', RequestContext(
        request, {'form': form,'mostrar': mostrar})
    )


from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'evento': evento}
    return render(request,'agenda.html', dados)

@login_required(login_url='/login/')
def cadastra_evento(request):
    return render(request, 'cadastra.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                        data_evento=data_evento,
                        descricao=descricao,
                        usuario=usuario)
    return redirect('/')
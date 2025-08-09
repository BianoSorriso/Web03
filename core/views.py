from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Projeto, Contato, Doacao, Voluntario
from .forms import ContatoForm, DoacaoForm, VoluntarioForm

def home(request):
    projetos = Projeto.objects.filter(ativo=True).order_by('-data_criacao')[:3]
    return render(request, 'pages/home.html', {'projetos': projetos})

def sobre(request):
    return render(request, 'pages/sobre.html')

def projetos(request):
    projetos = Projeto.objects.filter(ativo=True).order_by('-data_criacao')
    return render(request, 'pages/projetos.html', {'projetos': projetos})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'pages/contato.html', {'form': form})

def area_voluntarios(request):
    # Se o usuário não estiver autenticado, apenas renderiza a página sem o formulário
    if not request.user.is_authenticated:
        return render(request, 'pages/area_voluntarios.html')
    
    # Se o usuário estiver autenticado, processa o formulário
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            voluntario = form.save(commit=False)
            voluntario.usuario = request.user
            voluntario.save()
            messages.success(request, 'Cadastro de voluntário realizado com sucesso!')
            return redirect('area_voluntarios')
    else:
        # Verificar se o usuário já é voluntário
        try:
            voluntario = Voluntario.objects.get(usuario=request.user)
            form = VoluntarioForm(instance=voluntario)
        except Voluntario.DoesNotExist:
            form = VoluntarioForm()
    
    return render(request, 'pages/area_voluntarios.html', {'form': form})

def doacoes(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doação registrada com sucesso!')
            return redirect('doacoes')
    else:
        form = DoacaoForm()
    return render(request, 'pages/doacoes.html', {'form': form})

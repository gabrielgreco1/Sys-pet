from django.shortcuts import render
from .models import Venda

def home(request):
    return render(request, 'usuarios/index.html')

def vendas(request):
    # Salva os dados inseridos na tela no banco
    nova_venda = Venda()
    nova_venda.id_venda = request.POST.get('id_venda')
    nova_venda.valor = request.POST.get('valor')
    nova_venda.cliente = request.POST.get('cliente')
    nova_venda.cliente = request.POST.get('data')
    nova_venda.save()
    # Exibir todos os usuarios cadastrados em uma nova pagina
    vendas = {
        'vendas': Venda.objects.all()
    }
    # Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/vendas.html', vendas)



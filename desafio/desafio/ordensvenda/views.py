#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from desafio.ordensvenda.forms import AnexoForm
from desafio.ordensvenda.models import (Anexo, Comprador, Vendedor, Item,
    Compra)

def salva_objetos(arquivo):
    """
    Função para salvar os objetos.
    """
    arquivo = arquivo.read()
    linhas = arquivo.split('\n')
    cabecalho = True
    linhas.pop()
    compras = []
    for i in linhas:
        if cabecalho:
            cabecalho = False
            continue
        linha_split = i.split('\t')
        try:
            comprador = Comprador.objects.create(nome_comprador=linha_split[0])
            vendedor = Vendedor.objects.create(nome_vendedor=linha_split[5],
                                               endereco=linha_split[4])
            item = Item.objects.create(descricao_item=linha_split[1],
                preco_item=round(float(linha_split[2])))
        except:
            return compras
        compras.append((Compra.objects.create(
            quantidade=int(linha_split[3]),
            comprador=comprador,
            vendedor=vendedor,
            item=item)))
    return compras

def envio(request):
    """
    View para envio de anexo de arquivo.
    """
    if request.method == 'POST':
        form = AnexoForm(request.POST, request.FILES)
        if form.is_valid():
            compras = salva_objetos(request.FILES.items()[0][1].file)
            if compras:
                total = 0
                for i in compras:
                    total += i.quantidade * i.item.preco_item
                total = total
                Anexo.objects.create(arquivo=request.FILES.items()[0][1])
                mensagem = u'Formulário enviado com sucesso'
                messages.success(request, mensagem)
                return render_to_response(
                    u'envio.html',
                    {'form': AnexoForm(), 'total': total},
                    context_instance=RequestContext(request),
                )
            else:
                mensagem = u'-Árquivo inválido.'
                messages.error(request, mensagem)
        else:
            mensagem = u'-Erro no formulário. Verifique antes de enviar \
                novamente.'
            messages.error(request, mensagem)
    else:
        form = AnexoForm(request.GET or None)

    return render_to_response(
        u'envio.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

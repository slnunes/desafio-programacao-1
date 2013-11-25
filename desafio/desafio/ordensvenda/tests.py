#-*- coding:utf-8 -*-

from django.test import TestCase
from desafio.ordensvenda.models import *

class SaveModelsTestCase(TestCase):
    """
    Classe que testa o save das classes do models.
    """
    def test_save_objetos(self):
        """
        Garante que todos os campos de caráter obrigatório existem.
        """
        anexo = Anexo()
        anexo.arquivo = "/example_input.tab"
        anexo.save()
        self.assertTrue(anexo.id)

        comprador = Comprador()
        comprador.nome_comprador = u"João Sales"
        comprador.save()
        self.assertTrue(comprador.id)

        vendedor = Vendedor()
        vendedor.nome_vendedor = u"Roberto"
        vendedor.endereco = u"Fazenda Souza"
        vendedor.save()
        self.assertTrue(vendedor.id)

        item = Item()
        item.descricao_item = "50% de desconto"
        item.preco_item = 10.50
        item.save()
        self.assertTrue(item.id)

        compra = Compra()
        compra.quantidade = 15
        compra.comprador = comprador
        compra.vendedor = vendedor
        compra.item = item
        compra.save()
        self.assertTrue(compra.id)

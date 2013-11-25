#-*- coding:utf-8 -*-

from django.db import models


class Anexo(models.Model):
    """
    Classe com dados de um anexo.
    """
    class Meta:
        """
        Classe com configurações do models anexo.
        """
        verbose_name=u'Anexo'
        verbose_name_plural=u'Anexos'
    
    arquivo = models.FileField(
        u'Arquivo',
        upload_to='arquivos',
        )

    def __unicode__(self):
        return unicode(self.arquivo)


class Comprador(models.Model):
    """
    Classe com dados do comprador.
    """
    class Meta:
        """
        Classe com configurações do models Comprador.
        """
        verbose_name=u'Comprador'
        verbose_name_plural=u'Compradores'

    nome_comprador = models.CharField(
        u'Nome do Comprador',
        max_length=100,
        )

    def __unicode__(self):
        return unicode(self.nome_comprador)


class Vendedor(models.Model):
    """
    Classe com dados relacionados ao vendedor.
    """
    class Meta:
        """
        Classe com configurações do models Vendedor.
        """
        verbose_name=u'Vendedor'
        verbose_name_plural=u'Vendedores'

    nome_vendedor = models.CharField(
        u'Nome do Vendedor',
        max_length=100,
        )

    endereco = models.CharField(
        u'Endereço do Vendedor',
        max_length=100,
        )

    def __unicode__(self):
        return unicode(self.nome_vendedor)


class Item(models.Model):
    """
    Classe com dados relacionados a itens.
    """
    class Meta:
        """
        Classe com configurações do models Produto.
        """
        verbose_name=u'Item'
        verbose_name_plural=u'Itens'

    descricao_item = models.CharField(
        u'Descrição do Item',
        max_length=100,
        )

    preco_item = models.DecimalField(
        u'Preço do Item',
        max_digits=5,
        decimal_places=2,
        )

    def __unicode__(self):
        return unicode(self.descricao_item)


class Compra(models.Model):
    """
    Classe com relações dos dados vínculados a uma compra.
    """
    class Meta:
        """
        Classe com configurações do models Compra.
        """
        verbose_name=u'Compra'
        verbose_name_plural=u'Compras'

    quantidade = models.IntegerField(
        u'Quantidade',
        )

    comprador = models.ForeignKey(
        Comprador,
        )

    vendedor = models.ForeignKey(
        Vendedor,
        )

    item = models.ForeignKey(
        Item,
        )

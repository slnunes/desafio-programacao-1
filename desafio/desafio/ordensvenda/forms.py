#-*- coding:utf-8 -*-

from django import forms

from desafio.ordensvenda.models import Anexo

class AnexoForm(forms.ModelForm):
    """
    Formulário para envio de anexos de arquivos.
    """
    class Meta:
        model = Anexo

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re


from categoria.models import Categoria
from parceiro.models import Parceiro


class ParceiroForm(forms.ModelForm):

    class Meta:
        model = Parceiro
        fields = ('nome', 'categoria', 'telefone', 'cnpj')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={'required': 'Campo obrigatório.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['categoria'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['categoria'].queryset = Categoria.objects.all().order_by('nome')
        self.fields['categoria'].empty_label = '--- Selecione uma categoria ---'

        self.fields['telefone'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['telefone'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['cnpj'].error_messages = {'required': 'Campo obrigatório'}
        self.fields['cnpj'].widget.attrs.update({'class': 'form-control form-control-sm'})


    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        cnpjAlterado = ''.join(re.findall('\d', str(cnpj)))
        if (not cnpjAlterado) or (len(cnpjAlterado) < 14):
            raise ValidationError("CNPJ Inválido")

        inteiros = list(map(int, cnpjAlterado))
        novo = inteiros[:12]

        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        while len(novo) < 14:
            r = sum([x * y for (x, y) in zip(novo, prod)]) % 11
            if r > 1:
               f = 11 - r
            else:
               f = 0
            novo.append(f)
            prod.insert(0, 6)

        if novo == inteiros:
            return cnpj
        raise ValidationError("CNPJ Inválido")


#Formulario que possui o campo nome
class PesquisaParceiro(forms.Form):

    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '200'}),
        required=False)






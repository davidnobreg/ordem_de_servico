from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['name', 'documento', 'email', 'fone', 'is_ativo']

    def clean_documento(self):
        documento = self.cleaned_data['documento']
        documento = ''.join(filter(str.isdigit, documento))  # apenas números

        if len(documento) == 11:
            if not self.instance.validar_cpf(documento):
                raise ValidationError("CPF inválido")
        elif len(documento) == 14:
            if not self.instance.validar_cnpj(documento):
                raise ValidationError("CNPJ inválido")
        else:
            raise ValidationError("Documento deve ter 11 dígitos (CPF) ou 14 dígitos (CNPJ)")

        return documento

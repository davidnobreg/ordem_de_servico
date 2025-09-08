from django.core.validators import RegexValidator
from django.db import models

## Cadastro de Fabricantes
class Fabricante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


## Cadastro de Veículos
class Veiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    Cor = models.CharField(max_length=100)
    ano_fabricacao = models.PositiveIntegerField()
    placa = models.CharField(
        max_length=7,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$',
                message='Placa inválida. Formato esperado: ABC1D23'
            )
        ]
    )
    chassi = models.CharField(
        max_length=17,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-HJ-NPR-Z0-9]{17}$',
                message='Chassi inválido. Deve conter 17 caracteres alfanuméricos.'
            )
        ]
    )
    is_ativo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
        ordering = ['id']

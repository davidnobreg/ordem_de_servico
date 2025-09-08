from django.contrib import admin
from .models import Fabricante, Veiculo


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("id", "modelo", "fabricante", "ano_fabricacao", "placa", "chassi", "is_ativo")
    list_filter = ("fabricante", "ano_fabricacao", "is_ativo")
    search_fields = ("modelo", "placa", "chassi")
    ordering = ("id",)
    list_editable = ("is_ativo",)  # permite ativar/desativar direto na listagem
    list_per_page = 20  # paginação para não ficar gigante

    fieldsets = (
        ("Informações do Veículo", {
            "fields": ("fabricante", "modelo", "ano_fabricacao", "placa", "chassi")
        }),
        ("Status", {
            "fields": ("is_ativo",)
        }),
    )

from django.urls import path  # adicionar include
from .views import lista_cliente

urlpatterns = [
    # Cadastro de cliente
    path('listar_clientes/', lista_cliente, name='lista_cliente'),

    # path('cadastrar_cliente/', views.criarCliente, name='criar-cliente'),
    # path('update/<int:cliente_id>/', views.alteraCliente, name='altera-cliente'),
    # path('delete_cliente/<int:id>/', views.deleteCliente, name='delete-cliente'),

    # path('select/<int:cliente_id>/', views.selectCliente, name='select-cliente'),
    # path('listar_clientes_relatorio/', views.listaClienteRelatorio, name='lista-cliente-relatorio'),
    # path('listar_clientes_filtro/', views.reports, name='lista-cliente-filtro'),
]

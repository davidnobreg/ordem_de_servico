from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Cliente
from .serializers import ClienteSerializer

# Função view
def clientes(request):
    clientes = Cliente.objects.all()  # Pega todos os clientes cadastrados
    # Pode passar um contexto para o template se quiser
    contexto = {
        'clientes': clientes
    }
    return render(request, 'lista_clientes.html', contexto)

# Paginação personalizada
class ClientePagination(PageNumberPagination):
    page_size = 10  # número de clientes por página
    page_size_query_param = 'page_size'  # permite alterar pelo query param
    max_page_size = 100

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    pagination_class = ClientePagination

    # Filtros e ordenação
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['nome', 'is_ativo', 'documento']
    ordering_fields = ['nome', 'documento']
    ordering = ['nome']  # ordenação padrão

    # List personalizado
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # aplica filtros
        page = self.paginate_queryset(queryset)  # aplica paginação

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

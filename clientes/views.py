from django.shortcuts import render, redirect
from django.http import HttpResponse

def lista_cliente(request):
    return render(request, 'lista_cliente.html')
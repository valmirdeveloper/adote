from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse('Ola estou no cadastro')

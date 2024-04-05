from django.shortcuts import render
from django.http import HttpResponse



def home(requeste):
    return HttpResponse('Home 1')

def sobre(requeste):
    return HttpResponse('sobre')

def contato(requeste):
    return HttpResponse('Contato 3')


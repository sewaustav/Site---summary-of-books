from django.http import HttpResponse
from django.shortcuts import render, redirect

def main(request):
    data = {
        'title': 'Ессе',
        'text': 'Добро пожаловать!!!',
    }
    return render(request, 'content/main.html', data)

def accounts(request):

    return render(request, 'content/profile.html')
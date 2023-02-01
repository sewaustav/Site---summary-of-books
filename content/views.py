from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Content
from django.contrib.auth.models import User
from .forms import CreateForm, SignUpForm, LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from aiogram.utils.mixins import DataMixin
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from django.db.models import Q

# Create your views here.
class ContentView(DetailView):
    model = Content
    template_name = 'content/all_story.html'
    context_object_name = "content"

def create_post(request):
    error = ''
    form = CreateForm(request.POST)
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ok")
        else:
            error = "Ошибка"
            form = CreateForm()
    data = {
        "title": "Добавить",
        "form": form,
        "error": error,
    }
    return render(request, 'content/createform.html', data)

def show_all(request):
    base = Content.objects.all()
    data = {
        'story': base,
        'title': 'Краткое содержание' 
    }
    return render(request, 'content/story.html', data)

def ok(request):
    data = {
        'title': 'OK',
        'text1': 'Ваш шаблон успешно отправлен.',
        'text2': 'В ближайшее время наши модераторы рассмотрят ваш текст.',
    }
    return render(request, 'content/ok.html', data)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            return redirect('login')
    else:
        print('invalid form')
        form = SignUpForm()
    data = {
        "form": form,
        "title": "Sign up",
    }
    return render(request, 'content/signup.html', data)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return redirect('signup')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'content/login.html', {'form': form})

def test(request):
    data = {
        'title': 'Test',
        'text': 'Test text from content-app',
    }
    return render(request, 'content/test.html', data)

def post_search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('q')
        if query == '':
            query = 'None'
        results = Content.objects.filter(Q(autor__icontains=query) | Q(title__icontains=query))
    return render(request, 'content/search.html', {'query': query,
                                                'results': results,})
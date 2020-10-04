from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import LoginForm, UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


def work(request):
    return render(request, 'work.html')


def about(request):
    return render(request, 'about_us.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            # Profile.objects.create(user=new_user)
            return render(request,
                          'register.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'register.html',
                  {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Аутентификация прошла успешно')
            else:
                return HttpResponse('Неверный аккаунт')
        else:
            return HttpResponse('Неверный логин')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
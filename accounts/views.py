from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    return render(request, 'registration/login.html', {'form': form, 'message': 'Неактивный аккаунт'})
            else:
                return render(request, 'registration/login.html',
                              {
                                'form': form,
                                'message': 'Не удалось войти. Убедитесь что ввели верные Логин и Пароль'
                              })
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
    return HttpResponseRedirect("/")




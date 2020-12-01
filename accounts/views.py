from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from urllib.parse import urlencode


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
        message = request.GET.get("scmsg")
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form, 'scmsg': message})


def user_logout(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
    return HttpResponseRedirect("/")


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            url_param = urlencode({'scmsg': 'Вы успешно зарегистрировались.\nТеперь вы можете войти в свой аккаунт'})
            http_response = HttpResponseRedirect(f'/login?{url_param}')

            return http_response
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def change_user_information(request):
    if request.method == 'GET':
        user = request.user
        user_form = UserRegistrationForm()
        user_form.first_name.initial = user.first_name
        user_form.last_name.initial = user.last_name
        user_form.email.initial = user.email


from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'title': 'HOMIC - Авторизация'
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'HOMIC - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'HOMIC - Кабинет'
    }
    return render(request, 'users/profile.html', context)



def logout(request):
    pass
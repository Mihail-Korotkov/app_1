from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'HOMIK',
        'content':'Магазин мебели HOME'
        }

    return render(request,'main/index.html',context)

def about(request):
    context = {
        'title':'HOMIK - about',
        'content':'о нас:',
        'about_us':'о том какой хороший магазин и тд.'
        }

    return render(request,'main/about.html',context)

def contact_information(request):
    context = {
        'title':'HOMIK - contacts',
        'content':'контакты:',
        'adress_tel':'косой переулок д.6, тел.6-78-77'
    }

    return render(request,'main/contact_information.html',context)

def pay(request):
    context = {
        'title':'HOMIK - how2pay',
        'content':'как платить:',
        'pay':'деньгами (желательно)'
    }

    return render(request,'main/pay.html',context)

from django.shortcuts import render


# Create your views here.
def hello(request):
    return render(request, 'hello02.html', {'name':'파이썬'})


def var01(request):
    lst = ['Python' , 'Django', 'Template']
    return render(request, 'variable01.html', {'lst':lst})


def var02(request):
    dct = {'class':'qclass' , 'name': '최태준'}
    return render(request, 'variable02.html', {'dct':dct})


def forLoop(request):
    return render(request, 'for.html', {'numbers':range(1, 10)})

def if01(request):
    return render(request,'if01.html',{"user":{"id":"test","name":"최태준"}})

def if02(request):
    return render(request,'if02.html',{'role':'student'})

def href(request):
    return render(request,'href.html')

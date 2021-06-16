from django.shortcuts import render,redirect
from .models import Myboard
from django.utils import timezone

def index(request):
    return render(request,'index.html',{'list':Myboard.objects.all()})

def get(request,id):
    return render(request,'select.html',{'dto':Myboard.objects.get(id=id)})

def update_form(request,id):
    return render(request,'update.html',{'dto':Myboard.objects.get(id=id)})

def update_res(request):
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']
    
    myboard = Myboard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_content = myboard.update(mycontent=mycontent)
    
    if result_title + result_content == 2:
        return redirect('select/'+id)
    else :
        return redirect('updateform/'+id)

def delete(request,id):
    result_delete = Myboard.objects.filter(id=id).delete()
    
    if result_delete[0] == 1:
        return redirect('index')
    else :
        return redirect('detail/'+id)

def insert_form(request):
    return render(request,'insert.html')

def insert_res(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']
    
    result = Myboard.objects.create(myname=myname,
                                    mytitle=mytitle,
                                    mycontent=mycontent,
                                    mydate=timezone.now())
    
    if result :
        return redirect('index')
    else :
        return redirect('insertform')
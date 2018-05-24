from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render
from .models import Todo 

# Create your views here.

def index(request):
    user = request.user
    if user.is_authenticated():
        todos = Todo.objects.filter(user=user)
        context={
            'todos': todos
        }
        return render(request,'todos/index.html',context)
    else :
        return redirect('/login/')
        

def add(request):    
        if(request.method == 'POST'):
            if request.user.is_authenticated():
                Title = request.POST['Title']
                Description = request.POST['Description']
                todo = Todo(Title=Title, Description=Description, user = request.user)
                todo.save()
                return redirect('/todos')
            else:
                return redirect('/login/')
        else:
            return render(request,'todos/add.html')


def edit(request, pk):
    if (request.method=='GET'):    
        if request.user.is_authenticated():
            todo = Todo.objects.filter(id=pk).filter(user=request.user).first()
            context={
                'todos': todo
                }
            return render(request,'todos/edit.html',context)
        else:
            return redirect('/login/')     

    elif (request.method=='POST'):
        if request.user.is_authenticated():
            Title = request.POST['Title']
            Description = request.POST['Description']
            todo = Todo.objects.get(id=pk,user=request.user)
            todo.Title = Title
            todo.Description = Description        
            todo.save()
            return redirect('/todos/')
        else:
            return redirect('/login/')


def delete(request, pk):
    if request.user.is_authenticated():
        todo = Todo.objects.get(id=pk,user=request.user)
        todo.delete()
        return redirect('/todos/')
    else:
        return redirect('/login/')


def detail(request, pk):
    if request.user.is_authenticated():
        todo = Todo.objects.get(id=pk,user=request.user)
        context = {
            'todo':todo
        }
        return render(request, 'todos/detail.html', context)
    else:
        return redirect('/login/')


##Delete via form###
# def delete(request, pk):
#     if (request.method=='GET'):
#         todo = Todo.objects.filter(id=pk).first()
#         context={
#             'todos': todo
#             }
#         return render(request,'todos/delete.html',context) 
        
#     if (request.method=='POST'):
#         Title = request.POST['Title']
#         Description = request.POST['Description']
#         todo = Todo.objects.get(id=pk)
#         todo.Title = Title
#         todo.Description = Description        
#         todo.delete()
#         return redirect('/todos/')
























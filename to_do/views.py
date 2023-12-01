from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
from .forms import TaskForms
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import UpdateView

@login_required(login_url='signin')
def taskList(request):
    username=request.session.get('logged_in_username', None)
    print(username)
    if username:
        task=Task.objects.all()
        form=TaskForms()
        print('jere')
        if request.method=="POST":
            print("??")
            form=TaskForms(request.POST)
            form.instance.user = request.user

            print(form.is_valid())
            if form.is_valid():
                print('ii')
                print('kkki')
                form.save()
                print("saved")
                return redirect('all-tasks')
        
        context={'tasks':task,'form':form}
        return render(request,'to_do/lists.html',context)

def todoHome(request):
    return render(request,'base.html')

@login_required(login_url='signin')
def allTasks(request):
    username=request.session.get('logged_in_username', None)
    if username:
        user=User.objects.get(username=username)
        user_id = user.pk
        all_tasks=Task.objects.filter(user_id=user_id).order_by('complete')

        return render(request,'home.html',{'all_tasks':all_tasks})




def taskcompleted(request):

    if request.POST.get('action')=='post':
        print(request.POST.get('product_id'))
        product_id=request.POST.get('product_id')
        task=get_object_or_404(Task,id=product_id)
        task.complete=True
        task.save()
        response=JsonResponse({'task':str(task)})
        return response

def taskdelete(request):
    if request.POST.get('action')=='post':
        product_id=request.POST.get('product_id')
        task = get_object_or_404(Task, id=product_id)
        task.delete()
        username=request.session.get('logged_in_username', None)
        if username:
            user=User.objects.get(username=username)
            
            user_id = user.pk
            all_tasks=Task.objects.filter(user_id=user_id)
            response=JsonResponse({'task':str(all_tasks)})
            return response 
        

def taskedit(request):
    
    if request.POST.get('action')=='post':
        print('hii')
        product_id=request.POST.get('product_id')
        product_title=request.POST.get('product_title')
        task = get_object_or_404(Task, id=product_id)
        task.title=product_title
        task.save()
        username=request.session.get('logged_in_username', None)
        if username:
            user=User.objects.get(username=username)
            
            user_id = user.pk
            all_tasks=Task.objects.filter(user_id=user_id)
            response=JsonResponse({'task':str(all_tasks)})

            return response 







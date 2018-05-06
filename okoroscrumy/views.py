from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from .models import ScrumyGoal,Task,ScrumyUser,Role,GoalStatus
from django.db import transaction
import simplejson
from .forms import AddUser,AddTask



def index(request,template_name='index.html'):
    #for lab 11
    try:
        scrumy_user_list = ScrumyUser.objects.all()
    except BaseException as e:
        raise e.message

    #for lab 12
    scrumy_total_count=len(scrumy_user_list)
    try:
        for i in range(1,scrumy_total_count):
            scrumy_user=ScrumyUser.objects.get(id=i)
    except BaseException:
        raise

    #for lab13
    scrumy_user=scrumy_user_list[0]
    status=GoalStatus.objects.get(status="weekly target")
    scrumy_goals=scrumy_user.scrumygoal_set.filter(status_id=status.id)
    print("len goal", scrumy_goals[0].user_id.full_name)


    return render(request, template_name, {'scrumy_goals': scrumy_goals})


# def add_task(request):
#     try:
#         task=Task()
#         task.description="design all the user interface"
#         task.save()
#         transaction.commit()
#     except:
#         transaction.rollback()
#         raise



def move_Task(request,task_id):
    obj = Task.objects.get(id=task_id)
    return HttpResponse(obj.description)

# def add_user(request):
#     try:
#         user=ScrumyUser()
#         role=Role.objects.get(id=1)
#         user.full_name="okoro ugochukwu"
#         user.email="ugdesmond@gmail.com"
#         user.password="desmond"
#         user.user_name="michael"
#         user.role=role
#         user.save()
#     except:
#         transaction.rollback()
#         raise
#     else:
#         transaction.commit()
#     finally:
#         transaction.set_autocommit(True)
#
#     scrumy_user_list=ScrumyUser.objects.all()
#     output = ', '.join([eachuser.user_name for eachuser in scrumy_user_list])
#     return HttpResponse(output)





def add_user(request,template_name="add_user.html"):
    roles = Role.objects.all()
    if request.method == 'POST':
        add_user_form = AddUser(request.POST)
        if add_user_form.is_valid():
            add_user_form.save()
            users = ScrumyUser.objects.all()
            return render(request, template_name, {'msg': "User created successfully",'scrumy_users':users,'roles':roles})
        else:
            users = ScrumyUser.objects.all()
            return render(request, template_name, {'form':add_user_form, 'scrumy_users': users,'roles':roles})

    else:
        users=ScrumyUser.objects.all()

        return render(request, template_name,{'scrumy_users':users,'roles':roles})


def add_task(request,template_name="add_task.html"):

    if request.method == 'POST':
        add_task_form = AddTask(request.POST)
        if add_task_form.is_valid():
            user=ScrumyUser.objects.get(pk=1)
            new_task=add_task_form.save(commit=False)
            new_task.created_by=user
            new_task.save()
            tasks = Task.objects.all()
            return render(request, template_name,
                          {'msg': "Task created successfully", 'tasks': tasks,})
        else:
            tasks = Task.objects.all()
            return render(request, template_name, {'form': add_task_form, 'tasks': tasks})

    else:
        tasks = Task.objects.all()
        return render(request, template_name, {'tasks': tasks})



def edit_task(request,task_id,template_name="edit_task.html"):

    if request.method == 'POST':
        task_update = Task.objects.get(pk=task_id)
        add_task_form = AddTask(request.POST,instance=task_update)
        if add_task_form.is_valid():
            add_task_form.save()
            tasks = Task.objects.all()
            return render(request,"add_task.html",
                          {'msg': "Task updated successfully", 'tasks': tasks,})
        else:
            task = Task.objects.get(pk=task_id)
            return render(request, template_name, {'form': add_task_form, 'tasks': task})

    else:
        task = Task.objects.get(pk=task_id)
        return render(request, template_name, {'task': task,'task_id':task_id})







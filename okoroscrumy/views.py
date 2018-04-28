from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from .models import ScrumyGoal,Task,ScrumyUser,Role
from django.db import transaction
import simplejson



def index(request):
    try:
        scrummy_goal_list = ScrumyGoal.objects.all()
    except BaseException as e:
        raise e.message
    return HttpResponse(scrummy_goal_list[0].description)


def move_goal(request,task_id):
    obj = Task.objects.get(id=task_id)
    return HttpResponse(obj.description)

def add_user(request):
    try:
        user=ScrumyUser()
        role=Role.objects.get(id=1)
        user.full_name="okoro ugochukwu"
        user.email="ugdesmond@gmail.com"
        user.password="desmond"
        user.user_name="michael"
        user.role=role
        user.save()
    except:
        transaction.rollback()
        raise
    else:
        transaction.commit()
    finally:
        transaction.set_autocommit(True)

    scrumy_user_list=ScrumyUser.objects.all()
    output = ', '.join([eachuser.user_name for eachuser in scrumy_user_list])
    return HttpResponse(output)



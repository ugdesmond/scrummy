from django.db import models
from enum import Enum

# Create your models here.

class GoalStatus (models.Model):

    status=models.TextField(null=False)


class Role(models.Model):
    description=models.TextField()


    def __repr__(self):
        return '<Status %r>' % self.status


class ScrumyUser(models.Model):

    full_name = models.CharField(max_length=100)
    email=models.CharField(max_length=100,null=True)
    user_name=models.CharField(max_length=50,null=True)
    role=models.ForeignKey(Role,on_delete=models.CASCADE,null=True)

class Task(models.Model):
    description=models.TextField()
    status=models.CharField(max_length=50)
    # created_on = models.DateTimeField(auto_now=True)
    # updated_on = models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(ScrumyUser,on_delete=models.CASCADE)


class ScrumyGoal(models.Model):
    user_id=models.ForeignKey(ScrumyUser,on_delete=models.CASCADE)
    status_id=models.ForeignKey(GoalStatus,on_delete=models.CASCADE)
    description=models.TextField()
    task_id=models.ForeignKey(Task,on_delete=models.CASCADE)
    created_on=models.DateTimeField()
    updated_on=models.DateTimeField(null=True)


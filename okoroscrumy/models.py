from django.db import models

# Create your models here.

class GoalStatus (models.Model):

    status=models.TextField(null=False)


class Role(models.Model):
    description=models.TextField()


    def __repr__(self):
        return '<Status %r>' % self.status


class ScrumyUser(models.Model):

    full_name = models.TextField(max_length=200)
    email=models.TextField(blank=True)
    user_name=models.TextField(null=True)
    password=models.TextField(null=False)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)

class Task(models.Model):
    description=models.TextField()
    created_by=models.ForeignKey(ScrumyUser,on_delete=models.CASCADE)


class ScrumyGoal(models.Model):
    user_id=models.ForeignKey(ScrumyUser,on_delete=models.CASCADE)
    status_id=models.ForeignKey(GoalStatus,on_delete=models.CASCADE)
    description=models.TextField()
    task_id=models.ForeignKey(Task,on_delete=models.CASCADE)
    created_on=models.DateTimeField()
    updated_on=models.DateTimeField(null=True)


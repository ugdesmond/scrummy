from django.contrib import admin
from .models import ScrumyUser,ScrumyGoal,GoalStatus,Task

# Register your models here.

admin.site.register(ScrumyUser)
admin.site.register(ScrumyGoal)
admin.site.register(GoalStatus)
admin.site.register(Task)

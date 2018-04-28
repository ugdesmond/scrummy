from django.urls import path,include
from okoroscrumy import  views
urlpatterns = [
path('index/', views.index),
path('movegoal/<int:task_id>/',views.move_goal),
path('add_user/',views.add_user)
]

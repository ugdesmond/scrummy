from django.urls import path
from okoroscrumy import  views
urlpatterns = [
path('index/', views.index,name='index'),
path('add_task/', views.add_task,name='add_task'),
path('edit_task/<int:task_id>/', views.edit_task,name='edit_task'),
path('movegoal/<int:task_id>/', views.move_Task),
path('add_user/', views.add_user,name='add_user')
]

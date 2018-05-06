from django.forms import ModelForm
from .models import ScrumyUser,Task




class AddUser(ModelForm):

    class Meta:
        model = ScrumyUser
        fields = ['user_name','email','full_name','role']


class AddTask(ModelForm):

    class Meta:
        model = Task
        fields = ['description','status']
from django import forms
from django.contrib.auth.models import User
from myapp.models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=['title','deadline']
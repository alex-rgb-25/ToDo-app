from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import ToDoList


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","password1", "password2"]
        widgets = {
            "sent_to" : forms.TextInput(attrs={'class':'form-control', 'placeholder':""}),
        }

    #clear helper messages
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class ToDoForm(forms.Form):
    todo = forms.CharField(label="todo", max_length=200, required=False,
    widget=forms.TextInput(attrs={'placeholder': 'add new todo'}))

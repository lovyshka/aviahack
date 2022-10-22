from .models import Users
from django.forms import ModelForm

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['login', 'passwords']
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import Customer


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Customer
        fields = ('name', 'email', 'number')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Employee
        fields = ('name',)
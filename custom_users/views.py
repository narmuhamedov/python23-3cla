from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from custom_users.forms import RegistrationForm, LoginForm

# для регистрации
class Registation(CreateView):
    # form_class = UserCreationForm
    form_class = RegistrationForm
    success_url = "/users/"
    template_name = "registration.html"


# для входа через логин
class NewLoginView(LoginView):
    # form_class = AuthenticationForm
    form_class = LoginForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse("users:user_list")


# для списка наших пользователей
class UserListView(ListView):
    queryset = User.objects.all()
    template_name = "user_list.html"

    def get_queryset(self):
        return User.objects.all()

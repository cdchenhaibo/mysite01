from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth import views as auth_views


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {'form': form})


class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    template_name = 'accounts/settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class UserPasswordChangeView(auth_views.PasswordChangeView):
    model = User
    fields = ('old_password', 'new_password1', 'new_password2')
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')

    def get_object(self):
        return self.request.user


class UserPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
    title = '密码修改成功！'

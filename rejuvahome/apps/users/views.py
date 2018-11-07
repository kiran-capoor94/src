from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.views.generic import FormView, CreateView

from .forms import LoginForm, RegisterForm

class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'users/login.html'
    # default_next = '/'

    def form_valid(self, form):
        request = self.request
        
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None

        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = '/login/'
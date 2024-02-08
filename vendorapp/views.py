from vendorapp.models import User
from vendorapp.forms import VendorRegistrationForm,LoginForm
from django.contrib import messages
from django.shortcuts import render,redirect

from django.views.generic import FormView,TemplateView,ListView,CreateView,DetailView,UpdateView,View
from django.urls import reverse_lazy,reverse
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def is_admin(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            messages.error(request,"permission denied for current user!!")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


class signUpView(CreateView):
    template_name="register.html"
    model=User
    form_class=VendorRegistrationForm
    success_url=reverse_lazy("signin")

    def form_valid(self,form):
        form.instance.user_type="company"
        messages.success(self.request,"company account created successfully")
        return super().form_valid(form)
    

def signin_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'home' with the name of your home page URL pattern
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def signout_view(request):
    logout(request)
    return redirect('signup')  # Replace


class IndexView(TemplateView):
    template_name="index.html"




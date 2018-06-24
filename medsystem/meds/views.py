from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Category, Profile
from .forms import AdviceModelForm, ProfileModelForm


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "meds/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "meds/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class IndexView(View):
    def get(self, request):
        
        if request.user.is_authenticated:
            try:
                profile = self.request.user.profile
            except Profile.DoesNotExist:
                return redirect('/add_profile')
        categories = Category.objects.all()
        for cat in categories:
            doctors = cat.get_doctors
            for doc in doctors:
                print(doc.user.profile.last_name)
            
        return render(request, 'meds/index.html', {
            "categories": categories
        })


class AdviceCreateView(CreateView):
    form_class = AdviceModelForm
    template_name = 'meds/advice.html'
    success_url = "/advices"


class ProfileCreateView(CreateView):
    form_class = ProfileModelForm
    template_name = 'meds/profile.html'
    success_url = "/profile"


class ProfileView(UpdateView):
    form_class = ProfileModelForm
    template_name = 'meds/profile.html'
    success_url = "/profile"

    def get_object(self, queryset=None):
        obj = Profile.objects.filter(user=self.request.user).first()
        return obj
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data["form"] = ProfileModelForm(instance=self.object)
        return data




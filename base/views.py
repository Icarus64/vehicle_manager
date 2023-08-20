from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Vehicle
from .mixins import ViewMixin, CreateMixin, DeleteMixin, EditMixin

# Create your views here.


class VehicleLogin(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('vehicle_list')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self, form):
        user = form.save()
        
        if user is not None:
            user_group = Group.objects.get(name='User')
            user.groups.add(user_group)
            login(self.request, user)
        
        if self.request.user.is_authenticated:
            return redirect('vehicle_list')
        
        return super().form_valid(form)
    




class VehicleList(ViewMixin, LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'base/vehicle_list.html'
    context_object_name = 'vehicles'


class VehicleCreate(CreateMixin, LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'base/vehicle_form.html'
    fields = '__all__'
    success_url = reverse_lazy('vehicle_list')

class VehicleDetail(ViewMixin, LoginRequiredMixin, DetailView):
    model = Vehicle
    context_object_name = 'vehicle'
    template_name = "base/vehicle_detail.html"

class VehicleUpdate(EditMixin, LoginRequiredMixin, UpdateView):
    model = Vehicle
    template_name = 'base/vehicle_update.html'  
    fields = '__all__'
    context_object_name = 'vehicle'
    success_url = reverse_lazy('vehicle_list')

class VehicleDelete(DeleteMixin, LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'base/vehicle_confirm_delete.html'
    context_object_name = 'vehicle'
    success_url = reverse_lazy('vehicle_list') 


class NoPermissionView(View):
    template_name = 'base/error_403.html'
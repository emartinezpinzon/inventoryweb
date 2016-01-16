# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, ListView
from forms import LoginForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from models import Product


class LoginView(FormView):
    """Vista de Login de la aplciacion. """
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')

    def get(self, request):
        data = {'form': self.form_class}
        return render(request, self.template_name, data)

    def post(self, request):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                if user is not None and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(self.success_url)
        else:
            form = LoginForm()

        return HttpResponseRedirect(reverse('login'))


class DashboardView(TemplateView):
    """Vista dashboard de la aplicación"""
    template_name = "dashboard.html"


class ProductView(ListView):
    template_name = "productos.html"
    model = Product
    context_object_name = 'products'


login_view = LoginView.as_view()
dashboard_view = DashboardView.as_view()
products_view = ProductView.as_view()
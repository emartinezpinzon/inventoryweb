# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from forms import LoginForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponseRedirect


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
                    print self.success_url, "IMPRIMIENDO EL SELF.SUCCES_URL"
                    return HttpResponseRedirect(self.success_url)
        else:
            form = LoginForm()

        return HttpResponseRedirect(reverse('login'))


class DashboardView(TemplateView):
    """Vista dashboard de la aplicación"""
    template_name = "dashboard.html"


login_view = LoginView.as_view()
dashboard_view = DashboardView.as_view()
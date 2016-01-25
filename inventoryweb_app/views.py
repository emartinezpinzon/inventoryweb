# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, ListView, View
from forms import LoginForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponseRedirect, HttpResponse
from models import Product, Category
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class LoginView(FormView):
    """Vista de Login de la aplicacion. """
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


class ProductView(View):
    """Mustra los nombre de los productos con su respectiva información"""
    template_name = "productos.html"

    def get(self, request, *args, **kwargs):
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 10) # Muestra 10 productos por página

        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # si el parametro page no es un int.
            products = paginator.page(1)
        except EmptyPage:
            # si la pag esta fuera de rango devuelve la ultima por default.
            products = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'products': products})

class CategoryView(ListView):
    """Mustra las categorias en la que estan agrupada los diferentes productos"""
    template_name = "categorias.html"
    model = Category
    context_object_name = 'categorys'


class SellView(ListView):
    """Modulo para realizar las ventas de Productos"""
    model = Product
    template_name = "vender.html"


def search_product(request):
    """LLamada ajax que consulta por nombre de producto
        Retorna un JSON con la información de la busqueda."""
    if request.method == 'POST' or request.is_ajax():
        product_name = request.POST.get('product_name', '')
        #  SQL 'like' en django  "__contains"
        result = Product.objects.filter(name__contains=product_name)
        data = serializers.serialize("json", result)
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse("ERROR")


login_view = LoginView.as_view()
dashboard_view = DashboardView.as_view()
products_view = ProductView.as_view()
categorys_view = CategoryView.as_view()
sell_view = SellView.as_view()
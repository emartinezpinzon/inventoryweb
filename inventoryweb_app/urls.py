from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('inventoryweb_app.views',
                       url(r'^$', 'login_view', name="login"),
                       url(r'^dashboard/$', 'dashboard_view', name="dashboard"),
                       url(r'^productos/$', 'products_view', name="products"),
                       url(r'^categorias/$', 'categorys_view', name="categorys"),
                       url(r'^vender/$', 'sell_view', name="sells"),
                       url(r'^buscar_producto/$', 'search_product', name="search_products")
                       )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

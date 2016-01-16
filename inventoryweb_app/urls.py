from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('inventoryweb_app.views',
                       url(r'^$', 'login_view', name="login"),
                       url(r'^dashboard/$', 'dashboard_view', name="dashboard"),
                       url(r'^produtos/$', 'products_view', name="products"),
                       )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Goden_Store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('core.urls')),
    url(r'', include('cadastro.urls')),
    url(r'', include('estoque.urls')),
    url(r'', include('login.urls')),
    url(r'', include('vendas.urls')),

]

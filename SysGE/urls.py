from django.conf.urls import patterns, include, url
from django.contrib import admin
from report_builder import urls
from django.views.generic import TemplateView
from django.conf import settings

#I18NJS_URL = getattr(settings, 'I18NJS_URL', "i18njs/")

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SysGE.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # tiene que estar antes del admin para que funcione los selects
    #url(r'^report_builder/', include('report_builder.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^report_builder/', include(urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    #url(r'^%s' % I18JS_URL, 'django.views.i18n.javascript_catalog'),
    #INICIO
    url(r'^', include('apps.inicio.urls')),
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^asistencias/', include('apps.asistencias.urls')),
)

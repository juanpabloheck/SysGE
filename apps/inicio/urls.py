from django.conf.urls import url, patterns
from django.views.generic import TemplateView
from .views import Inicio

urlpatterns = patterns('',
    #url(r'^&', TemplateView.as_view(template_name='inicio/index.html')),
    url(r'^', Inicio.as_view()),
    #(r'^about/', AboutView.as_view()),
    url(r'^/(?P<theme>)$', Inicio, name='inico'),
)

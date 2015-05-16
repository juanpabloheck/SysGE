from django.shortcuts import render
from bootstrap_themes import list_themes, themes
from django.views.generic import TemplateView

class Inicio(TemplateView):
    template_name = "inicio/index.html"
    #theme = list_themes()
    #theme = models.CharField(default='default', choices=list_themes())
    #def get_context_data(self, **kwargs):
    #    context = super(Inicio, self).get_context_data(**kwargs)
    #    context['theme'] = self.theme
    #    return context

#def Inicio(request):
    #if request.method == 'POST':
    #    tema = request.POST['theme']
    #    themes = tema
#        pass





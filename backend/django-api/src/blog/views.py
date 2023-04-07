from django.views.generic.base import View  #Importar clase vistas generica
from django.shortcuts import render


# Create your views here.
class HelloWorld(View):

    def get(self, request):
        data = {
            'name': 'Daniel Mauricio Diaz Forero',
            'years': 42,
            'codes': ['Python', 'Django', 'React', 'VueJS']
        }
        return render(request, 'index.html', context=data)

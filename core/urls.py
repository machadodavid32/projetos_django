from django.urls import path

from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto')
]

"""Este arquivo foi criado por mim para configurar as rotas (que fiz dentro do arquivo views) dentro de 'core'
pois, profissionalmente fica melhor pois não é indicado colocar varias rodas na pasta 'django1' (urls)"""





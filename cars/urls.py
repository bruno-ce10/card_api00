from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.views import BrandModelViewSet, CarModelViewSet

router = DefaultRouter()
router.register('brands', BrandModelViewSet) # criando uma rota no sistema /brand
router.register('cars', CarModelViewSet) # outra rota no sistema /cars

urlpatterns = [
    path('', include(router.urls)), # é o caminho pra acesar as rotas
]

# models, urls, views e serializers se comunicam um com outro pra criar o API

# models é o banco de dados onde fica as tabelas

# urls é as rotas do projeto que apontam p uma view

# views é onde vai ta a logica da rota, busca os dados no banco de dados, prepara e devolve uma resposta p usuario em JSON com o serializer
# DRF ModelViewSet melhor opçao cria um CRUD completo, criar, buscar, adicionar, excluir e listar.

# views usa o serializer pra serializar os dados e devolver em formato de JSON p usuario
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, EditoraViewSet, LivroViewSet, AutorViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'autores', AutorViewSet)   


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
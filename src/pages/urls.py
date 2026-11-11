from django.urls import path, include
from .views import CrearGuia, ActualizarGuia, EliminarGuia, ObtenerGuia
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register("api/obtener-guia", ObtenerGuia, basename="obtener-guia")
router.register("api/crear-guia", CrearGuia, basename="crear-guia")
router.register("api/actualizar-guia", ActualizarGuia, basename="actualizar-guia")
router.register("api/eliminar-guia", EliminarGuia, basename="eliminar-guia")


urlpatterns = [
  path("", include(router.urls))
]

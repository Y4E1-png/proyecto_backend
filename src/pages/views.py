from rest_framework.viewsets import ViewSet
from .serializers import GuideSerializer
from rest_framework import status
from .models import Guide
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class CrearGuia (ViewSet):

  serializer_class = GuideSerializer

  def create (self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response (serializer.data, status= status.HTTP_201_CREATED)
    else:
      return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class ActualizarGuia (ViewSet):

  serializer_class = GuideSerializer

  def update (self, request, pk=None):
    datos = get_object_or_404(Guide, pk=pk)
    serializer = self.serializer_class(datos,data=request.data )

    if serializer.is_valid():
      serializer.save()
      return Response (serializer.data)
    else:
      return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class ObtenerGuia (ViewSet):

  serializer_class = GuideSerializer

  def retrieve(self, request, pk=None):
    datos = get_object_or_404(Guide, pk=pk)
    serializer = self.serializer_class(datos)
    return Response(serializer.data)


class EliminarGuia (ViewSet):

  serializer_class = GuideSerializer

  def destroy(self, request, pk=None):
    datos = get_object_or_404(Guide, pk=pk)
    datos.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)

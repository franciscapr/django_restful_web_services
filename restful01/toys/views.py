from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from toys.models import Toy
from toys.serializers import ToySerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONRenderer, self).__init__(content, **kwargs)

@csrf_exempt
def toy_list(request):
    if request.method == 'GET':
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)    # many=True especifica que deben serializarse varias instancias, no solo una
        return JSONRenderer(toys_serializer.data)
    
    elif request.method == 'POST':    # La respuesta viene en formato json
        toy_data = JSONParser().parse(request)    # con parse la convertimos en formato dic
        toy_serializer = ToySerializer(data=toy_data)    # con el serializador convertimos el dic en un objeto
        if toy_serializer.is_valid():    # verificamos si es valid
            toy_serializer.save()    # guardamos en la bd
            return JSONResponse(toy_serializer.data,    
                                status=status.HTTP_201_CREATED)
        return JSONResponse(toy_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def toy_detail(request, pk):   # tenemos pk como argumento y request. pk-->identificador
    try:
        toy = Toy.objects.get(pk=pk)    # recuperamos el objeto segun el pk y lo guardamos en toy
    except Toy.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        toy_serializer = ToySerializer(toy)
        return JSONResponse(toy_serializer.data)
    
    elif request.method == 'PUT':
        toy_data = JSONParser().parse(request)
        toy_serializer = ToySerializer(toy, data=toy_data)
        if toy_serializer.is_valid():
            toy_serializer.save()
            return JSONResponse(toy_serializer.data)
        return JSONResponse(toy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        toy.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
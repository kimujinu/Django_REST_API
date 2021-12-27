import random

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Example
from .serializers import ExampleSerializer

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello")

@api_view(['GET'])
def randomReturn(request,id):
    totalcount = Example.objects.all()
    randomcount = random.sample(list(totalcount),id)
    serializer = ExampleSerializer(randomcount,many=True) # many=True 다수의 데이터에 대해서도 직렬화
    return Response(serializer.data)
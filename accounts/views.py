# from django.shortcuts import render //we dont need render function because we are using API view (creating API)

from rest_framework.decorators import api_view
from rest_framework.response import Response  #this Response for JSON serialize
from .serializers import UserSerializer

@api_view(['POST'])
def register_user(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


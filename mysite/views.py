from django.http import JsonResponse
from .models import Person
from .serializer import PersonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class PersonList(APIView):
    def get(self, request, format=None):
        snippets = Person.objects.all()
        serializer = PersonSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def people(request, iin):
    snippet = Person.objects.get(iin=iin)
    serializer = PersonSerializer(snippet)
    return JsonResponse(serializer.data)

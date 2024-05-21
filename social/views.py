from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PersonSerializer
from .models import Person


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

from django.shortcuts import render
from .models import House, ContactUs
from .serializers import HouseSerializer, ContactUsSerializer
from rest_framework import generics


class ListHouseView(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class DetailHouseView(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class CreateContactView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

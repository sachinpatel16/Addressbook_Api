from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework import generics
from api.models import Addres
from api.serializer import AddresSerializer

def home(request):
    return HttpResponse("This is home")
def index(request):
    return HttpResponse("This is index")

#Create
class AddresSerializerCView(generics.CreateAPIView):
    queryset = Addres.objects.all()
    serializer_class = AddresSerializer

#Read
class AddresSerializerRView(generics.ListAPIView):
    queryset = Addres.objects.all()
    serializer_class = AddresSerializer
    
class AddresSerializerRtView(generics.RetrieveAPIView):
    queryset = Addres.objects.all()
    serializer_class = AddresSerializer
    lookup_field ="pk"

#Update
class AddresSerializerUView(generics.RetrieveUpdateAPIView):
    queryset = Addres.objects.all()
    serializer_class = AddresSerializer
    lookup_field = 'pk'

#Delete
class AddresSerializerDView(generics.DestroyAPIView):
    queryset = Addres.objects.all()
    serializer_class = AddresSerializer
    lookup_field = 'pk'
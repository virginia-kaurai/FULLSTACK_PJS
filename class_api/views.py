
from django.shortcuts import render
from urllib import request

from .serializers import ClassDetailSerializer, ClassSerializer
from classroom.models import Class ,ClassDetail
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import generics



def index(request):
    return render(request, 'index.html')

class ClassList(ListCreateAPIView):
   queryset = Class.class_objects.all()
   serializer_class = ClassSerializer
   pass



class ClassDetail(RetrieveDestroyAPIView):
   queryset = ClassDetail.objects.all()
   serializer_class = ClassDetailSerializer
   pass
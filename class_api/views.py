
from django.shortcuts import render
from urllib import request

from .serializers import ClassDetailSerializer, ClassSerializer, StudentSerializer, TeacherSerializer
from classroom.models import Class ,ClassDetail,Student,Teacher
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser



def index(request):
    return render(request, 'index.html')

class ClassList(ListCreateAPIView):
   permission_classes = [IsAdminUser]  
   queryset = Class.class_objects.all()
   serializer_class = ClassSerializer
   pass



class ClassDetail(RetrieveDestroyAPIView):
   queryset = ClassDetail.objects.all()
   serializer_class = ClassDetailSerializer
   pass

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pass

class StudentDetail(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pass

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pass   

class TeacherDetail(generics.RetrieveDestroyAPIView):
      queryset = Teacher.objects.all()
      serializer_class = TeacherSerializer
      pass

class SubjectList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pass
class SubjectDetail(generics.RetrieveDestroyAPIView):
      queryset = Teacher.objects.all()
      serializer_class = TeacherSerializer
      pass

class EnrollmentList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pass


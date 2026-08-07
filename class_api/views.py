
from django.shortcuts import render
from urllib import request
from rest_framework.permissions import SAFE_METHODS, BasePermission 
from .serializers import ClassDetailSerializer, ClassSerializer, StudentSerializer, TeacherSerializer
from classroom.models import Class ,ClassDetail,Student,Teacher
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser



class IsAdminUserOrReadOnly(BasePermission):
      message = "Only admins can make changes"

      def has_permission(self, request, view):
        return request.user.is_authenticated

      def has_object_permission(self, request, view, obj):

          if request.method in SAFE_METHODS:
              return True
          return request.user.role == "admin"

class IsTeacherOrAdmin(BasePermission):
    message ="restricted access"

    def has_object_permission(self, request, view, obj):
     if request.method in SAFE_METHODS:
         return True
     return request.user.role in ["teacher","admin"]
        


class IsOwnerOrAdmin(BasePermission):

    message = "You can only access your own information."

def has_permission(self, request, view):
        return request.user.is_authenticated

def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return obj.user == request.user

        return obj.user == request.user or request.user.role == "admin"
        
def index(request):
    return render(request, 'index.html')

class ClassList(ListCreateAPIView):
   permission_classes = [IsAdminUserOrReadOnly]  
   queryset = Class.class_objects.all()
   serializer_class = ClassSerializer
   pass



class ClassDetail(RetrieveDestroyAPIView):
   permission_classes = [IsAdminUserOrReadOnly]
   queryset = ClassDetail.objects.all()
   serializer_class = ClassDetailSerializer
   pass

class StudentList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pass

class StudentDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrAdmin]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pass

class TeacherList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pass   

class TeacherDetail(generics.RetrieveDestroyAPIView):
      permission_classes = [IsOwnerOrAdmin]
      queryset = Teacher.objects.all()
      serializer_class = TeacherSerializer
      pass

class SubjectList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pass
class SubjectDetail(generics.RetrieveDestroyAPIView):
      permission_classes = [IsAdminUserOrReadOnly]
      queryset = Teacher.objects.all()
      serializer_class = TeacherSerializer
      pass

class EnrollmentList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrAdmin]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pass


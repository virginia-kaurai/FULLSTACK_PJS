from django.urls import path ,include


from . import views

urlpatterns = [
    path('classes/', views.ClassList.as_view(), name='ClassList'),
    path('classes/<int:pk>/', views.ClassDetail.as_view(), name='ClassDetail'),
    path('students/', views.StudentList.as_view(), name='StudentList'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='StudentDetail'),
    path('teachers/', views.TeacherList.as_view(), name='TeacherList'),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view(), name='TeacherDetail'),
    path('subjects/', views.SubjectList.as_view(), name='SubjectList'),
    path('subjects/<int:pk>/', views.SubjectDetail.as_view(), name='SubjectDetail'),
    path('enrollments/', views.EnrollmentList.as_view(), name='EnrollmentList'),
   
]
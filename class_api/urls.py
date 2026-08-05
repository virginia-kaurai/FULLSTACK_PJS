from django.urls import path

from . import views

urlpatterns = [
    path('classes/', views.ClassList, name='ClassList'),
    path('classes/<int:class_id>/', views.ClassDetail, name='ClassDetail'),
]
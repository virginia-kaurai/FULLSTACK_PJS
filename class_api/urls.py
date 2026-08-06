from django.urls import path


from . import views

urlpatterns = [
    path('classes/', views.ClassList.as_view(), name='ClassList'),
    path('classes/<int:pk>/', views.ClassDetail.as_view(), name='ClassDetail'),
]
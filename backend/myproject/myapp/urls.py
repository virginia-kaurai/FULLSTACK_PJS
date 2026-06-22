from django.urls import path
from . import views


urlpatterns=[

    path('person/', views.PersonView.as_view()),
    path('transaction/', views.TransactionView.as_view()),
    path('referral-code/', views.ReferralCodeView.as_view())
]
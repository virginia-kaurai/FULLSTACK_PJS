from django.shortcuts import render
from rest_framework.permissions import AllowAny
from .serializers import PersonSerializer, ReferralCodeSerializer, TransactionSerializer
from .models import person, transaction, referral_code
from rest_framework import generics

class PersonView(generics.ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [AllowAny]    

class TransactionView(generics.ListCreateAPIView):
    queryset = transaction.objects.all()
    serializer_class = TransactionSerializer

class ReferralCodeView(generics.ListCreateAPIView):
    queryset = referral_code.objects.all()
    serializer_class = ReferralCodeSerializer
    permission_classes = [AllowAny]    

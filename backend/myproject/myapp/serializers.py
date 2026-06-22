from rest_framework import serializers
from .models import  person, referral_code, transaction



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = '__all__'

class ReferralCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = referral_code
        fields = '__all__'

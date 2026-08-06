from rest_framework import serializers
from classroom.models import Class, ClassDetail , Faculty


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class ClassDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassDetail
        fields = '__all__'


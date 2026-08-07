from rest_framework import serializers
from classroom.models import Class, ClassDetail, Enrollment , Faculty, Student ,Results


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class ClassDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClassDetail
        fields = '__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class ResultsSerializer(serializers.Serializer):
    class Meta:
        model = Results
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
     class Meta:
        model = Enrollment
        fields = '__all__'       

   



               

from rest_framework import serializers
from .models import *

class RegPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterPatient
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','phone','qualification','specialist',)

class AnalysisPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisPatient
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
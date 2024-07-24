from rest_framework import serializers
from .models import projectInstance

class ProjectInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectInstance
        fields = '__all__'

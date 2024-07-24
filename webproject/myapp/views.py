from rest_framework import viewsets
from .models import projectInstance
from .serializers import ProjectInstanceSerializer

class ProjectInstanceViewSet(viewsets.ModelViewSet):
    queryset = projectInstance.objects.all()
    serializer_class = ProjectInstanceSerializer


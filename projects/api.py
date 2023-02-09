from .models import Project
from rest_framework import viewsets,permissions
from .serializers import ProjectSirializer

class ProjectViewSet(viewsets.ModelViewSet): #Que consultas se van a poder hacer 
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny] #Cualquier cliente o aplicacion cliente va a poder solicitar datos a mi servidor
    #permission_classes = [permissions.IsAuthenticated] #Solo si esta autenticado puede hacer la query
    serializer_class = ProjectSirializer

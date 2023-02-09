from rest_framework import serializers
from .models import Project

#Los serializers son contenedores que nos permiten tomar tipos de datos complejos, convertirlos en datos nativos de python para después poderlos usar como JSON o XML

class ProjectSirializer(serializers.ModelSerializer): #Convierte el modelo en datos que van a ser consultados
    class Meta:
        model = Project
        fields = ('id','title','description','technology','create_at') 
        read_only_fields = ('create_at', ) #Indica que el campo es solo de lectura(la coma es importante,sino lo lee como si fuera un str)

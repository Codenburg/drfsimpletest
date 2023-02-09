from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/project',ProjectViewSet,'projects') #rutas creadas por router. Genera 4 urls, 1 para delete otra para get,post y put

urlpatterns = router.urls 

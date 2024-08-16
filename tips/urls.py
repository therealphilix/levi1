from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('tips', views.TipViewSet)
router.register('programminglanguage', views.ProgrammingLanguageViewSet)

urlpatterns = router.urls
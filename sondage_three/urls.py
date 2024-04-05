from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, ChoixViewSet, ReponseViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choix', ChoixViewSet)
router.register(r'reponses', ReponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import SondageTwoListCreateView, SondageTwoDetailView, ReponseTwoCreateView, ReponseTwoDetailView, ReponseTwoListView

urlpatterns = [
    path('', SondageTwoListCreateView.as_view(), name='sondage-list-create'),
    path('<int:pk>/', SondageTwoDetailView.as_view(), name='sondage-detail'),
    path('reponses/', ReponseTwoCreateView.as_view(), name='reponse-create'),
    path('reponses/all/', ReponseTwoListView.as_view(), name='reponse-list'),
    path('reponses/<int:pk>/', ReponseTwoDetailView.as_view(), name='reponse-detail'),

]

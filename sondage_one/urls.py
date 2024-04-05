from django.urls import path, include
from sondage_one.views import SondageListCreateView, SondageDetailView, AnswerCreateView, SondageResultsView, SondageDetailSimpleView  


urlpatterns = [
        path('sondages/', SondageListCreateView.as_view(), name='creation-de-sondage'), 
        path('sondages/<int:pk>/', SondageDetailView.as_view(), name='sondage-detail'),
        path('sondages/choix/', AnswerCreateView.as_view(), name='choix-sondage'),
        path('sondages/<int:pk>/resultats/', SondageResultsView.as_view(), name='resulats-sondages'),
        path('sondages/<slug:slug>/', SondageDetailSimpleView.as_view(), name='sondage-detail'),
        
]

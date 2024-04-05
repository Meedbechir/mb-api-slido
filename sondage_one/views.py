from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from sondage_one.models import Sondage, Answer  
from sondage_one.serializers import SondageSerializer, AnswerSerializer, SimpleSondageSerializer 
from rest_framework import generics
from rest_framework.permissions import AllowAny

class SondageListCreateView(generics.ListCreateAPIView):
    queryset = Sondage.objects.all()
    serializer_class = SondageSerializer

    def perform_create(self, serializer):
        print("Données reçues:", self.request.data)
        sondage = serializer.save()
        print("Sondage :", sondage)
        survey_url = sondage.get_survey_url()
        return Response({'survey_url': survey_url})


class SondageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sondage.objects.all()
    serializer_class = SondageSerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        sondage_id = self.kwargs.get('pk')
        answers = Answer.objects.filter(sondage=sondage_id)
        print("Answers for sondage_id {}:".format(sondage_id), answers)
        answer_serializer = AnswerSerializer(answers, many=True)
        response.data['answers'] = answer_serializer.data
        return response
    
class SondageDetailSimpleView(generics.RetrieveAPIView):
    queryset = Sondage.objects.all()
    serializer_class = SimpleSondageSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        print("Données reçues:", self.request.data) 
        sondage_id = self.request.data.get('sondage_id')
        choix = self.request.data.get('choix') 
        serializer.save(sondage_id=sondage_id, choix=choix)
        print("Answer saved with sondage_id:", sondage_id)



class SondageResultsView(APIView):
    def get(self, request, pk, format=None):
        answers = Answer.objects.filter(sondage=pk)
        print("Answers for sondage_id {}:".format(pk), answers) 
        answer_serializer = AnswerSerializer(answers, many=True)

        response_data = {
            'sondage_id': pk,
            'answers': answer_serializer.data,
        }
        
        return Response(response_data, status=status.HTTP_200_OK)


from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .models import SondageTwo, QuestionTwo, ReponseTwo
from .serializers import SondageTwoSerializer, QuestionTwoSerializer, ReponseTwoSerializer

class SondageTwoListCreateView(generics.ListCreateAPIView):
    queryset = SondageTwo.objects.all()
    serializer_class = SondageTwoSerializer

    def perform_create(self, serializer):
        print("Données reçues:", self.request.data)
        sondage = serializer.save()
        print("Sondage :", sondage)
        survey_url = sondage.get_survey_url()

        question_data_list = self.request.data.get('question', [])
        for question_data in question_data_list:
            question_text = question_data.get('question', '')
            if question_text:
                question_data = {'question': question_text}
                question_serializer = QuestionTwoSerializer(data=question_data)
                if question_serializer.is_valid():
                    question = question_serializer.save(sondage=sondage)
                    print("Question created:", question)
                else:
                    print("Question data is not valid:", question_serializer.errors)

        questions = QuestionTwo.objects.filter(sondage=sondage.id)
        question_serializer = QuestionTwoSerializer(questions, many=True)
        response_data = {'survey_url': survey_url, 'questions': question_serializer.data}

        return Response(response_data, status=status.HTTP_201_CREATED)




class SondageTwoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SondageTwo.objects.all()
    serializer_class = SondageTwoSerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        sondage_id = self.kwargs.get('pk')
        questions = QuestionTwo.objects.filter(sondage=sondage_id)
        print("Questions for sondage_id {}:".format(sondage_id), questions)
        question_serializer = QuestionTwoSerializer(questions, many=True)
        response.data['questions'] = question_serializer.data
        return response

class ReponseTwoCreateView(generics.CreateAPIView):
    queryset = ReponseTwo.objects.all()
    serializer_class = ReponseTwoSerializer

    def perform_create(self, serializer):
        question_id = self.request.data.get('question', None)
        if question_id:
            serializer.save(question_id=question_id)
        else:
            return Response(
                {"error": "L'ID de la question est manquant."},
                status=status.HTTP_400_BAD_REQUEST
            )
    
class ReponseTwoListView(generics.ListAPIView):
    queryset = ReponseTwo.objects.all()
    serializer_class = ReponseTwoSerializer

class ReponseTwoDetailView(generics.RetrieveAPIView):
    queryset = ReponseTwo.objects.all()
    serializer_class = ReponseTwoSerializer
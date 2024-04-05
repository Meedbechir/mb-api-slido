from rest_framework import viewsets
from .models import QuestionThree, ChoixThree, ReponseThree
from .serializers import QuestionSerializerThree, ChoixSerializerThree, ReponseSerializerThree
from rest_framework.response import Response
from rest_framework import status

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = QuestionThree.objects.all()
    serializer_class = QuestionSerializerThree

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question_data = serializer.validated_data

        choices_data = question_data.pop('choix', [])
        correct_answer = question_data.pop('correct_answer', None)

        question_instance = QuestionThree.objects.create(**question_data)

        for choice_data in choices_data:
            ChoixThree.objects.create(question=question_instance, **choice_data)

        if correct_answer:
            question_instance.correct_answer = correct_answer
            question_instance.save()

        question_serializer = self.get_serializer(question_instance)
        response_data = question_serializer.data
        return Response(response_data, status=status.HTTP_201_CREATED)

class ChoixViewSet(viewsets.ModelViewSet):
    queryset = ChoixThree.objects.all()
    serializer_class = ChoixSerializerThree

class ReponseViewSet(viewsets.ModelViewSet):
    queryset = ReponseThree.objects.all()
    serializer_class = ReponseSerializerThree

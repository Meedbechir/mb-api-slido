from rest_framework import serializers
from .models import QuestionThree, ChoixThree, ReponseThree

class ChoixSerializerThree(serializers.ModelSerializer):
    class Meta:
        model = ChoixThree
        fields = ['id', 'choix', 'question']

class QuestionSerializerThree(serializers.ModelSerializer):
    choix = ChoixSerializerThree(many=True, read_only=True)

    class Meta:
        model = QuestionThree
        fields = ['id', 'question', 'choix', 'correct_answer', 'choix']

class ReponseSerializerThree(serializers.ModelSerializer):
    class Meta:
        model = ReponseThree
        fields = ['id', 'reponse', 'question']

from rest_framework import serializers
from .models import SondageTwo, QuestionTwo, ReponseTwo

class QuestionTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTwo
        fields = ['question']

class ReponseTwoSerializer(serializers.ModelSerializer):
    question = QuestionTwoSerializer(read_only=True)

    class Meta:
        model = ReponseTwo
        fields = ['id', 'reponse', 'question']

class SondageTwoSerializer(serializers.ModelSerializer):
    questions = QuestionTwoSerializer(many=True, read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = SondageTwo
        fields = ['id', 'title', 'questions', 'slug']

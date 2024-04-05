from rest_framework import serializers
from sondage_one.models import Sondage, Answer

# Med Bechir
class AnswerSerializer(serializers.ModelSerializer):
    sondage_id = serializers.IntegerField(write_only=True)
    choix = serializers.ListField(child=serializers.CharField(max_length=200), read_only=True)

    class Meta:
        model = Answer
        fields = ['choix', 'created_at', 'sondage_id']

    def validate_choix(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Les choix doivent être une liste.")

        sondage_id = self.initial_data.get('sondage_id')
        sondage = Sondage.objects.get(pk=sondage_id)
        valid_options = sondage.options

        for choice in value:
            if choice not in valid_options:
                raise serializers.ValidationError(f"{choice} n'est pas une option valide pour ce sondage.")

        return value



class SondageSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False) 
    slug = serializers.SlugField(read_only=True)  

    class Meta:
        model = Sondage
        fields = ['id', 'question', 'options', 'answers', 'slug']

class SimpleSondageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sondage
        fields = ['id', 'question', 'options']

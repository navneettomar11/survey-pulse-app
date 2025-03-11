from rest_framework.serializers import ModelSerializer
from apis_v1.models import AnswerModel
from apis_v1.serializers import ChoiceSerializer


class AnswerSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = AnswerModel
        fields = ['type', 'choices']

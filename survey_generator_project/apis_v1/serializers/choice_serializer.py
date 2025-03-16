from rest_framework.serializers import ModelSerializer

from apis_v1.models import ChoiceModel
from apis_v1.serializers import AnswerSerializer


class ChoiceSerializer(ModelSerializer):
    answer = AnswerSerializer(read_only=True)

    class Meta:
        model = ChoiceModel
        fields = ['text', 'sequence_no', 'answer']

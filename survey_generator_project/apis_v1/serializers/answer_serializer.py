from rest_framework.serializers import ModelSerializer
from apis_v1.models import AnswerModel
from apis_v1.serializers import QuestionSerializer


class AnswerSerializer(ModelSerializer):
    question = QuestionSerializer(read_only=True)

    class Meta:
        model = AnswerModel
        fields = ['type', 'question']

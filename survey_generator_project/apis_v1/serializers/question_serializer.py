from rest_framework.serializers import ModelSerializer
from apis_v1.models import QuestionModel


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ['sequence_no', 'text', 'helpText', 'answers']

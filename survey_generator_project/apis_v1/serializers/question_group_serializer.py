from rest_framework.serializers import ModelSerializer
from apis_v1.models import QuestionGroupModel
from apis_v1.serializers import QuestionSerializer


class QuestionGroupSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionGroupModel
        fields = ['number_of_questions', 'questions']

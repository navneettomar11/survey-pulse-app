from rest_framework.serializers import ModelSerializer
from apis_v1.models import QuestionGroupModel
from apis_v1.serializers import SectionSerializer


class QuestionGroupSerializer(ModelSerializer):
    section = SectionSerializer(read_only=True)

    class Meta:
        model = QuestionGroupModel
        fields = ['id','number_of_questions', 'section']

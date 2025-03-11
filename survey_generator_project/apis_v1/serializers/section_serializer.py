from rest_framework.serializers import ModelSerializer

from apis_v1.models import SectionModel
from apis_v1.serializers import QuestionGroupSerializer


class SectionSerializer(ModelSerializer):
    groups = QuestionGroupSerializer(many=True, read_only=True)

    class Meta:
        model = SectionModel
        fields = ['title', 'body', 'groups']

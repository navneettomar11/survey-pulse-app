from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from apis_v1.models import SectionModel, SurveyModel
from apis_v1.serializers import SurveySerializer


class SectionSerializer(ModelSerializer):
    survey = SurveySerializer(read_only=True)
    class Meta:
        model = SectionModel
        fields = ['id', 'title', 'body', 'survey']
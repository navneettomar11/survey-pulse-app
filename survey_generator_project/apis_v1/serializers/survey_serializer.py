from rest_framework.serializers import ModelSerializer

from apis_v1.models import SurveyModel
from . import SectionSerializer


class SurveySerializer(ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = SurveyModel
        fields = ['name', 'description', 'sections']

from rest_framework.serializers import ModelSerializer

from apis_v1.models import SurveyModel


class SurveySerializer(ModelSerializer):
    class Meta:
        model = SurveyModel
        fields = ['name', 'description']

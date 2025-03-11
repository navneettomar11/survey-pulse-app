from rest_framework.viewsets import ModelViewSet

from apis_v1.models import SurveyModel
from apis_v1.serializers import SurveySerializer


class SurveyViewSet(ModelViewSet):
    queryset = SurveyModel.objects.all()
    serializer_class = SurveySerializer

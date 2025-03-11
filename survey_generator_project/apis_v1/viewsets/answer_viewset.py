from rest_framework.viewsets import ModelViewSet

from apis_v1.models import AnswerModel
from apis_v1.serializers import AnswerSerializer


class AnswerViewSet(ModelViewSet):
    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer

from rest_framework.viewsets import ModelViewSet

from apis_v1.models import QuestionGroupModel
from apis_v1.serializers import QuestionGroupSerializer


class QuestionGroupViewSet(ModelViewSet):
    queryset = QuestionGroupModel.objects.all()
    serializer_class = QuestionGroupSerializer

from rest_framework.viewsets import ModelViewSet

from apis_v1.models import QuestionModel
from apis_v1.serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

from rest_framework.viewsets import ModelViewSet

from apis_v1.models import ChoiceModel
from apis_v1.serializers import ChoiceSerializer


class ChoiceViewSet(ModelViewSet):
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoiceSerializer

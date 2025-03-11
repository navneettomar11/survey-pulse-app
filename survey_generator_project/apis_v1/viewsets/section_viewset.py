import sys

from rest_framework.viewsets import ModelViewSet
from apis_v1.models import SectionModel
from apis_v1.serializers import SectionSerializer


class SectionViewSet(ModelViewSet):
    queryset = SectionModel.objects.all()
    serializer_class = SectionSerializer

    def retrieve(self, request, *args, **kwargs):
        print("Goodbye cruel world!",kwargs, file=sys.stderr)

        surveyId = kwargs['surveyId']
        return super().retrieve(request, *args, **kwargs)



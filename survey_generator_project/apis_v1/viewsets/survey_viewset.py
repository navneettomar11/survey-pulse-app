from apis_v1.models import SurveyModel
from apis_v1.serializers import SurveySerializer
from apis_v1.viewsets import BaseViewSet


class SurveyViewSet(BaseViewSet):
    serializer_class = SurveySerializer

    def initial(self, request, *args, **kwargs):
        self.queryset = SurveyModel.objects.all()

        survey_id = self.get_id(kwargs)
        if survey_id is not None:
            self.instance = self.get_instance(SurveyModel, survey_id)

        super().initial(request, args, kwargs)
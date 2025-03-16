import logging

from apis_v1.models import SectionModel, SurveyModel
from apis_v1.serializers import SectionSerializer
from apis_v1.viewsets import BaseViewSet


class SectionViewSet(BaseViewSet):
    serializer_class = SectionSerializer
    parent_instance_name = 'survey'
    logger = logging.getLogger(__name__)

    def initial(self, request, *args, **kwargs):
        survey_id = self.get_id(kwargs, 'surveys_pk')
        self.logger.debug(f"Survey ID {survey_id}")
        survey_not_found_exception_message = ("A survey is necessary for a section to exist. Please provide accurate "
                                              "survey data.")
        if survey_id is None:
            self.raise_exception(survey_not_found_exception_message)

        self.queryset = SectionModel.objects.filter(survey_id=survey_id).distinct()
        self.parent_instance = self.get_instance(SurveyModel, survey_id)
        if self.parent_instance is None:
            self.raise_exception(survey_not_found_exception_message)

        section_id = self.get_id(kwargs)
        self.logger.debug(f"Section ID {section_id}")
        if section_id is not None:
            self.instance = self.get_instance(SectionModel, section_id)

        super().initial(request, args, kwargs)


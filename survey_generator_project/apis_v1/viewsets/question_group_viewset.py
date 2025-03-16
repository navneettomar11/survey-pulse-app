import logging

from apis_v1.models import QuestionGroupModel, SectionModel
from apis_v1.serializers import QuestionGroupSerializer
from apis_v1.viewsets import BaseViewSet


class QuestionGroupViewSet(BaseViewSet):
    serializer_class = QuestionGroupSerializer
    section_model: SectionModel = None
    parent_instance_name = 'section'
    logger = logging.getLogger(__name__)

    def initial(self, request, *args, **kwargs):
        section_id = self.get_id(kwargs, 'sections_pk')
        self.logger.debug(f"Section ID {section_id}")
        section_not_found_exception = ("A section is necessary for question groups to function. Pass the validate "
                                       "section, please.")
        if section_id is None:
            self.raise_exception(section_not_found_exception)
        self.queryset = QuestionGroupModel.objects.filter(section_id=section_id).distinct()
        self.parent_instance = self.get_instance(SectionModel, section_id)
        if self.parent_instance is None:
            self.raise_exception(section_not_found_exception)

        group_id = self.get_id(kwargs)
        self.logger.debug(f"Question Group ID {group_id}")
        if group_id is not None:
            self.instance = self.get_instance(QuestionGroupModel, group_id)

        super().initial(request, args, kwargs)

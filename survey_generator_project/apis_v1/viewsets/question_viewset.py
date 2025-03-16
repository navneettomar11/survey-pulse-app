from apis_v1.exceptions import NotFoundException
from apis_v1.models import QuestionModel, QuestionGroupModel
from apis_v1.serializers import QuestionSerializer
from apis_v1.viewsets import BaseViewSet


class QuestionViewSet(BaseViewSet):
    serializer_class = QuestionSerializer
    parent_instance_name = 'group'

    def initial(self, request, *args, **kwargs):
        question_group_id = self.get_id(kwargs, 'groups_pk')
        question_group_not_found_exception = ("There cannot be a question without a group. Please give a legitimate "
                                              "question group.")
        if question_group_id is None:
            self.raise_exception(question_group_not_found_exception)

        self.parent_instance = self.get_instance(QuestionGroupModel, question_group_id)
        if self.parent_instance is None:
            self.raise_exception(question_group_not_found_exception)

        self.queryset = QuestionModel.objects.filter(group_id=question_group_id).distinct()

        question_id = self.get_id(kwargs)
        if question_id is not None:
            try:
                self.instance = self.get_instance(QuestionModel, question_id)
            except Exception as e:
                raise NotFoundException("Question instance not found")
        super().initial(request, args, kwargs)

from apis_v1.exceptions import NotFoundException
from apis_v1.models import QuestionModel, AnswerModel
from apis_v1.serializers import AnswerSerializer
from apis_v1.viewsets import BaseViewSet


class AnswerViewSet(BaseViewSet):
    serializer_class = AnswerSerializer
    parent_instance_name = 'question'

    def initial(self, request, *args, **kwargs):
        question_id = self.get_id(kwargs, 'questions_pk')
        question_not_found_exception = "Without question, the answer is impossible. Please ask a legitimate question."
        if question_id is None:
            self.raise_exception(question_not_found_exception)

        self.parent_instance = self.get_instance(QuestionModel, question_id)
        if self.parent_instance is None:
            self.raise_exception(question_not_found_exception)

        self.queryset = AnswerModel.objects.filter(question_id=question_id).distinct()

        answer_id = self.get_id(kwargs)
        if answer_id is not None:
            try:
                self.instance = self.get_instance(AnswerModel, answer_id)
            except:
                raise NotFoundException("Answer instance not found")

        super().initial(request, args, kwargs)
from apis_v1.exceptions import NotFoundException
from apis_v1.models import ChoiceModel, AnswerModel
from apis_v1.serializers import ChoiceSerializer
from apis_v1.viewsets import BaseViewSet


class ChoiceViewSet(BaseViewSet):
    serializer_class = ChoiceSerializer
    parent_instance_name = 'answer'

    def initial(self, request, *args, **kwargs):
        answer_id = self.get_id(kwargs, 'answers_pk')
        answe_not_found_exception = ("An answer is mandatory for the type selection, dropdown, etc. choices. Please "
                                     "give specific information about your response.")
        if answer_id is None:
            self.raise_exception(answe_not_found_exception)

        self.parent_instance = self.get_instance(AnswerModel, answer_id)
        if self.parent_instance is None:
            self.raise_exception(answe_not_found_exception)

        self.queryset = ChoiceModel.objects.filter(answer_id=answer_id).distinct()

        choice_id = self.get_id(kwargs)
        if choice_id is not None:
            try:
                self.instance = self.get_instance(ChoiceModel, choice_id)
            except:
                raise NotFoundException("Choice instance not found")

        super().initial(request, args, kwargs)
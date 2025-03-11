from django.db.models import CharField, ForeignKey, CASCADE, IntegerField
from . import BaseModel, AnswerModel


class ChoiceModel(BaseModel):
    answer = ForeignKey(AnswerModel, on_delete=CASCADE)
    text = CharField(max_length=100)
    sequence_no = IntegerField()

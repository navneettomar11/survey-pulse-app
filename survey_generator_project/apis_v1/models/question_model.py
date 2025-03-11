from django.db.models import IntegerField, TextField, ForeignKey, CASCADE, SET_NULL
from . import BaseModel
from .question_group_model import QuestionGroupModel


class QuestionModel(BaseModel):
    sequence_no = IntegerField(default=0)
    text = TextField(blank=False, null=False)
    helpText = TextField(blank=True, null=True)
    parent = ForeignKey("QuestionModel", null=True, on_delete=SET_NULL)
    group = ForeignKey(QuestionGroupModel, on_delete=CASCADE)
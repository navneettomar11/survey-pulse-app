from django.db.models import ForeignKey, CASCADE, CharField
from . import BaseModel, QuestionModel

ANSWER_TYPES = (
    ('TEXTBOX', 'Text'),
    ('SINGLE_CHOICE', 'Single Choice'),
    ('MULTIPLE_CHOICE', 'Multiple Choice'),
    ('DROPDOWN', 'Dropdown'),
    ('RANGE', 'Range'),
)


class AnswerModel(BaseModel):
    question = ForeignKey(QuestionModel, on_delete=CASCADE)
    type = CharField(max_length=30, choices=ANSWER_TYPES)

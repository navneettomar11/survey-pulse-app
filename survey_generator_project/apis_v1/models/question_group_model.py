from django.db.models import ForeignKey, IntegerField, CASCADE
from django.core.validators import MaxValueValidator
from . import BaseModel, SectionModel


class QuestionGroupModel(BaseModel):
    section = ForeignKey(SectionModel, on_delete=CASCADE)
    number_of_questions = IntegerField(default=1, validators=[MaxValueValidator(12,
                                                                                "Number of question per group should be less than 12")])

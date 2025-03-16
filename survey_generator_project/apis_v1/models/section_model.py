from django.db.models import CharField, TextField, ForeignKey, CASCADE
from . import BaseModel,SurveyModel


class SectionModel(BaseModel):
    title = CharField(max_length=100, blank=True, null=True)
    body = TextField(blank=True, null=True)
    survey = ForeignKey(to=SurveyModel, on_delete=CASCADE)

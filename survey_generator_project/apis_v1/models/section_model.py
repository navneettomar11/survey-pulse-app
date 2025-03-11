from django.db.models import SlugField, TextField, ForeignKey, CASCADE
from . import BaseModel,SurveyModel


class SectionModel(BaseModel):
    title = SlugField(blank=True, null=True)
    body = TextField(blank=True, null=True)
    survey = ForeignKey(to=SurveyModel, on_delete=CASCADE)

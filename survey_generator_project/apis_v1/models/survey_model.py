from django.db.models import SlugField, TextField
from .base_model import BaseModel


class SurveyModel(BaseModel):
    name = SlugField(max_length=80, unique=True)
    description = TextField(blank=True, null=True)


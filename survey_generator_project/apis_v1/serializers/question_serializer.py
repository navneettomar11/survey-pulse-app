from rest_framework.serializers import ModelSerializer, IntegerField
from apis_v1.models import QuestionModel
from apis_v1.serializers import QuestionGroupSerializer


class QuestionSerializer(ModelSerializer):
    group = QuestionGroupSerializer(read_only=True)
    parent_id = IntegerField(required=False)

    class Meta:
        model = QuestionModel
        fields = ['id', 'sequence_no', 'text', 'helpText', 'group', 'parent_id']

from rest_framework.serializers import ModelSerializer

from apis_v1.models import ChoiceModel


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = ChoiceModel
        fields = ['text', 'sequence_no']

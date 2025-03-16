from typing import Any

from django.db.models import Model
from rest_framework.viewsets import ModelViewSet


class BaseViewSet(ModelViewSet):
    parent_instance: Model = None
    parent_instance_name = None
    instance: Model = None

    def get_object(self):
        return self.instance

    @classmethod
    def get_id(self, kwargs, key='pk'):
        parent_id = kwargs.get(key, None)
        if parent_id is None:
            return None
        return int(parent_id)

    @classmethod
    def get_instance(self, model, pk):
        instance = model.objects.filter(id=pk).first()
        if instance is None:
            raise Exception('Instance not found')
        return instance

    def raise_exception(self, message):
        raise Exception(message)

    def perform_create(self, serializer):
        if self.parent_instance_name is not None and self.parent_instance is not None:
            kwargs = {self.parent_instance_name : self.parent_instance}
            serializer.save(**kwargs)
        else:
            serializer.save()

    def perform_update(self, serializer):
        if self.parent_instance_name is not None and self.parent_instance is not None:
            kwargs = {self.parent_instance_name: self.parent_instance}
            serializer.save(**kwargs)
        else:
            serializer.save()

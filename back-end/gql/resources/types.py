from graphene_django import DjangoObjectType
from resources.models import Resource


class ResourceType(DjangoObjectType):
    class Meta:
        model = Resource
        only_fields = (
            'id',
            'title',
            'body',
            'created_at',
        )
        use_connection = True
from graphene import Argument, Field, ID, ObjectType, Schema
from graphene_django import DjangoConnectionField
from resources.models import Resource
from .resources.types import ResourceType


class Query(ObjectType):
    resources = DjangoConnectionField(ResourceType, filterset_class=ResourceFilter)
    resource = Field(ResourceType, id=Argument(ID, required=True))
    
    def resolve_resources(root, info, **kwargs):
        return Resource.objects.all()
    
    def resolve_resource(root, info, **kwargs):
        return Resource.objects.get(id=kwargs.get('id'))
    
schema = Schema(query=Query)
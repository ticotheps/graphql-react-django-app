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
    
    def resolve_is_old(root, *args):
        return root.created_at < (timezone.now() - timezone.timedelta(days=666))
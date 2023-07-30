from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from ..core.models import ModelWithMetadata, PublishableModel

class Client(TenantMixin, ModelWithMetadata, PublishableModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    
    class Meta(ModelWithMetadata.Meta):
        ordering = ('name',)
    
class Domain(DomainMixin):
    pass
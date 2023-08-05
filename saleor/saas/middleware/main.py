from django_tenants.middleware.main import TenantMainMiddleware as BaseTenantMainMiddleware
from django.conf import settings
from django.db import connections


class TenantMainMiddleware(BaseTenantMainMiddleware):
    def process_request(self, request):
        super().process_request(request)
        try:
            alias = settings.DATABASE_CONNECTION_REPLICA_NAME
            if settings.DATABASES.get(alias):
                self._set_tenant_to_replicas(request, alias)
        except AttributeError:
            pass
        
    def _set_tenant_to_replicas(self, request, alias: str) -> None:
        connection = connections.__getitem__(alias)
        connection.set_schema_to_public()
        if connection and hasattr(request, "tenant"):
            connection.set_tenant(request.tenant)
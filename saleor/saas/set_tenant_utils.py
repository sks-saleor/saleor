from django.db import connections


def extra_set_tenant_stuff(wrapper_class, tenant):
    """
    you can add stuff when the connection is set such as read replica

    :return:
    """
    # print(f"changing replica schema to {tenant.schema_name}")
    pass
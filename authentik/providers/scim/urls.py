"""API URLs"""

from authentik.providers.scim.api.property_mappings import SCIMMappingViewSet
from authentik.providers.scim.api.providers import SCIMProviderViewSet

api_urlpatterns = [
    ("providers/scim", SCIMProviderViewSet),
    ("propertymappings/scim", SCIMMappingViewSet),
]

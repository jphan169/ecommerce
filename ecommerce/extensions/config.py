from __future__ import absolute_import

from oscar import config
from oscar.core.application import OscarConfig


class EdxShop(config.Shop):
    name = "ecommerce"
    # URLs are only visible to users with staff permissions
    default_permissions = 'is_staff'

    # Override core app instances with blank application instances to exclude their URLs.
    promotions_app = OscarConfig()
    catalogue_app = OscarConfig()
    search_app = OscarConfig()

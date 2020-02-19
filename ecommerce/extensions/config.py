from __future__ import absolute_import
from django.apps import apps
from oscar import config
from oscar.core.application import OscarConfig


class EdxShop(config.Shop):
    name = "ecommerce"
    # URLs are only visible to users with staff permissions
    default_permissions = 'is_staff'

    def ready(self):
        super().ready()
        # Override core app instances with blank application instances to exclude their URLs.
        # self.promotions_app = OscarConfig()
        # self.catalogue_app = OscarConfig()
        # self.search_app = OscarConfig()
        self.promotions_app = apps.get_app_config('oscar_promotions')

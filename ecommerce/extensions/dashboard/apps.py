from __future__ import absolute_import

from oscar.apps.dashboard import apps


class DashboardConfig(apps.DashboardConfig):
    name = 'ecommerce.extensions.dashboard'

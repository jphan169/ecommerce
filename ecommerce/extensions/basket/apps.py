from __future__ import absolute_import

from oscar.apps.basket import apps


class BasketConfig(apps.BasketConfig):
    name = 'ecommerce.extensions.basket'

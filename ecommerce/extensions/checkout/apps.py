from __future__ import absolute_import

from django.apps import AppConfig
from oscar.apps.checkout import apps


class CheckoutAppConfig(AppConfig):
    name = 'ecommerce.extensions.checkout'
    verbose_name = 'Checkout'

    def ready(self):
        super(CheckoutAppConfig, self).ready()

        # noinspection PyUnresolvedReferences
        import ecommerce.extensions.checkout.signals  # pylint: disable=unused-import, import-outside-toplevel


class CheckoutConfig(apps.CheckoutConfig):
    name = 'ecommerce.extensions.checkout'

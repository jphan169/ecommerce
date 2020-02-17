from __future__ import absolute_import

from oscar.apps.payment import apps


class PaymentConfig(apps.PaymentConfig):
    name = 'ecommerce.extensions.payment'

    def ready(self):
        # Register signal handlers
        # noinspection PyUnresolvedReferences
        import ecommerce.extensions.payment.signals  # pylint: disable=unused-import, import-outside-toplevel

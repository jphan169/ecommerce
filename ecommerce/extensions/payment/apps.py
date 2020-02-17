from __future__ import absolute_import

from oscar.apps.payment import apps
from ecommerce.extensions.payment.urls import urlpatterns


class PaymentConfig(apps.PaymentConfig):
    name = 'ecommerce.extensions.payment'

    def ready(self):
        # Register signal handlers
        # noinspection PyUnresolvedReferences
        import ecommerce.extensions.payment.signals  # pylint: disable=unused-import, import-outside-toplevel

    def get_urls(self):
        """Returns the URL patterns for the Payment Application."""
        return self.post_process_urls(urlpatterns)

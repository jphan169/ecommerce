from __future__ import absolute_import

from django.conf.urls import include, url

from django.apps import apps
from ecommerce.extensions.payment.apps import PaymentConfig as payment

application = apps.get_app_config('ecommerce.extensions')

urlpatterns = [
    url(r'^api/', include('ecommerce.extensions.api.urls', namespace='api')),
    url(r'^payment/', include(payment.urls)),
    url(r'', include(application.urls[0])),
]

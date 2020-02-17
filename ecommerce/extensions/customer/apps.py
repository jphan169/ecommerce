from __future__ import absolute_import

from auth_backends.views import EdxOAuth2LoginView
from oscar.apps.customer import apps

from ecommerce.core.views import LogoutView


class CustomerConfig(apps.CustomerConfig):
    name = 'ecommerce.extensions.customer'

    login_view = EdxOAuth2LoginView
    logout_view = LogoutView



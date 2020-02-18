from __future__ import absolute_import

from oscar.apps.customer import apps


class CustomerConfig(apps.CustomerConfig):
    name = 'ecommerce.extensions.customer'

    def ready(self):
        from auth_backends.views import EdxOAuth2LoginView
        from ecommerce.core.views import LogoutView
        self.login_view = EdxOAuth2LoginView
        self.logout_view = LogoutView



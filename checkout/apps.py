from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        return checkout.signals
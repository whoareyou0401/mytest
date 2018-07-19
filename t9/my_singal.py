from django.dispatch import Signal

action = Signal(providing_args=['param1', 'param2'])
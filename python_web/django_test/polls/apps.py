from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class PollsConfig(AppConfig):
    name = 'polls'

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
from django.apps import AppConfig


class BoardConfig(AppConfig):
    name = 'board'

    # Почему-то необходимо, чтобы сигналы работали
    def ready(self):
        import board.signals

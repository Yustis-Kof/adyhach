from django.apps import AppConfig


class BoardConfig(AppConfig):
    name = 'board'
    boards = []

    # Почему-то необходимо, чтобы сигналы работали
    def ready(self):
        import board.signals
        self.boards = ['a', 'b']
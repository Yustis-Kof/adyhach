from .models import Board

def nav(request):
    boards = Board.objects.all()
    return {
        'boards': boards,
    }
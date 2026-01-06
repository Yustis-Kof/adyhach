from .models import Board

def nav(request):
    boards = Board.objects.all().order_by('code')
    return {
        'boards': boards,
    }
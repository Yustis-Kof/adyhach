from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Board, Thread, Post
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView



def home(request):
    return render(request, 'home.html')


def faq(request):
    return render(request, 'faq.html')

#def b(request):
#    threads = Thread.objects.all()
#    print(threads.first().post_set.first().id)
#    #  
#    context = {
#        'name': 'Бред',
#        'threads': threads
#    }
#
#
#    return render(request, 'board.html', context)



class BoardView(ListView):
    url = 'board'
    model = Thread
    template_name = 'board.html'
    context_object_name = 'threads'
    ordering = '-last'
    paginate_by = 2

    def get_queryset(self):
        self.queryset = Thread.objects.filter(board__code=self.kwargs['code'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        # Да, это реально решение из документации
        context = super().get_context_data(**kwargs)

        context["name"] = Board.objects.get(code=self.kwargs['code']).name
        context["board"] = self.kwargs['code']
        return context
    
    def post(self, request, code, *args, **kwargs):
        form = request.POST.dict()
        print(request.POST)
        if 'reply' in request.POST:
            Post.objects.create(
                thread = Thread.objects.get(id=form["thread"]),
                content = form["content"]
            )

            self.object_list = self.get_queryset()
            allow_empty = self.get_allow_empty()
            context=self.get_context_data()
        return HttpResponseRedirect(reverse(self.url, kwargs=self.kwargs)) # Редиректим к этой же странице, чтобы не было повторной отправки

class ThreadView(BoardView):
    model = Post
    template_name = 'thread.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        # Да, это реально решение из документации
        context = super().get_context_data(**kwargs)

        this_board = Board.objects.get(code=self.kwargs['code'])
        this_thread = Post.objects.get(local_id=self.kwargs['op_id'], thread__board=this_board).thread
        context["thread"] = this_thread
        context["name"] = this_thread.title
        return context



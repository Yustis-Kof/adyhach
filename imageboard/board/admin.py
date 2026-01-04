from django.contrib import admin
from .models import Board, Thread, Post

admin.site.register([Board, Thread, Post])
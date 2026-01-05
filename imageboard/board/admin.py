from django.contrib import admin
from .models import *

admin.site.register([Board, Thread, Post, Attachment])
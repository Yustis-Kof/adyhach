from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Post

@receiver(pre_save, sender=Post)
def set_local_id(sender, instance, **kwargs):
    # Все посты этой доски. Да, я удивлён, что в django так можно. Удобно.
    # last_post = sender.objects.all().filter(thread__board=sender.thread.board).last()
    # Но я всё же лучше реализую, добавив борде атрибут last
    if instance.local_id is None:
        instance.local_id = instance.thread.board.last + 1



@receiver(post_save, sender=Post)
def update_last(sender, instance, created, **kwargs):
    if created:
        thread = instance.thread

        thread.last = instance.local_id
        thread.save()
        thread.board.last = thread.last
        thread.board.save()

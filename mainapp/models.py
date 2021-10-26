from django.db import models


class Message(models.Model):

    author = models.CharField(max_length=100, verbose_name='Автор')
    email = models.EmailField(verbose_name='Електронная почта')
    text = models.TextField(verbose_name='Текст сообщения', blank=False, max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


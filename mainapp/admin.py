from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('author','email','text','create_date','update_date')

admin.site.register(Message, MessageAdmin)

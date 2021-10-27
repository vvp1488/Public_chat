from django.urls import path

from .views import MessageList, MessageDetail, NewMessage

urlpatterns = [
    path('messages/list/<int:page>/', MessageList.as_view(), name='messages_list'),
    path('messages/single/<int:id>/', MessageDetail.as_view()),
    path('newmessage/', NewMessage.as_view(), name='new_message'),
]
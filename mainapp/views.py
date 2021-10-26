from django.http import Http404
from rest_framework.response import Response

from .models import Message
from rest_framework import generics, views
from .serializers import MessageSerializer, NewMessageSerializer, MessageDetailSerializer



class MessageList(views.APIView):
    '''
    Вывод списка сообщений
    '''

    def get(self,request, *args,**kwargs):
        page = kwargs.get('page')
        if page == '0':
            messages = Message.objects.all()[:10]
        else :
            page = page*10
            messages = Message.objects.all()[page:page+10]
            if messages.count() == 0:
                raise Http404

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class MessageDetail(views.APIView):
    '''Вывод полной информации об сообщении'''

    def get(self,request, *args, **kwargs):
        message = Message.objects.get(id=kwargs.get('id'))
        serializer = MessageDetailSerializer(message)
        return Response(serializer.data)


class NewMessage(generics.CreateAPIView):
    '''Создание нового сообщения'''

    serializer_class = NewMessageSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            serializer.save(author='Гость')
        else:
            serializer.save(author=self.request.user.username)






from .models import Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = (
            'author',
            'email',
            'text'
        )


class NewMessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = (
            'author',
            'email',
            'text',
        )


class MessageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = (
            'id',
            'author',
            'email',
            'text',
            'create_date',
            'update_date'
        )
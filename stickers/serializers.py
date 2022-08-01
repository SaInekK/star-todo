from .models import Todo, Sticker, Table
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'text', 'completed']


class StickerSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)
    class Meta:
        model = Sticker
        fields = ['id', 'text', 'todos', 'image']

class TableSerializer(serializers.ModelSerializer):
    # depth = 2
    stickers = StickerSerializer(many=True)
    class Meta:
        model = Table
        read_only_fields = ['user']
        fields = ['id', 'stickers']
        
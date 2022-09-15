from .models import Todo, Sticker, Table
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    sticker_id = serializers.IntegerField(required=True)

    class Meta:
        model = Todo
        fields = ['id', 'text', 'completed', 'sticker_id']
        read_only_fields = ['id', ]


class StickerSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, required=False)
    table_id = serializers.IntegerField(required=True)

    class Meta:
        model = Sticker
        fields = ['id', 'text', 'image', 'todos', 'table_id']
        read_only_fields = ['id', ]

    def create(self, validated_data):
        todos_data = validated_data.pop('todos', [])
        sticker = Sticker.objects.create(**validated_data)
        for todo_data in todos_data:
            Sticker.objects.create(sticker=sticker, **todo_data)
        return sticker


class TableSerializer(serializers.ModelSerializer):
    stickers = StickerSerializer(many=True, required=False)

    class Meta:
        model = Table
        fields = ['id', 'stickers', ]
        read_only_fields = ['id', 'stickers', ]

    def create(self, validated_data):
        stickers_data = validated_data.pop('stickers', [])
        table = Table.objects.create(**validated_data)
        for sticker_data in stickers_data:
            Sticker.objects.create(table=table, **sticker_data)
        return table

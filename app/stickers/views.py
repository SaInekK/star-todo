from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Sticker, Table, Todo
from .permissions import IsOwner
from .serializers import TableSerializer, StickerSerializer, TodoSerializer


class StickerViewSet(viewsets.ModelViewSet):
    queryset = Sticker.objects.all()
    serializer_class = StickerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        table_id = self.request.data.get('table_id')
        table_instance = Table.objects.filter(id=table_id).first()
        if not serializer.is_valid(raise_exception=True):
            print(serializer.errors)
        serializer.save(table=table_instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Table.objects.all()
        return Sticker.objects.filter(table__user=user).prefetch_related('todos')


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Table.objects.all()
        return Table.objects.filter(user=user).prefetch_related('stickers', 'stickers__todos')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        sticker_id = self.request.data.get('sticker_id')
        sticker_instance = Sticker.objects.filter(id=sticker_id).first()
        if not serializer.is_valid(raise_exception=True):
            print(serializer.errors)
        serializer.save(sticker=sticker_instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Table.objects.all()
        return Todo.objects.filter(sticker__table__user=user)

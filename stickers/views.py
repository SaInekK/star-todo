from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TableSerializer
from .models import Sticker, Table

# class StickerViewSet(viewsets.ModelViewSet):
#     queryset = Sticker.objects.all()
#     serializer_class = TableSerializer
#     # permission_classes = [IsAccountAdminOrReadOnly]
    
#     # def list(self, request):
#     #     serializer = self.get_serializer(self.get_queryset(), many=True)
#     #     return self.get_paginated_response(self.paginate_queryset(serializer.data))
    
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_superuser:
#             return Sticker.objects.all()
#         return Sticker.objects.filter(user=user.user)
    

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
    
    # def list(self, request):
    #     serializer = self.get_serializer(self.get_queryset(), many=True)
    #     return self.get_paginated_response(self.paginate_queryset(serializer.data))
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Table.objects.all()
        return Table.objects.filter(user=user.user)
from django.urls import include, path
from rest_framework import routers
from .views import TableViewSet, StickerViewSet, TodoViewSet


router = routers.DefaultRouter()
router.register(r'table', TableViewSet)
router.register(r'sticker', StickerViewSet)
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

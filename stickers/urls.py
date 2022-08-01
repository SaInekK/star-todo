from django.urls import include, path
from rest_framework import routers
from .views import TableViewSet

router = routers.DefaultRouter()
router.register(r'table', TableViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("stickers/", StickerViewSet.as_view(), name="article_list"),
]
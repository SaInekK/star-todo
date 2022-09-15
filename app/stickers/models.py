from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tables')

    def __str__(self):
        return f'{self.pk} Table'

    def get_absolute_url(self):  # TEST
        return reverse("table_read", kwargs={"pk": self.pk})


class Sticker(models.Model):
    text = models.CharField(default='Sample sticker', max_length=255)
    image = models.ImageField(blank=True, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='stickers')

    def __str__(self):
        return f'{self.pk} Sticker'


class Todo(models.Model):
    text = models.CharField(default='Sample todo', max_length=255)
    completed = models.BooleanField(default=False)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE, null=True, blank=True, related_name='todos')

    def __str__(self):
        return f'{self.text} Todo'

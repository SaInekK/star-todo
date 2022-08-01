from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Todo(models.Model):
    text = models.CharField(default='Sample todo', max_length=255)
    completed = models.BooleanField(default=False)
    sticker = models.ForeignKey('stickers.Sticker', on_delete=models.CASCADE, null=True, blank=True, related_name='todos')


class Sticker(models.Model):
    text = models.CharField(default='Sample sticker', max_length=255)
    # todos = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True, blank=True, related_name='stickers')
    image = models.ImageField(blank=True)
    
    
class Table(models.Model):
    user = models.ManyToManyField(User)
    stickers = models.ManyToManyField(Sticker, blank=True)
    


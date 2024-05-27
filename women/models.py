from typing import Any
from django.db import models


class Women(models.Model):
    def __init__(self, *args, **kwargs):
        self.first_name = models.CharField('Имя', max_length=255)
        self.last_name = models.CharField('Фамилия', max_length=255)
        self.description = models.TextField('Описание', max_length=2000)
        self.category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='woman')
        self.tags = models.ManyToOneRel(to='Tag', on_delete=models.CASCADE, related_name='woman')
        self.husband = models.OneToOneRel(to='Husband', on_delete=models.CASCADE, related_name='wife')
        self.created_time = models.DateTimeField('Время создания', auto_now_add=True)
        self.updated_time = models.DateTimeField('Последние изменение', auto_now=True)
        self.picture = models.ImageField('Фотография',)

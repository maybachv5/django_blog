from django.db import models
from django.contrib.auth.models import AbstractUser


class Ouser(AbstractUser):
    nickname = models.CharField('昵称',max_length=20,blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username
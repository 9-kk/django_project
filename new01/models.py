from django.db import models
# Create your models here.


class Post(models.Model):
    # 根据模型自动值数据库中创建一个对应的表，此表包括title, name两个字段
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title

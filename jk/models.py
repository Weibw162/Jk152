from django.db import models


# Create your models here.

class Img(models.Model):
    sn = models.IntegerField(verbose_name="图片编号")
    like_num = models.IntegerField(verbose_name="喜欢数量", default=0)

    def __str__(self):
        return str(self.sn)


class Per(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=30)
    password = models.CharField(verbose_name="密码", max_length=30)

    def __str__(self):
        return self.username


class PerLike(models.Model):
    per = models.ForeignKey('Per', verbose_name="用户", on_delete=models.CASCADE)
    img = models.ForeignKey('Img', verbose_name="图片", on_delete=models.CASCADE)

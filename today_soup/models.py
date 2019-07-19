from django.db import models

# Create your models here.

class SoupModel(models.Model):
    soup_origin_id = models.CharField('源网站ID', max_length=10)
    title = models.CharField('标题', max_length=128)
    head_url = models.URLField('头图',null=True)
    pic_urls = models.TextField('内容图片地址',null=True)
    page_url = models.URLField('源网页',null=True)
    content = models.TextField('简介',null=True)
    how_to_do = models.TextField('制作步骤',null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
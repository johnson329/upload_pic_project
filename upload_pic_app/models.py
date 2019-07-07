from django.db import models
from .storage import ImageStorage
# Create your models here.
class Pictures(models.Model):
    #数据库中保存的是图片的存储路径
    # pic=models.ImageField(upload_to='img/')
    #加时间戳尽量避免重复
    pic = models.ImageField(upload_to='img/',storage=ImageStorage())


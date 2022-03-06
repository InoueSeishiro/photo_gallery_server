from django.db import models


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')


class Keyword(models.Model):
    keyword = models.CharField(max_length=32)


class KeywordRelation(models.Model):
    image_id = models.IntegerField()
    keyword_id = models.IntegerField()

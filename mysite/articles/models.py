from django.db import models

class Article(models.Model):
    article_name = models.CharField('Названия статьи',max_length = 50)
    article_text = models.TextField('text articles')
    # # image = models.ImageField(upload_to='images/')
    # image = models.ImageField(upload_to='articles/')

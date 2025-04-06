from django.db import models


# Create your models here.

class BaseModel(models.Model):
    author = models.CharField('автор', max_length=120)
    text = models.TextField('текст', null=False, blank=False)
    date_create = models.DateField('дата создания', auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField('заголовок', max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Comment(BaseModel):
    post = models.ForeignKey(Post, verbose_name='пост', on_delete=models.CASCADE, null=False, blank=False,
                             related_name='comments')

    def __str__(self):
        return f'{self.post} {self.text[:20]}'

    class Meta:
        verbose_name = 'коммент'
        verbose_name_plural = 'комментарии'

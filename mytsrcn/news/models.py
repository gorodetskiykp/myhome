from django.db import models


# https://docs.djangoproject.com/en/5.0/ref/models/fields/
class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Новость')
    published = models.DateTimeField(verbose_name='Дата публикации')
    # добавить автора (charfield) и вывести его в списке новостей

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-published', )

    def __str__(self):
        return '{}. {}... {}'.format(self.title, self.text[:10], self.published)

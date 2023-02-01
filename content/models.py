from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField('Название', max_length=50)
    autor = models.CharField('Автор', max_length=50)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Content" 

class NewContent(models.Model):
    title = models.CharField('Название', max_length=50)
    autor = models.CharField('Автор', max_length=50)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "NewContent"
        verbose_name_plural = "NewContent"
from django.db import models


class grupa(models.Model):
    title = models.CharField('Название группы',max_length=20)
    teacher = models.CharField('Воспитатель', max_length=50)



    def __str__(self):
         return self.title



    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'




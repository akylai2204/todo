from django.db import models



class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=350)
    data = models.DateTimeField('Дата')
    


    def __str__(self):
        return self.title




    def get_absolute_url(self):
        return f'/new/{self.id}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
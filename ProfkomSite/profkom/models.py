from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUsers(AbstractUser):

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'


class Applications(models.Model):

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'

    (typeMeals, typeSingle, typeMonthly, typeProf) = range(1, 5)
    types = [
        (typeMeals, u'Бесплатное питание'),
        (typeSingle, u'Единоразовый АПОС'),
        (typeMonthly, u'Ежемесячный АПОС'),
        (typeProf, u'Профилакторий')
    ]
    type = models.SmallIntegerField(
        choices = types
    )

    (statusNew, statusAccepted, statusRejected) = range(1, 4)
    statuses = [
        (statusNew, u'Не рассмотрена'),
        (statusAccepted, u'Принята'),
        (statusRejected, u'Отклонена')
    ]
    status = models.SmallIntegerField(
        choices = statuses,
        default = statusNew
    )

    period = models.ForeignKey('Periods', on_delete = models.PROTECT) #TODO : add message
    filesAttached = models.ManyToManyField('Files')
    dateSubmitted = models.DateTimeField(auto_now_add = True)
    dateAccepted = models.DateTimeField(blank = True)
    revisedBy = models.ForeignKey('AppUsers', on_delete = models.SET(0), blank = True)


class Files(models.Model):

    class Meta:
        verbose_name = u'Файл'
        verbose_name_plural = u'Файлы'

    owner = models.ForeignKey('AppUsers', on_delete = models.CASCADE)
    file = models.FileField('', )


class Periods(models.Model):

    class Meta:
        verbose_name = u'Период'
        verbose_name_plural = u'Периоды'


    createdBy = models.ForeignKey('AppUsers', on_delete = models.SET(0))
    dateStart = models.DateTimeField()
    dateEnd = models.DateTimeField()
    dateApplicationStart = models.DateTimeField()
    dateApplicationEnd = models.DateTimeField()




from django.db import models
import datetime


class Statistic(models.Model):

    date_stat = models.DateField(default=datetime.date.today())
    spent = models.IntegerField(null=False)
    get_money = models.IntegerField(default=0)


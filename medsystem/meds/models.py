from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Профиль пользователя """
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    sex = models.CharField(5, choices=['man', 'woman'])
    birth_date = models.DateField()
    first_name = models.CharField(20)
    last_name = models.CharField(20)
    education = models.CharField(100, blank=True)
    points = models.IntegerField()


class SprService(models.Model):
    """ Справочник услуг и цены на них """
    title = models.CharField(50)
    price = models.IntegerField()


class Service(models.Model):
    """ Стоимость услуг каждого доктора """
    doctor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='servises')
    service = models.ForeignKey(SprService, on_delete=models.PROTECT, related_name='spr')


class PointTransaction(models.Model):
    """ Транзакции попоплнения счета """
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='transactions')
    type = models.CharField(10, choices=['plus', 'minus'])
    price = models.IntegerField()


class Advice(models.Model):
    """ Консультация между доктором и пациентом"""
    active = models.BooleanField(default=False)
    problem = models.TextField()
    doctor = models.ForeignKey(User, on_delete=models.PROTECT)
    patient = models.ForeignKey(User, on_delete=models.PROTECT)
    diagnoz = models.CharField(50, blank=True)


class AdviceMessages(models.Model):
    """ Консультация между доктором и пациентом"""
    advice = models.ForeignKey(Advice, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now=True)


class AdviceResult(models.Model):
    """ Назначение доктором для пациента по результатам консультации"""
    advice = models.ForeignKey(Advice, on_delete=models.PROTECT)
    drug_name = models.CharField(50)
    period = models.IntegerField()  # количество дней приема
    per_day = models.IntegerField()  # кол-во в день
    dosage = models.FloatField()  # сколько сьесть/выпить за один прием




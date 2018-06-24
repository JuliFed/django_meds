from django.db import models
from django.contrib.auth.models import User
from .utils.current_user import get_current_user


class Profile(models.Model):
    """ Профиль пользователя """
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile', default=get_current_user)
    email = models.EmailField()
    sex = models.CharField(max_length=5, choices=(('man', 'man'), ('woman', 'woman')))
    birth_date = models.DateField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    education = models.CharField(max_length=100, blank=True)
    points = models.IntegerField(default=100)

    def __str__(self):
        return self.user.username


class SprService(models.Model):
    """ Справочник услуг и цены на них """
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    @property
    def get_doctors(self):
        return Doctor.objects.filter(category=self)
    
    def __str__(self):
        return self.title


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='doctors')
    service = models.ForeignKey(SprService, on_delete=models.PROTECT, related_name='spr')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='doctors')

    def __str__(self):
        return '{} {}'.format(self.user, self.service)


class PointTransaction(models.Model):
    """ Транзакции попоплнения счета """
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='transactions', default=get_current_user)
    type = models.CharField(max_length=10, choices=(('plus', 'пополнение'), ('minus', 'расход')))
    price = models.IntegerField()


class Advice(models.Model):
    """ Консультация между доктором и пациентом"""
    closed = models.BooleanField(default=False)
    problem = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name='advices', null=True)
    patient = models.ForeignKey(User, on_delete=models.PROTECT, related_name='patient', default=get_current_user)
    diagnoz = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='advices')


class AdviceMessages(models.Model):
    """ Консультация между доктором и пациентом"""
    advice = models.ForeignKey(Advice, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=get_current_user)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now=True)


class AdviceResult(models.Model):
    """ Назначение доктором для пациента по результатам консультации"""
    advice = models.ForeignKey(Advice, on_delete=models.PROTECT)
    drug_name = models.CharField(max_length=50)
    period = models.IntegerField()  # количество дней приема
    per_day = models.IntegerField()  # кол-во в день
    dosage = models.FloatField()  # сколько сьесть/выпить за один прием



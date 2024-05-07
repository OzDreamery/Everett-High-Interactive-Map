from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RoomInput(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    day_a_period_1 = models.IntegerField(default=1000)
    day_a_period_2 = models.IntegerField(default=1000)
    day_a_period_3 = models.IntegerField(default=1000)
    day_a_period_4 = models.IntegerField(default=1000)
    day_b_period_1 = models.IntegerField(default=1000)
    day_b_period_2 = models.IntegerField(default=1000)
    day_b_period_3 = models.IntegerField(default=1000)
    day_b_period_4 = models.IntegerField(default=1000)
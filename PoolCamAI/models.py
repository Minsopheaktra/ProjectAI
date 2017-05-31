from django.db import models


# Create your models here.


class Camera(models.Model):
    title = models.CharField(max_length=80)
    created_date = models.DateTimeField("Init Date")
    current_date = models.DateTimeField("Last Modified Date")
    photo = models.FileField()


class Notification(models.Model):
    title = models.CharField(max_length=80)
    current_date = models.DateTimeField("Init Date")
    photo = models.FileField()
    num_person = models.IntegerField(default=0)


class Setting(models.Model):
    notification = models.BooleanField(default=True)
    # phone
    # user
    # email


class Schedule(models.Model):
    # profile = models.IntegerField
    # start_time = models.
    # end_time = models
    pass


class Profile(models.Model):
    name = models.CharField(max_length=40)

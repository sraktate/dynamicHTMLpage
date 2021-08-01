from django.db import models


class EventDetails(models.Model):
    event_name = models.CharField(max_length=32)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=32)
    image = models.ImageField(blank=True, upload_to='pic_folder/')
    is_like = models.BooleanField(null=True)

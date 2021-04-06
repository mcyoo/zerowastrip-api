from django.db import models


class Cafe(models.Model):

    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    open_time = models.TimeField(default="00:00:00")
    close_time = models.TimeField(default="00:00:00")
    holiday = models.DateField()
    meeting_time = models.DateField()
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    content = models.TextField()
    file = models.ImageField()

    def __str__(self):
        return self.title

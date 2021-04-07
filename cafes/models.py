from django.db import models


class Cafe(models.Model):

    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"
    no_holiday = "null"
    no_holiday = "null"

    STATUS_CHOICES = (
        (Monday, "월요일"),
        (Tuesday, "화요일"),
        (Wednesday, "수요일"),
        (Thursday, "목요일"),
        (Friday, "금요일"),
        (Saturday, "토요일"),
        (Sunday, "일요일"),
        (no_holiday, "휴일없음"),
    )

    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    open_time = models.TimeField(default="00:00:00")
    close_time = models.TimeField(default="00:00:00")
    holiday = models.CharField(
        max_length=16, choices=STATUS_CHOICES, default=Monday
    )
    meeting_time = models.DateField()
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    content = models.TextField()
    file1 = models.ImageField()
    file2 = models.ImageField()
    file3 = models.ImageField()
    file4 = models.ImageField()

    def __str__(self):
        return self.title

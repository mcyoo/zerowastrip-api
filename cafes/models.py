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

    title = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    open_time = models.TimeField(default="00:00:00")
    close_time = models.TimeField(default="00:00:00")
    holiday = models.CharField(
        max_length=16, choices=STATUS_CHOICES, default=no_holiday
    )
    special_holiday = models.DateField(
        blank=True)
    check_time = models.BooleanField(default=False)

    no_straw = models.BooleanField(default=False)
    no_plasticCup = models.BooleanField(default=False)
    use_biodegradable = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    discount_pruncup = models.BooleanField(default=False)
    allow_pat = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    desert = models.BooleanField(default=False)
    pruncup_rental = models.BooleanField(default=False)

    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    kakaomap_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

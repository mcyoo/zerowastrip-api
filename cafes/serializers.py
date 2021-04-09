from rest_framework import serializers
from .models import Cafe
import datetime


class CafeSerializer(serializers.ModelSerializer):
    cafe_open = serializers.SerializerMethodField()

    class Meta:
        model = Cafe
        fields = '__all__'

    def get_cafe_open(self, obj):
        t = ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday"]

        now = datetime.datetime.now()
        open_time = obj.open_time
        close_time = obj.close_time
        holiday = obj.holiday
        if holiday == t[now.weekday()]:
            return False

        now = now.strftime('%H:%M:%S')

        return str(open_time) < now < str(close_time)

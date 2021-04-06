from rest_framework import serializers
from .models import Cafe
import datetime


class CafeSerializer(serializers.ModelSerializer):
    cafe_open = serializers.SerializerMethodField()

    class Meta:
        model = Cafe
        fields = '__all__'

    def get_cafe_open(self, obj):
        now = datetime.datetime.now()
        open_time = obj.open_time
        close_time = obj.close_time

        now = now.strftime('%H:%M:%S')
        #now = datetime.datetime.strptime(now, '%H:%M:%S')

        print(open_time)
        print(close_time)
        print(now)

        return str(open_time) < now < str(close_time)
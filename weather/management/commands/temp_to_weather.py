from observations.models import TemperatureReading, WeatherReading
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Converts temperature objects to weather objects"

    def handle(self, *args, **options):
        for temp in TemperatureReading.objects.all():
            datetime = temp.datetime
            weather = WeatherReading.objects.filter(user=temp.user,
                                                    datetime__year=datetime.year,
                                                    datetime__month=datetime.month,
                                                    datetime__day=datetime.day,
                                                    datetime__hour=datetime.hour).first()
            if weather:
                if weather.temperature == -1:
                    print('Converting Temperature on {0}'.format(datetime))
                    weather.temperature = temp.value
                    weather.unit = temp.unit
                    weather.save()
                    print('Temperature saved')
            else:
                print('Temp Object: {0} on {1} has no weather.'.format(temp.temperature_reading_id, temp.datetime))


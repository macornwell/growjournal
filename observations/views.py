from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from observations.models import TemperatureReading
from observations.forms import TemperatureReadingForm


def add_temperature_reading(request):
    lastReading = ''
    lastReadingObj = TemperatureReading.objects.order_by('-datetime').first()
    if lastReadingObj:
        lastReading = str(lastReadingObj)
    if request.method == 'POST':
        form = TemperatureReadingForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.save()
            messages.info(request, 'Temperature Saved!')
            lastReading = str(model)
        else:
            messages.error(request, 'Unable to save Temperature.')
    else:
        form = TemperatureReadingForm()
    return render(request, 'observations/temperature_reading.html', {'form': form, 'last_reading': lastReading})


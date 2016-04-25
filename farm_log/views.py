from datetime import timedelta
from django.shortcuts import render
import django.utils.timezone as timezone
from django.contrib import messages
from observations.models import TemperatureReading, WeatherReading, Observation
from work.models import WorkCompleted
from livestock.models import EggCollection


def home(request):
    datesToReport = _get_dates_to_report()
    data = {'daily_reports': []}
    for date in datesToReport:
        data['daily_reports'].append(get_daily_report(date))
    return render(template_name='home.html', context=data, request=request)


def _get_dates_to_report():
    now = timezone.now()
    datesToReport = [now,]
    for i in range(5):
        if not i:
            continue
        newDate = now - timedelta(days=i)
        datesToReport.append(newDate)
    return datesToReport

def _build_work_summary(date):
    projectToItems ={}
    for work in WorkCompleted.objects.filter(datetime__year=date.year,
                                             datetime__month=date.month,
                                             datetime__day=date.day):
        project = work.project or ''
        if project not in projectToItems:
            projectToItems[project] = []
        projectToItems[project].append(work)
    listOfData = []
    for proj in projectToItems.keys():
        summary = WorkSummaryForDay()
        summary.project_name = proj.name
        summary.work_items = list(projectToItems[proj])
        listOfData.append(summary)
    return listOfData



def get_daily_report(date):
    report = DailyReport()
    report.date = date

    report.temperature_readings = TemperatureReading.get_readings_by_date(date)
    report.weather_readings = WeatherReading.get_readings_by_date(date)
    report.observations = Observation.get_observations_by_date(date)
    report.work_completed = _build_work_summary(date)
    report.eggs = EggCollection.get_total_eggs_collected_on_date(date)

    return report


class DailyReport:
    date = None
    eggs = 0
    temperature_readings = []
    weather_readings = []
    observations = []
    work_completed = []


class WorkSummaryForDay:
    project_name = None
    work_items = []

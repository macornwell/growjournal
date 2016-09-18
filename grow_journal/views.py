import datetime
from datetime import timedelta
from django.shortcuts import render
from django.core.urlresolvers import reverse
import django.utils.timezone as timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.html import escape


LOG_DAYS_PER_PAGE = 5

def home(request):
    data = {}
    loginUrl = reverse('admin:login')
    loginNextUrl = escape(request.path)
    data['loginUrl'] = '{0}?next={1}'.format(loginUrl, loginNextUrl)
    return render(template_name='home.html', context=data, request=request)

def setup(request):
    data = {}
    return render(template_name='setup.html', context=data, request=request)

"""
def home(request):
    return home_with_page(request, 0)

def home_with_page(request, page):
    if not page:
        page = 0
    page = int(page)
    if page < 0:
        page = 0
    datesToReport = _get_dates_to_report(page)
    data = {'daily_reports': []}
    for date in datesToReport:
        data['daily_reports'].append(get_daily_report(date))
    data['older_page'] = page + 1
    data['newer_page'] = page - 1
    return render(template_name='home.html', context=data, request=request)




@login_required
def worksite(request):
    datesToReport = _get_dates_to_report(0)
    data = {'daily_reports': []}
    for date in datesToReport:
        data['daily_reports'].append(get_daily_report(date))
    data['older_page'] = 1
    data['newer_page'] = 0
    return render(template_name='worksite.html', context=data, request=request)


def _get_dates_to_report(page):
    now = timezone.now()
    datesToReport = []
    starting = page * LOG_DAYS_PER_PAGE
    ending = starting + LOG_DAYS_PER_PAGE
    for i in range(starting, ending):
        newDate = now - timedelta(days=i)
        newDate = datetime.date(newDate.year, newDate.month, newDate.day)
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
        summary.project_name = proj
        summary.work_items = list(projectToItems[proj])
        listOfData.append(summary)
    return listOfData


def get_daily_report(date):
    report = DailyReport()
    report.date = date

    report.weather_readings = list(WeatherReading.get_readings_by_date(date))
    report.observations = list(Observation.get_observations_by_date(date))
    report.work_completed = _build_work_summary(date)
    report.eggs = EggCollection.get_total_eggs_collected_on_date(date)
    report.harvests = Harvest.get_harvests_by_date(date)

    return report


class DailyReport:
    date = None
    eggs = 0
    temperature_readings = []
    weather_readings = []
    observations = []
    work_completed = []
    harvests = []


class WorkSummaryForDay:
    project_name = None
    work_items = []




def _open_model_trend(request):

    queryset = TemperatureReading.objects.all()
    data =  [
    ]
    dateSeen = {}
    for t in queryset:
        day = t.datetime.day
        month = t.datetime.month
        year = t.datetime.year
        if year in dateSeen:
            if month in dateSeen[year]:
                if day in dateSeen[year][month]:
                    continue
                else:
                    dateSeen[year][month].append(day)
            else:
                dateSeen[year] = {month: [day,]}
        else:
            dateSeen[year] = {month: [day,]}

        data.append([int(t.datetime.strftime('%Y%m%d')), float(t.value)])
    data = sorted(data, key=lambda x: x[0])
    data.insert(0, ['Date', 'Value'])
    chart = LineChart(SimpleDataSource(data=data), html_id="line_chart")
    data = {'chart': chart}
    s = chart.as_html()

    return render(template_name='model_popup.html', context=data, request=request)
    """
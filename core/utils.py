import pytz


LOCAL = pytz.timezone('US/Central')



def get_local_time_formatted(dateTime):
    text = dateTime.astimezone(LOCAL).strftime('%b %d %Y: %H:%M:%S')
    return text


def get_summary(totalText, summary=None, maxSummarySize=25):
    text = summary
    if not text:
        text = totalText[:maxSummarySize]
        if len(totalText) > maxSummarySize:
            text += '...'
    return text


def get_summary_with_datetime(dateTime, totalText, summary=None, maxSummarySize=25):
    summary = get_summary(totalText, summary=summary, maxSummarySize=maxSummarySize)
    return '{0} - {1}'.format(get_local_time_formatted(dateTime), summary)

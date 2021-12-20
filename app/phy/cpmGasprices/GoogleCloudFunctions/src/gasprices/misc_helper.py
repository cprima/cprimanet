from datetime import datetime, timedelta, time


def list_datetime_obj(days_range, offset=1):
    """Returns datetime objects since yesterday as a list"""
    retval = []
    end_date = datetime.now() - timedelta(days=offset)
    start_date = end_date - days_range * timedelta(days=1)
    for i in range((end_date - start_date).days):
        d = end_date - i * timedelta(days=1)
        d2 = datetime(d.year, d.month, d.day)
        retval.append(d2)
    return retval


def get_end_of_day_time(d):
    return datetime.combine(d.date(), time.max)

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


def get_end_of_day_time(dt):
    return datetime.combine(dt.date(), time.max)


def get_iso_week_no(dt):
    try:
        retval = dt.isocalendar().week
    except AttributeError as e:
        retval = dt.isocalendar()[1]
    finally:
        print(retval)
        return retval
    return

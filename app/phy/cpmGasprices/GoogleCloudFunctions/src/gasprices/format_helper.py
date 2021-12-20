from datetime import datetime, date
import time


def parse_metadata_to_datetime(str_date, str_time):
    try:
        from_time = time.strptime(str_time, '%H:%M:%S')
    except ValueError:
        from_time = time.strptime(str_time, '%H:%M')
    except Exception as e:
        print(e)
    finally:
        return datetime.strptime(
            str_date + ' ' + str_time, '%Y-%m-%d %H:%M:%S')


def format_templatestring(tpl, from_datetime, thru_datetime=datetime.now(), location=""):
    #print(from_datetime, thru_datetime)
    return tpl.format(
        location=location,
        from_year=from_datetime.year, from_month=from_datetime.month, from_day=from_datetime.day,
        from_hour=from_datetime.hour, from_minute=from_datetime.minute, from_second=from_datetime.second,
        to_year=thru_datetime.year, to_month=thru_datetime.month, to_day=thru_datetime.day,
        to_hour=thru_datetime.hour, to_minute=thru_datetime.minute, to_second=thru_datetime.second
    )


def list_formatted_tplstr(tpl, ld, location=""):
    retval = []
    for d in ld:
        t = format_templatestring(tpl, d, d, location)
        retval.append(t)
    return retval


def add_date_time(d, str_time):
    try:
        from_time = datetime.strptime(str_time, '%H:%M:%S')
    except ValueError:
        from_time = datetime.strptime(str_time, '%H:%M')
    except Exception as e:
        print(e)
    return datetime.combine(d.date(), from_time.time())

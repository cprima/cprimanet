import os
import datetime
import calendar


tk_stations_url_tpl = "https://dev.azure.com/tankerkoenig/362e70d1-bafa-4cf7-a346-1f3613304973/_apis/git/repositories/0d6e7286-91e4-402c-af56-fa75be1f223d/items?path=/stations/{year:n}/{month}/{year:n}-{month:02d}-{day:02d}-stations.csv"
tk_prices_url_tpl = "https://dev.azure.com/tankerkoenig/362e70d1-bafa-4cf7-a346-1f3613304973/_apis/git/repositories/0d6e7286-91e4-402c-af56-fa75be1f223d/items?path=/prices/{year:n}/{month}/{year:n}-{month:02d}-{day:02d}-prices.csv"
tk_prices_filename_tpl = "data/external/tankerkoenig/prices/prices_{year}-{month:02d}-{day:02d}.csv"
tk_stations_filename_tpl = "data/external/tankerkoenig/stations/current.csv"
my_subset_prices_location_date_timespan_filename_tpl = "data_interim/subset_prices_{location}_{from_year}-{from_month:02d}-{from_day:02d}_{from_hour:02d}-{from_minute:02d}-{from_second:02d}_-_{to_year}-{to_month:02d}-{to_day:02d}_{to_hour:02d}-{to_minute:02d}-{to_second:02d}.csv"
my_weeklyaggregate_prices_location_date_timespan_filename_tpl = "data_processed/weeklyaggregate_prices_{from_year}-{from_month:02d}-{from_day:02d}_{from_hour:02d}-{from_minute:02d}-{from_second:02d}_-_{to_year}-{to_month:02d}-{to_day:02d}_{to_hour:02d}-{to_minute:02d}-{to_second:02d}.csv"

figure_subtitle_tpl = "vom {from_day:02d}.{from_month:02d}. bis {to_day:02d}.{to_month:02d}. zwischen {from_hour:02d}:{from_minute:02d} und {to_hour:02d}:{to_minute:02d}"

yesterday = datetime.date.today() - datetime.timedelta(days=1)
day_delta = datetime.timedelta(days=1)
days_range = 3  # 0
end_date = datetime.date.today() - datetime.timedelta(days=1)
start_date = end_date - days_range*day_delta
daysOfWeek = {0: 'Montag', 1: 'Dienstag', 2: 'Mittwoch',
              3: 'Donnerstag', 4: 'Freitag', 5: 'Samstag', 6: 'Sonntag'}

tk_stations_url_current = tk_stations_url_tpl.format(
    year=yesterday.year, month=yesterday.month, day=yesterday.day) + "&download=true"

bucket_name = "2021.gasprices.cprima.net"

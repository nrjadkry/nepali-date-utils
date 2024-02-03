from data.data import calendar_data
from datetime import datetime, timedelta

en_max_year = 2099
en_min_year = 1944

days_in_year = 365
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Apr-Oct have 31 days. Feb has 28 days. Rest have 30 days


reference_ad = {"year": 2017, "month": 2, "day": 11}
reference_bs = {"year": 2073, "month": 10, "day": 29}


# BS
def count_days_in_year(year):
    if year not in calendar_data:
        return days_in_year

    return calendar_data[year][12]

#AD
def is_leap_year_ad(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


#BS
def is_leap_year_bs(year):
    return days_in_year != count_days_in_year(year)


def verify_english_date(year, month, day):
    return en_min_year <= year <= en_max_year and 1 <= month <= 12 and 1 <= day <= 31



def difference_in_ad(date):
    # Split the date string into year, month, and day components
    date_arr = list(map(int, date.split('/')))

    # Create a dictionary to represent the date object
    date_obj = {'year': date_arr[0], 'month': date_arr[1], 'day': date_arr[2]}

    # Create datetime objects for the base date and the input date
    date1 = datetime(reference_ad['year'], reference_ad['month'], reference_ad['day'])
    date2 = datetime(date_obj['year'], date_obj['month'], date_obj['day'])

    # Calculate the difference in days
    time_diff = date2 - date1
    diff_days = time_diff.days

    return {'diff_days': diff_days}



def english_to_nepali(year,month,day):
    if not verify_english_date(year, month, day):
        raise ValueError("Date out of range")


def convert_to_bs(day_data):
    day_count = day_data['diff_days']
    bs_date = reference_bs.copy()

    if day_count >= 0:
        bs_date['day'] += day_count
        while bs_date['day'] > calendar_data[bs_date['year']][bs_date['month'] - 1]:
            bs_date['day'] -= calendar_data[bs_date['year']][bs_date['month'] - 1]
            bs_date['month'] += 1
            if bs_date['month'] > 12:
                bs_date['year'] += 1
                bs_date['month'] = 1
    else:
        day_count = abs(day_count)
        while day_count >= 0:
            if day_count < calendar_data[bs_date['year']][bs_date['month'] - 1]:
                day_count = calendar_data[bs_date['year']][bs_date['month'] - 1] - day_count
                break
            day_count -= calendar_data[bs_date['year']][bs_date['month'] - 1]
            bs_date['month'] -= 1
            if bs_date['month'] == 0:
                bs_date['year'] -= 1
                bs_date['month'] = 12
        bs_date['day'] = day_count
    return bs_date


def ad_to_bs(date):
    return convert_to_bs(difference_in_ad(date))

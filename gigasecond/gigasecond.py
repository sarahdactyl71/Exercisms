from datetime import datetime, timedelta

def add_gigasecond(birth_date):
    gigasecond = birth_date + timedelta(seconds = 10**9)
    return gigasecond

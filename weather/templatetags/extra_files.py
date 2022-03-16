from django import template
from datetime import datetime
register = template.Library()


def fulldate(ts):
    return ts.strftime("%A %d,%m,%Y")


register.filter('fulldate', fulldate)


# Template filters to convert Unix API date to string representation of the date
def day(time):
    if time != "":
        unix = int(time)
        return datetime.utcfromtimestamp(unix).strftime("%A")


register.filter('day', day)


def date(time):
    if time != "":
        unix = int(time)
        return datetime.utcfromtimestamp(unix).strftime("%d %b")


register.filter('date1', date)
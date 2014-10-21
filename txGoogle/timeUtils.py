'''
Created on 27 jan. 2014

@author: sjuul
'''
from calendar import timegm
from datetime import datetime
import time


def datetimeToTimestamp(dt):
    return timegm(dt.utctimetuple())


def timestampToDateTime(timestamp):
    return datetime.utcfromtimestamp(timestamp)


def getYearMonthFromTimestamp(timestamp):
    if not isinstance(timestamp, datetime):
        timestamp = datetime.utcfromtimestamp(timestamp)
    return str(timestamp.year) + str(timestamp.month).zfill(2)


def getYearFromTimestamp(timestamp):
    if not isinstance(timestamp, datetime):
        timestamp = datetime.utcfromtimestamp(timestamp)
    return str(timestamp.year)


def timeTextToTimestamp(timeText):
    # http://www.timeanddate.com/library/abbreviations/timezones/military/z.html
    utcTimeText = timeText + 'UTC'
    return timegm(time.strptime(utcTimeText, '%Y%m%d%H%M%S%Z'))

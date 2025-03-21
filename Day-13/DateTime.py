# # In python we have date, time, datetime,timezone& timedelta
import datetime
# # there r 2 typess of datetime 
# # 1. Naive date times :don't have enough information to determine things like time zone or daylight savings time
# # 2. Aware date times :have enough information to determine things like time zone or daylight savings time & we can use when we need these details
# date1 = datetime.date(2024, 3, 21)
# print(date1)
# tdate = datetime.date.today() # to get the current date
# print(tdate)
# tdate_weekday = tdate.weekday()
# tdate_isoweekday = tdate.isoweekday()
# print(tdate_weekday) # Monday - 0 & Sunday -6
# print(tdate_isoweekday) # Monday - 1 & Sunday -7
# print("-------------------------------------------------------------------------------------------------")
# tdelta = datetime.timedelta(days=7)
# print(tdate+tdelta)

# bday = datetime.date(2026, 1, 11)
# till_bday = bday - tdate
# print(till_bday)
# print(till_bday.days)
# print(till_bday.total_seconds())

# print("-------------------------------------------------------------------------------------------------")
# t= datetime.time(9, 30, 45, 10500) # working with Hr,min,sec & milli secs
# # by default it doesn't have time zone information - so this is till naive but we can specify timeone using tzinfo
# print(t)
# print(t.hour)

# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100690)
# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)

# timedelta = datetime.timedelta(hours=12)
# print(dt+timedelta)
# print("-----------------------------------------------------------------------------------------------")
# dt_today = datetime.datetime.today() # returns current local time with a ime zone of none 
# # u can avoid repeated datetime.datetime by importing this way - "from datetime import datetime"
# dt_now = datetime.datetime.now() # gives us the option to pass in a timezone as below, so if timezone is empty then both now & today are similar
# # dt_utcnow = datetime.datetime.utcnow() # this is deprecated and returns a naive datetime (without timezone).
# dt_utcnow = datetime.datetime.now(datetime.timezone.utc) # directly returns a timezone-aware datetime in UTC.
# # from datetime import timezone
# # NOTE: all above 3 dt are naive datetiem & not aware - datetime we have to explicitly set those
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

print("---------------------------------------pytz---------------------------------------------------")
# pip install pytz
# The pytz library was commonly used for handling time zones in Python before Python 3.9. However, starting from Python 3.9, the standard library (datetime and zoneinfo) provides built-in timezone support, making pytz mostly unnecessary for new projects
import pytz
# NOTE: it's lways recommended to use UTC when dealing with time zones 
dt1 = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo = pytz.UTC) # this is the UTC Offset
print(dt1)
dt_now_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_now_utcnow)
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) # as utcnow() returns a naive datetime .replace(tzinfo=pytz.UTC) is a manual fix, but it's not ideal.
dt_utcnow = datetime.datetime.now(datetime.timezone.utc) # directly returns a timezone-aware datetime in UTC so need of pytz
# by importing this way - "from datetime import datetime,timezone" dt_utcnow = datetime.now(timezone.utc)
print("-----------------------------------Convert it into different time zone ------------------------------------")

dt_mtn = dt_now_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print("US/Mountain time : ",dt_mtn)

# for tz in pytz.all_timezones: # to see alll timezones
#     print(tz)

dt_tn = datetime.datetime.now()
dt_east = dt_tn.astimezone(pytz.timezone('US/Eastern')) # you cannot directly apply .astimezone() to a naive datetime object because astimezone() requires a timezone-aware datetime.
#Python does not explicitly throw an error when calling .astimezone() on a naive datetime object. However, it assumes the system's local timezone, which can lead to unexpected results.
print("Conversion not correct : ",dt_east)

dt_mtn_now = datetime.datetime.now() # returns a naive datetime (i.e., it does not contain timezone information).
mtn_tz = pytz.timezone('US/Mountain') # This creates a pytz timezone object for US/Mountain time. i.e., local time

dt_mtn = mtn_tz.localize(dt_mtn_now)
print(dt_mtn)

print("----------------------------------- iso format -----------------------------------------")
# ISO format :  best way to save dates or pass them around for internal use
print(dt_mtn.strftime('%B %d, %Y')) # March 21, 2025 strftime: to convert from 
# refer python docuentation & look at the format code

#strftime (String Format Time) → Converts a datetime object to a formatted string.
#strptime (String Parse Time) → Converts a string into a datetime object.

dt_str = 'March 21, 2025' #it's a string
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)
# NOTE:Even though strptime correctly parses the date string, the datetime object by default prints in the standard ISO format:
# 2025-03-21 00:00:00 → This is the default output of a datetime object.
# It stores the correct date, but when printed, it uses its default format.

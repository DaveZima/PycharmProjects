import os
import sys
import datetime as dt
import yfinance as yf

import pandas as pd
from pandas_datareader import data


##################################
# Global variables and constants #
##################################

JOB_NAME = None






def log_msg(catg,msg):

    cur = dt.datetime.now()
    cur_str = cur.strftime("%Y-%m-%d %H:%M:%S")
    print("%s %s: %s" % (cur_str,catg,msg))

def show_obj(obj):
    t = type(obj)
    p = dir(obj)
    print("***************")
    print("* Object Type *")
    print("***************")
    print(t)
    print("*********************")
    print("* Object Properties *")
    print("*********************")
    print(p)
    print("")

########
# main #
########

# Get program name
tmp_list = sys.argv[0].split("/")
JOB_NAME = tmp_list[len(tmp_list) - 1]

log_msg("INFO","%s starting" % (JOB_NAME))

tick_obj = yf.Ticker("TSLA")

# Ticker.history() parameters
# period: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# interval: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# start: YYYY-MM-DD datetime (if not using period)
# end: YYYY-MM-DD datetime (if not using period)
# prepost: Include Pre and Post regular market data in results? (Default is False)
# auto_adjust: Adjust all OHLC (Open/High/Low/Close prices) automatically? (Default is True)
# actions: Download stock dividends and stock splits events? (Default is True)
log_msg("INFO","Initializing the Ticker object history data")
tick_hist = tick_obj.history(period="max")


# Determine len and range of data
# shape[0] = number of rows and shape[1] = number of columns
l = len(tick_hist)
r = range(tick_hist.shape[0])
log_msg("INFO","DataFrame cols = %d rows = %d" % (tick_hist.shape[1],tick_hist.shape[0]))

col_names = []
for l in tick_hist.columns:
    col_names.append(l)

# Indices

data_top = tick_hist.head()
min_date = data_top.index[0]

data_bot = tick_hist.tail()
max_date = data_bot.index[len(data_bot.index) - 1]

x = dt.datetime(2020, 5, 17)

print("min_date: ")
print(min_date)
print("max_date: ")
print(max_date)

# Pandas replacement for python datetime.datetime object
# Different assignments

td = pd.Timestamp('2010-06-29 00:00:00')
td = pd.Timestamp(2010, 6, 29)
td = pd.Timestamp(year=2010, month=6, day=29)


# Define year trading day start and stop



# 2012-01-02
# MSFT max range = 1986-03-13 2021-01-19
# Good choice to validate year start and end
# list of dictionaries year = 2012, start = pd.Timestamp, end = pd.Timestamp
tick_obj_test = yf.Ticker("MSFT")
# tick_hist_test = tick_obj_test.history(interval="1d",start="2012-01-01",end="2012-01-07")

start_ts = pd.Timestamp(2012, 1, 1)
end_ts = pd.Timestamp(2012, 1, 7)

# end is less than.  need 1,3 and 1,4 to give you 1,3

start_ts = pd.Timestamp(2021, 1, 1)
end_ts = pd.Timestamp(2021, 1, 7)
tick_hist_test = tick_obj_test.history(start=start_ts,end=end_ts)
print(tick_hist_test)

start_ts = pd.Timestamp(2021, 12, 24)
end_ts = pd.Timestamp(2021, 12, 31)
tick_hist_test = tick_obj_test.history(start=start_ts,end=end_ts)
print(tick_hist_test)

YEAR_PERIODS = [
    {"year": 2012, "year_start": pd.Timestamp(2012,1,3), "year_end": pd.Timestamp(2012,12,28)},
    {"year": 2013, "year_start": pd.Timestamp(2013,1,2), "year_end": pd.Timestamp(2013,12,30)},
    {"year": 2014, "year_start": pd.Timestamp(2014,1,2), "year_end": pd.Timestamp(2014,12,30)},
    {"year": 2015, "year_start": pd.Timestamp(2015,1,2), "year_end": pd.Timestamp(2015,12,30)},
    {"year": 2016, "year_start": pd.Timestamp(2016,1,4), "year_end": pd.Timestamp(2016,12,30)},
    {"year": 2017, "year_start": pd.Timestamp(2017,1,3), "year_end": pd.Timestamp(2017,12,28)},
    {"year": 2018, "year_start": pd.Timestamp(2018,1,2), "year_end": pd.Timestamp(2018,12,28)},
    {"year": 2019, "year_start": pd.Timestamp(2019,1,2), "year_end": pd.Timestamp(2019,12,30)},
    {"year": 2020, "year_start": pd.Timestamp(2020,1,2), "year_end": pd.Timestamp(2020,12,30)},
    {"year": 2021, "year_start": pd.Timestamp(2021,1,4), "year_end": pd.Timestamp(2021,12,28)}
]

now_ts = pd.Timestamp.now()
print("now_ts")
print(now_ts)


# Build year_dates
# Another year_data ticker = , year_start = , year_start_price, year_end = , year_end_price =

# tick_hist_test = tick_obj_test.history(period="max")



"""
Set a 10 year time window but accommodate any min year
Best to create a dataframe
Show trailing returns (year_end - year_start) / year_end
Look for a master list of symbols (NASDAQ)
Start with a simple csv that can be imported into Google Sheets
Should be able to easily handle tens of thousands
Project is Target Finder
Good intro in to capturing financial data and pandas in python
Need to capture 2011 to 2021 start and end dates
Use sorting and filtering in Google Sheets to start
Maybe this is a start to an investing model
"""

# df.head(n) tail(n) creates a df with a subset of rows

x = tick_hist.iloc[0,1]
# print("[0,0]")
# print(x)

# type() = class  dir() = attributes getattr() = get attribute value (dataframe?)


# Determine the min max dates




# Exit gracefully
log_msg("INFO","%s completed successfully" % (JOB_NAME))
raise SystemExit(0)
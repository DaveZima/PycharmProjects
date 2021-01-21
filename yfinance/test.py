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

TRAILING_RETURNS = []
# {"year": 2012, "year_start": pd.Timestamp(2012, 1, 3), "year_start_price": 233.25,
#  "year_end": pd.Timestamp(2012, 12, 28) "year_end_price": 400.15 }


#---------------------------------------------------------------------------------------#
def log_msg(catg,msg):

    cur = dt.datetime.now()
    cur_str = cur.strftime("%Y-%m-%d %H:%M:%S")
    print("%s %s: %s" % (cur_str,catg,msg))

#---------------------------------------------------------------------------------------#
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

# ---------------------------------------------------------------------------------------#
def current_year():

    return int(str(dt.date.today())[:4])

#---------------------------------------------------------------------------------------#
def current_week():

    now_dt = dt.datetime.combine(dt.date.today(), dt.datetime.min.time())
    start_dt = now_dt - dt.timedelta(days=now_dt.weekday()+1)
    end_dt = start_dt + dt.timedelta(days=6)
#    log_msg("DEBG","now_dt=%s start_dt=%s end_dt=%s" % (now_dt,start_dt,end_dt))

    return start_dt, end_dt

#---------------------------------------------------------------------------------------#
def validate_year_periods():

    log_msg("INFO","Validating year periods")

    current_yr = current_year()

    for p in YEAR_PERIODS:

        year = p["year"]
        year_start = p["year_start"]
        year_end = p["year_end"]
        log_msg("INFO","Validating %d start=%s end=%s" % (year,year_start,year_end))

        # Create a MSFT yfinance ticker object. Microsoft started issuing stock in the 1980s
        # which makes it good stock to test our 2012-2021 period.

        tick_obj = yf.Ticker("MSFT")

        ###########################
        # Capture year_start data #
        ###########################

        start_ts = pd.Timestamp(year, 1, 1)
        end_ts = pd.Timestamp(year, 1, 7)
        tick_hist = tick_obj.history(start=start_ts, end=end_ts)
        if tick_hist.empty:
            log_msg("EROR","Period start dataframe is empty")
            raise SystemExit(1)

        # Trading Date is the index of the Ticker.History() DataFrame
        # year_start, year_start_close

        data_top = tick_hist.head()
        year_start = data_top.index[0]
        print("*** year_start ***")
        print(year_start)
        print("*** year_start DataFrame ***")
        print(tick_hist)

        #########################
        # Capture year_end data #
        #########################

        if year == current_yr:
            start_ts, end_ts = current_week()
        else:
            start_ts = pd.Timestamp(year, 12, 24)
            end_ts = pd.Timestamp(year, 12, 31)

        tick_hist = tick_obj.history(start=start_ts, end=end_ts)
        if tick_hist.empty:
            log_msg("EROR","Period end dataframe is empty")
            raise SystemExit(1)

        if year == current_yr:
            log_msg("DEBG","start_ts=%s end_ts=%s" % (start_ts,end_ts))
            print(tick_hist)

########
# main #
########

# Get program name
tmp_list = sys.argv[0].split("/")
JOB_NAME = tmp_list[len(tmp_list) - 1]

log_msg("INFO","%s starting" % (JOB_NAME))
log_msg("INFO","Current year = %d" % (current_year()))

validate_year_periods()

raise SystemExit(0)



# Exit gracefully
log_msg("INFO","%s completed successfully" % (JOB_NAME))
raise SystemExit(0)